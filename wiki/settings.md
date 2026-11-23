# 設定、隱私與版本限制

## 問題
功能越多，怎麼避免資料外洩及錯誤？

## 基本概念
預設關閉高風險／敏感功能，設定更新時保留未知狀態，不硬猜。

## 艾莉實作
ConfigManager 對 JSON 深度合併並以暫存檔替換；壞檔備份。手機、遠端及推播預設關閉；僅分享語意，畫面不寫入磁碟。

## 資料流程
讀設定 → 合併預設 → 驗證／備份 → 儲存

## 限制
頭部視線跟隨已移除，舊素材僅備份；LLM／手勢／語音／空中手寫不列為此版已完成。

## 來源
[P10](../raw/elysia/P10.md) [S03](../raw/external/S03.md) [S05](../raw/external/S05.md) [S06](../raw/external/S06.md) [P05](../raw/elysia/P05.md) [P09](../raw/elysia/P09.md) [P01](../raw/elysia/P01.md)

## 相關知識
[awareness](awareness.md)、[mobile](mobile.md)、[overview](overview.md)
