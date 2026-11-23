from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
S=[
('S01','Qt for Python — QWidget','https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html','Creating Translucent Windows','視窗在支援合成的環境可透過 WA_TranslucentBackground 保留透明區域；Windows 另需 FramelessWindowHint。這是桌寵沒有一般視窗邊框的技術基礎。'),
('S02','Qt for Python — QTimer','https://doc.qt.io/qtforpython-6/PySide6/QtCore/QTimer.html','Detailed Description / Accuracy','QTimer 在事件迴圈中發出 timeout 訊號，可連續觸發或只觸發一次；系統忙碌可能延遲事件，因此計時器不保證精準幀率。'),
('S03','Microsoft Learn — Screen capture','https://learn.microsoft.com/en-us/windows/apps/develop/media-authoring-processing/screen-capture','Screen capture / Check for screen capture support','Windows.Graphics.Capture 可取得顯示器或應用視窗的畫格；應確認裝置支援，且擷取須有清楚的使用者控制。'),
('S04','OpenCV — Template Matching','https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html','Theory / Template Matching in OpenCV','模板在較大影像上滑動並比較局部區域；matchTemplate 產生分數圖，minMaxLoc 找最佳位置。SQDIFF 以較小分數為佳，其他常見相關性方法以較大分數為佳。'),
('S05','aiohttp — Web Server Quickstart','https://docs.aiohttp.org/en/stable/web_quickstart.html','Run a Simple Web Server / WebSockets','HTTP 路由把請求交给 coroutine handler；WebSocketResponse 建立持續連線，伺服器與用戶端可以傳送訊息，而不用每次重新發起 HTTP 請求。'),
('S06','MDN — Push API','https://developer.mozilla.org/en-US/docs/Web/API/Push_API','Push concepts and usage','網頁在非前景甚至未載入時也可經 Push 接收訊息。Service worker 處理 push 事件；訂閱由 endpoint 與加密資訊組成，須保護訂閱資訊。實際送達受平台及網路影響。')]
P=[
('P01','版本與依賴','release_manifest.json；requirements.txt；README.md；docs/v2_4c_release_notes.md','manifest 版本 2.4c；依賴 PySide6、NumPy、OpenCV、aiohttp。README 開頭仍記錄工程候選／未合併；release notes Finalization decision 記錄後續授權合併並保留已知限制。完整實機聯合驗收仍 PARTIAL。'),
('P02','視窗與動畫','pet_window.py:136–180, 383–405；421–498 函式索引','PetWindow 使用無框、透明、可置頂 QWidget 及 QLabel；QTimer 接 next_frame；縮放後保留腳底位置；frame_index 依長度取餘數；static_first、sequence_loop 和 QMovie 分流。'),
('P03','桌面物理','desktop_engine.py:55–102, 149–238 函式索引；242–285','physics_tick 增加 vy 並限制最大速度；以舊腳底和新腳底跨越視窗頂面判斷接觸；達地板時停止下落並 clamp_position。另有相鄰螢幕與視窗附著方法。'),
('P04','自主行為及動畫閘門','behavior_engine.py:12–19, 86–183；animation_state_machine.py:14–91','六個隱藏數值；時間、夜晚、閒置及模式調整數值；sleepiness≥82 或 energy≤16 回傳 sleep，其他分支使用 random.choices。動畫 gate 有優先權、鎖定期限、冷卻及強制中斷。'),
('P05','環境感知','application_watcher.py:12–24, 28–97 函式索引；README v2.0a、v2.0b、v2.0c.1、v2.0d','唯讀 Windows 前景視窗 metadata；profile 分類、防抖；畫面擷取採前景與 profile gate、RAM-only。二重螺旋 WGC，GDI 不可靠時不降級為錯誤影像。'),
('P06','辨識與時間穩定','recognition/engine.py:43–73；recognition/detectors/template.py:105–138；recognition/temporal.py:51–89','每 label 計算 ROI 並取 detector evidence，SceneResolver 合成場景；HSV 模板使用 CCOEFF_NORMED，另一分支 SQDIFF_NORMED 轉 1−raw；分數裁切 0–1 並比較 threshold。TemporalSceneTracker 處理舊時間、缺失與進出穩定狀態。'),
('P07','連戰進度','game_modules/dna_auto_run_monitor.py:21–32 函式與類別摘要；docs/v2_4c_release_notes.md；README v2.3b','唯一進度監控；依場景與事件判斷連戰；中間輪次不 Push。數字候選需三張新畫面一致，僅扼守 current 預設關閉，無已確認 total；驅離能力保持關閉。'),
('P08','角色台詞與反應','dialogue_selector.py:101–139；reaction_policy.py:46–122 函式索引及預設；README v2.2a/v2.2b','320 條預先編寫台詞；依 pool、rarity、tone 篩選，近期歷史與冷卻防重複，random.choices 選句；無適用句可保持安靜。反應政策可控制說話／動作／沉默。沒有證據表明此版本呼叫 LLM API。'),
('P09','事件與手機連動','companion_link.py:14–19, 204–307 函式索引；mobile_link_service.py:148–183, 280–336；README v2.1a/v2.1b/v2.1c','CompanionEventBus 提供語意快照與有界歷史，排除影像、視窗標題等私人欄位；手機 WebSocket 驗證後接快照，非 ping 指令禁止；私人網路、配對 token、限流；選擇性 Web Push。'),
('P10','設定與資料安全','config_manager.py:9–25, 181–242；README v1.9.5.2；release_manifest.json','預設設定與本地 JSON 深度合併，壞檔備份，暫存檔替換；清除舊 gaze 設定。手機／遠端／推播預設關閉。舊視線資產保留不代表功能仍啟用。')]
# All notes are paraphrases based on source reading, not mirrored original documents.
for id,title,url,section,note in S:
 (R/'raw/external'/f'{id}.md').write_text(f'# {id}｜{title}\n\n來源：{url}\n\n讀取日期：2026-11-23\n\n閱讀範圍：{section}\n\n## 攝取筆記（中文轉述）\n{note}\n',encoding='utf-8')
for id,title,loc,note in P:
 (R/'raw/elysia'/f'{id}.md').write_text(f'# {id}｜{title}\n\n版本：v2.4c / main / 7eb19a8f900c2ce482581aff0f5c1dbf38e3c232\n\n定位：{loc}\n\n## 唯讀證據摘要\n{note}\n\n此筆記只公開技術摘要；不含原始碼、私有資產或設定值中的私人資訊。\n',encoding='utf-8')
# Each concept synthesizes source notes; teaching content is also the slide input.
K=[
('overview','專案全貌','桌寵是一個桌面上的互動程式，不只是 GIF。','先認識三層：角色呈現、感知與決策、事件輸出。','艾莉使用 PySide6 顯示角色，以規則引擎決定行為、OpenCV 分析遊戲局部畫面，並用 aiohttp 把語意狀態送到手機。','輸入 → 感知 → 決策 → 動畫／台詞／手機','v2.4c 是本作業的固定版本；未驗證功能不當作已完成。','P01',['S01','S04','S05'],['animation','behavior','vision','mobile']),
('animation','透明視窗與逐幀動畫','如何讓角色像是直接站在桌面？','Sprite 是一張角色圖；Frame 是動畫中的一幀；定時顯示多張圖形成動作。','PetWindow 設定無框透明視窗，QLabel 顯示 QPixmap；QTimer 觸發 next_frame，利用取餘數循環播放。另有 GIF 動作與固定幀序列。','素材 → 定時器 → 下一幀 → QLabel','靜態優先設定可能停止待機逐幀更新；定時器不保證精準 FPS。','P02',['S01','S02'],['physics','fsm']),
('physics','桌面座標與輕量物理','如何讓角色跳起、落地或站在視窗上？','螢幕 y 向下增加；每個 tick 更新垂直速度，腳底跨越平台就落地。','DesktopEngine.physics_tick 用 vy = min(vy + gravity, terminal)，預測新腳底位置，確認平台接觸或地板，再限制位置；支援視窗附著和多螢幕。','速度更新 → 預測位置 → 平台判定 → 落地','這是輕量 2D 幾何，不是通用物理引擎；特殊視窗可能不適用。','P03',['S02'],['animation','behavior']),
('behavior','自主行為與加權決策','如何讓艾莉不必等待指令也會自己行動？','規則決定必要行為，權重決定其他候選行為的相對機率。','BehaviorEngine 維護 mood、energy、curiosity、boredom、attention、sleepiness；夜晚與閒置會更新狀態。睡意 ≥82 或精力 ≤16 優先睡覺，其他情境以加權抽樣選動作。','時間／使用者活動 → 隱藏狀態 → 規則及加權 → 動作','這是規則式決策，不是情緒感知模型或強化學習；權重不等於真實情緒。','P04',['S02'],['fsm','dialogue']),
('fsm','有限狀態機與動畫優先權','如果正在閱讀，使用者突然拖曳她呢？','FSM 保存當前狀態；優先權、鎖定時間與冷卻用來限制狀態轉換。','AnimationStateMachine.can_start 檢查 cooldown 與 locked_until；預設 idle=0、reading=10、dragging=100、falling=90；高優先權可打斷低優先權。','請求動作 → 檢查冷卻與 priority → 切換／拒絕','同優先權也可能通過；此處不宣稱有固定的完整轉移表。','P04',['S02'],['behavior','animation']),
('awareness','應用程式感知','艾莉怎麼知道使用者正在做什麼？','前景程式的名稱及視窗資訊可被分類成使用情境，並不等於理解使用者心思。','ApplicationWatcher 取得 Windows 前景 metadata，profile 分類，防抖避免快速切換造成反覆觸發；前景與允許的 profile 是畫面擷取入口。','前景視窗 → Profile → 穩定情境 → 感知事件','普通應用並非一律截圖；畫面擷取受 profile gate 限制，記憶體內處理。','P05',['S03'],['vision','dialogue']),
('vision','電腦視覺：ROI 與模板比對','艾莉怎麼知道遊戲畫面出現結算？','ROI（感興趣區域）縮小搜尋範圍；模板比對找相似圖樣；閾值決定是否接受。','RecognitionEngine 針對 label 呼叫 detector，TemplateDetector 在 ROI 內比對多個尺度；HSV 使用 CCOEFF_NORMED，SQDIFF_NORMED 則轉為 1−raw，最後與閾值比較。','WGC 畫格 → ROI → 比對分數 → 場景證據','分數不是校準後的機率；遮擋、縮放、畫質或未知畫面可能辨識失敗。','P06',['S03','S04'],['awareness','progress']),
('progress','穩定辨識與遊戲進度','一張畫面就能確認真正完成嗎？','時序確認（Temporal confirmation）需要連續且新鮮的證據；UNKNOWN 是安全的不確定結果。','TemporalSceneTracker 使用進出穩定判定；DNAAutoRunMonitor 是唯一進度來源，避免中途每輪誤推播。v2.4c 數字候選需三張新畫面一致並核對生命週期。','場景證據 → 時序確認 → 連戰語意 → 進度','數字功能預設關閉；扼守只讀 current、total 無確認；驅離能力仍關閉，完整實機驗收 PARTIAL。','P07',['S04'],['vision','mobile']),
('dialogue','角色台詞與互動反應','她說話時一定使用生成式 AI 嗎？','預寫台詞可依分類、語氣、稀有度與冷卻選擇；和 LLM 生成新文字是兩種技術。','DialogueSelector 在 320 條台詞中依 pool 篩選及加權，排除近期句子與冷卻中句子，必要時按規則放寬；ReactionPolicy 可決定台詞、動作或沉默。','情境事件 → 反應政策 → 候選台詞 → 加權選擇','v2.4c 未找到 LLM API 實作證據；本作業的 LLM 用於 Wiki，而非桌寵即時語言生成。','P08',[],['behavior','awareness','mobile']),
('mobile','手機連動、事件與推播','如何離開電腦後仍得知遊戲結束？','事件匯流排解耦生產與消費；HTTP 取快照，WebSocket 傳即時狀態，Web Push 可離線通知。','CompanionEventBus 組合語意事件，MobileLinkService 驗證配對後傳快照及更新；PWA 可透過 Service Worker 接收推播，依規則只通知重要結果。','遊戲事件 → Event Bus → HTTP／WebSocket／Push → 手機','手機狀態唯讀；私人網路、權杖、限流；非所有情境或手機都已完成驗收，也不保證送達。','P09',['S05','S06'],['progress','settings']),
('settings','設定、隱私與版本限制','功能越多，怎麼避免資料外洩及錯誤？','預設關閉高風險／敏感功能，設定更新時保留未知狀態，不硬猜。','ConfigManager 對 JSON 深度合併並以暫存檔替換；壞檔備份。手機、遠端及推播預設關閉；僅分享語意，畫面不寫入磁碟。','讀設定 → 合併預設 → 驗證／備份 → 儲存','頭部視線跟隨已移除，舊素材僅備份；LLM／手勢／語音／空中手寫不列為此版已完成。','P10',['S03','S05','S06'],['awareness','mobile','overview'])]
for slug,title,question,concept,impl,flow,limit,p,ss,rels in K:
 ids=[p]+ss
 if slug=='progress':ids+=['P06']
 if slug=='settings':ids+=['P05','P09','P01']
 if slug=='overview':ids+=['P02','P04','P06','P09']
 sources=' '.join(f'[{i}](../raw/{"external" if i.startswith("S") else "elysia"}/{i}.md)' for i in ids)
 related='、'.join(f'[{i}]({i}.md)' for i in rels)
 text=f'# {title}\n\n## 問題\n{question}\n\n## 基本概念\n{concept}\n\n## 艾莉實作\n{impl}\n\n## 資料流程\n{flow}\n\n## 限制\n{limit}\n\n## 來源\n{sources}\n\n## 相關知識\n{related}\n'
 (R/'wiki'/f'{slug}.md').write_text(text,encoding='utf-8')
(R/'wiki/index.md').write_text('# Elysia LLM Wiki｜知識索引\n\n固定版本 v2.4c；按初學者順序閱讀。\n\n'+'\n'.join(f'- [{k[1]}]({k[0]}.md) — {k[2]}' for k in K)+'\n\n[來源索引](sources.md) · [工作流程](../workflow.md) · [教學簡報](../index.html)\n',encoding='utf-8')
(R/'wiki/sources.md').write_text('# 來源索引\n\n## 外部文件（6 篇）\n'+'\n'.join(f'- [{s[0]}](../raw/external/{s[0]}.md) — [{s[1]}]({s[2]})' for s in S)+'\n\n## 專案資料（10 組）\n'+'\n'.join(f'- [{p[0]}](../raw/elysia/{p[0]}.md) — {p[1]}：{p[2]}' for p in P)+'\n',encoding='utf-8')
(R/'logs/ingest.md').write_text('# Ingest 執行紀錄｜2026-11-23\n\n實際透過 GitHub 授權唯讀檢視 main 固定 commit 7eb19a8f900c2ce482581aff0f5c1dbf38e3c232；讀取檔案樹、版本與依賴、原始碼及發行紀錄。透過網頁閱讀六篇外部官方文件，再由 LLM 轉述為來源筆記並整合成 11 個概念頁。未下載或公開私有程式。\n\n| ID | 內容 | 狀態 | 對應 Wiki |\n|---|---|---|---|\n'+'\n'.join(f'| {s[0]} | {s[1]} | 已讀取並攝取 | '+ '、'.join(k[0] for k in K if s[0] in k[8])+' |' for s in S)+'\n'+'\n'.join(f'| {p[0]} | {p[1]} | 已讀取並摘要 | '+ '、'.join(k[0] for k in K if p[0] == k[7] or (p[0] in ["P01","P02","P04","P06","P09"] and k[0]=="overview"))+' |' for p in P)+'\n\n註：來源筆記為自行轉述，不是原文鏡像；未成功取得的 State pattern 網頁未算入六篇。\n',encoding='utf-8')
