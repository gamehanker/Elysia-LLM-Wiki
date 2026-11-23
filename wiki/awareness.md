# 應用程式感知

## 問題
艾莉怎麼知道使用者正在做什麼？

## 基本概念
前景程式的名稱及視窗資訊可被分類成使用情境，並不等於理解使用者心思。

## 艾莉實作
ApplicationWatcher 取得 Windows 前景 metadata，profile 分類，防抖避免快速切換造成反覆觸發；前景與允許的 profile 是畫面擷取入口。

## 資料流程
前景視窗 → Profile → 穩定情境 → 感知事件

## 限制
普通應用並非一律截圖；畫面擷取受 profile gate 限制，記憶體內處理。

## 來源
[P05](../raw/elysia/P05.md) [S03](../raw/external/S03.md)

## 相關知識
[vision](vision.md)、[dialogue](dialogue.md)
