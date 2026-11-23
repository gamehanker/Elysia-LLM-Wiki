# Chromium 實際瀏覽測試

19 / 19 項通過。桌面與手機 viewport；沙盒禁止 file:// 與 localhost 導覽，因此使用 Chromium set_content 載入實際 HTML；未測網址部署與檔案導覽。

- PASS — 首頁載入及 14 頁計數
- PASS — 下一頁
- PASS — 上一頁
- PASS — 鍵盤右箭頭
- PASS — 動畫幀切換
- PASS — 物理落地
- PASS — 自主行為睡眠門檻
- PASS — FSM 低優先拒絕
- PASS — FSM 高優先允許
- PASS — 模板示意閾值
- PASS — 時序三次確認
- PASS — 不一致時重設
- PASS — 示意台詞防連續重複
- PASS — 測驗錯誤回饋
- PASS — 測驗正確回饋
- PASS — 來源跳轉與展開
- PASS — 1280×900 全 14 頁可導覽且無水平溢出
- PASS — 390×844 全 14 頁可導覽且無水平溢出
- PASS — JavaScript 無未捕捉例外
