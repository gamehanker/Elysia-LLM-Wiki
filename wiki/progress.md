# 穩定辨識與遊戲進度

## 問題
一張畫面就能確認真正完成嗎？

## 基本概念
時序確認（Temporal confirmation）需要連續且新鮮的證據；UNKNOWN 是安全的不確定結果。

## 艾莉實作
TemporalSceneTracker 使用進出穩定判定；DNAAutoRunMonitor 是唯一進度來源，避免中途每輪誤推播。v2.4c 數字候選需三張新畫面一致並核對生命週期。

## 資料流程
場景證據 → 時序確認 → 連戰語意 → 進度

## 限制
數字功能預設關閉；扼守只讀 current、total 無確認；驅離能力仍關閉，完整實機驗收 PARTIAL。

## 來源
[P07](../raw/elysia/P07.md) [S04](../raw/external/S04.md) [P06](../raw/elysia/P06.md)

## 相關知識
[vision](vision.md)、[mobile](mobile.md)
