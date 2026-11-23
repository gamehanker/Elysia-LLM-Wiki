from pathlib import Path
from bs4 import BeautifulSoup
import re
R=Path(__file__).resolve().parents[1]
html=BeautifulSoup((R/'index.html').read_text(),'html.parser')
checks=[]
def check(msg,ok):
 checks.append((msg,bool(ok)))
 if not ok: print('FAIL:',msg)
notes=list((R/'raw/external').glob('S*.md')); check('至少五篇已攝取外部資料',len(notes)>=5 and all('攝取筆記' in x.read_text() for x in notes))
wiki=[f for f in (R/'wiki').glob('*.md') if f.stem not in ('index','sources')]
check('11 個概念頁對應 11 張內容投影片',len(wiki)==len(html.select('[data-wiki]'))==11)
check('總頁數 14',len(html.select('.slide'))==14)
for f in wiki:
 t=f.read_text(); lines=re.split(r'^## (.+)\n',t,flags=re.M); fields={lines[i]:lines[i+1].strip() for i in range(1,len(lines),2)}
 s=html.select_one(f'[data-wiki="{f.stem}"]'); check(f'{f.stem}：四個教學欄位與 Wiki 完全一致',all(s.select_one(f'[data-field="{k}"]').get_text()==fields[k] for k in ('基本概念','艾莉實作','資料流程','限制')))
 check(f'{f.stem}：來源 ID 一致且可追溯',set(re.findall(r'\[(\w+)\]',fields['來源']))=={a['data-source'] for a in s.select('[data-source]')} and all((f.parent/x).exists() for x in re.findall(r'\]\(([^)]+)\)',fields['來源'])))
# 建立本次即將覆寫的報告，避免檢查文件連結時報告還不存在。
report_path=R/'logs/static-check.md'
if not report_path.exists(): report_path.write_text('# 靜態驗證（執行中）\n',encoding='utf-8')
broken=[]
for f in R.rglob('*.md'):
 for href in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if not href.startswith(('http:','https:','#')) and not (f.parent/href.split('#')[0]).exists(): broken.append(f'{f.name}: {href}')
for a in html.select('a[href]'):
 h=a['href'];
 if not h.startswith(('http:','https:','#')) and not (R/h).exists(): broken.append(h)
check(f'所有本地 Markdown／HTML 連結（失效：{broken}）',not broken)
check('全部來源收錄於簡報',len(html.select('details[id^="source-"]'))==16)
check('正確保留預寫台詞與數字辨識限制', '未找到 LLM API' in (R/'wiki/dialogue.md').read_text() and '預設關閉' in (R/'wiki/progress.md').read_text() and 'PARTIAL' in (R/'wiki/progress.md').read_text())
check('未打包原始專案、憑證或私人設定檔',not any(f.name in ('.env','settings.json','lines.json','token.json') or f.suffix in ('.pem','.key','.png','.gif') for f in R.rglob('*')))
report='\n'.join(f'- {"PASS" if ok else "FAIL"} — {m}' for m,ok in checks)
(R/'logs/static-check.md').write_text(f'# 靜態驗證\n\n{sum(ok for _,ok in checks)} / {len(checks)} 項通過。\n\n'+report+'\n',encoding='utf-8')
print(f'{sum(ok for _,ok in checks)}/{len(checks)} passed'); assert all(ok for _,ok in checks)
