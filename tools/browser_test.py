from pathlib import Path
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1]; results=[]
def ok(label,cond):
 results.append((label,bool(cond))); assert cond,label
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']); page=b.new_page(viewport={'width':1280,'height':900}); errors=[];page.on('pageerror',lambda exc:errors.append(str(exc)))
 page.set_content((R/"index.html").read_text());ok('首頁載入及 14 頁計數',page.locator('#counter').inner_text()=='1 / 14');page.screenshot(path='/mnt/data/elysia-cover-preview.png');page.locator('#next').click();ok('下一頁',page.locator('#counter').inner_text()=='2 / 14');page.locator('#prev').click();ok('上一頁',page.locator('#counter').inner_text()=='1 / 14');page.locator('body').click(position={'x':5,'y':80});page.keyboard.press('ArrowRight');ok('鍵盤右箭頭',page.locator('#counter').inner_text()=='2 / 14')
 def go(i):page.locator('#chapter').select_option(str(i))
 go(2);page.locator('#frameNext').click();ok('動畫幀切換',page.locator('#frameLabel').inner_text()=='Frame 2 / 4')
 go(3);page.locator('#drop').click();page.wait_for_timeout(1000);ok('物理落地', '停止下落' in page.locator('#physicsStatus').inner_text())
 go(4);page.locator('#energy').evaluate("e=>{e.value=10;e.dispatchEvent(new Event('input'))}");ok('自主行為睡眠門檻', 'sleep' in page.locator('#behaviorResult').inner_text());page.screenshot(path='/mnt/data/elysia-lesson-preview.png')
 go(5);page.locator('#fsmIdle').click();ok('FSM 低優先拒絕','拒絕' in page.locator('#fsmResult').inner_text());page.locator('#fsmDrag').click();ok('FSM 高優先允許','允許' in page.locator('#fsmResult').inner_text())
 go(7);page.locator('#score').evaluate("e=>{e.value=60;e.dispatchEvent(new Event('input'))}");ok('模板示意閾值','未達' in page.locator('#scoreResult').inner_text())
 go(8);[page.locator('#match').click() for _ in range(3)];ok('時序三次確認','示意確認' in page.locator('#progressResult').inner_text());page.locator('#miss').click();ok('不一致時重設','0 / 3' in page.locator('#progressResult').inner_text())
 go(9);page.locator('#chooseLine').click();line=page.locator('#lineResult').inner_text();page.locator('#chooseLine').click();ok('示意台詞防連續重複',line!=page.locator('#lineResult').inner_text())
 go(12);page.locator('.quiz').first.locator('[data-ok="0"]').click();ok('測驗錯誤回饋','再想想' in page.locator('.feedback').first.inner_text());page.locator('.quiz').first.locator('[data-ok="1"]').click();ok('測驗正確回饋','正確' in page.locator('.feedback').first.inner_text())
 go(2);page.locator('.slide.active [data-source="S01"]').click();ok('來源跳轉與展開',page.locator('#counter').inner_text()=='14 / 14' and page.locator('#source-S01').get_attribute('open') is not None)
 for w,h in [(1280,900),(390,844)]:
  page.set_viewport_size({'width':w,'height':h}); fails=[]
  for i in range(14):
   go(i)
   if not page.locator('.slide.active').is_visible() or page.evaluate('document.documentElement.scrollWidth>innerWidth+1'):fails.append(i+1)
  ok(f'{w}×{h} 全 14 頁可導覽且無水平溢出',not fails)
 ok('JavaScript 無未捕捉例外',not errors);b.close()
report='\n'.join(f'- {"PASS" if result else "FAIL"} — {label}' for label,result in results)
(R/'logs/browser-check.md').write_text(f'# Chromium 實際瀏覽測試\n\n{sum(result for _,result in results)} / {len(results)} 項通過。桌面與手機 viewport；沙盒禁止 file:// 與 localhost 導覽，因此使用 Chromium set_content 載入實際 HTML；未測網址部署與檔案導覽。\n\n'+report+'\n',encoding='utf-8');print(f'{len(results)} browser checks passed')
