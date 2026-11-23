# Elysia LLM Wiki

從零認識 AI 桌面寵物：以 Elysia Desktop Pet v2.4c 為例。

第十週作業：以 LLM 讀取外部官方文件及固定版本的專案證據，製作持續可更新的技術知識庫與初學者 HTML 簡報。艾莉本體於本版的決策以規則、加權與傳統電腦視覺為主；不宣稱已整合生成式 AI 即時對話。

**入口：** [HTML 教學簡報](index.html) ｜ [Wiki 知識索引](wiki/index.md) ｜ [來源索引](wiki/sources.md) ｜ [工作流程](workflow.md) ｜ [Ingest 紀錄](logs/ingest.md) ｜ [驗證紀錄](logs/validation.md) ｜ [反思](reflection.md)

### 本機使用
解壓全部檔案後開啟 index.html，不需安裝或連線。方向鍵、頁碼下拉選單或底部按鈕切換。HTML 是教學示意，不會操作攝影機、桌寵或遊戲。

### 維護
先依 AGENTS.md 攝取新資料、更新 Wiki，執行 `python tools/build.py` 重新編譯，再執行 `python tools/validate.py`。`tools/ingest.py` 保存本次 LLM 整理的資料及重建方法（重新執行會覆寫初始頁面，更新後勿直接執行）。可選安裝 playwright、bs4 執行實際瀏覽測試 `python tools/browser_test.py`，需要 Chromium。

### 發布
建立與正式桌寵不同的 GitHub repository，上傳本資料夾內全部檔案；Settings → Pages → Deploy from a branch → main / (root)。確認 Pages 可公開開啟。原始私人 repository 保持不變。若不公開，亦可將完整成果交老師檢查。
