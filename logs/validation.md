# 實際執行與檢查紀錄｜2026-11-23

## 來源閘門（人工 LLM 審查）

| 發現 | 修正 | 再檢查 |
|---|---|---|
| 原規劃包含較新版本 LLM API 與手勢等功能，但 GitHub main 固定 commit 只顯示 v2.4c | 先鎖定版本並讀取依賴、檔案樹、DialogueSelector，將未找到證據的功能排除 | 台詞章節明確區分預寫選句與生成式 AI |
| README 工程候選狀態與後續 release notes 發布決策不同 | 以 manifest 與 release notes 核對版本與狀態，不把歷史文字當最新狀態 | 完整驗收仍標 PARTIAL，數字預設關閉 |
| State Pattern 網頁讀取失敗 | 未編入來源，改用其餘實際讀取的六篇官方文件及原始碼 FSM 證據 | 6 篇外部來源均已攝取 |

這些是實際發現的資料問題；並非故意製造的錯誤。修改後流程於 Ingest 前設置來源／版本閘門。

## 程式檢查

- 第一輪：瀏覽器直接開啟 `file://` 與本機 HTTP 網址被執行環境管理政策阻擋（ERR_BLOCKED_BY_ADMINISTRATOR）。改為 Chromium 直接載入 HTML 字串測試 DOM 與互動，未宣稱已測真實部署。
- 第一輪靜態驗證：28/29 PASS；唯一失效連結為尚未生成的 static-check.md。將報告建立移到連結檢查之前，再執行全套驗證，避免首次執行的次序問題。
- 第二輪：重新驗證連結與教學欄位，結果以下方報告為準。

- [靜態驗證](static-check.md)
- [瀏覽器測試](browser-check.md)

此作業只驗證知識庫與 HTML。沒有在本機重新執行 Windows 桌寵或原專案測試，既有 release notes 的工程測試與實機狀態屬歷史證據，不是本次測試結果。
