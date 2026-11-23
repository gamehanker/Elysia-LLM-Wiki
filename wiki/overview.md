# 專案全貌

## 問題
桌寵是一個桌面上的互動程式，不只是 GIF。

## 基本概念
先認識三層：角色呈現、感知與決策、事件輸出。

## 艾莉實作
艾莉使用 PySide6 顯示角色，以規則引擎決定行為、OpenCV 分析遊戲局部畫面，並用 aiohttp 把語意狀態送到手機。

## 資料流程
輸入 → 感知 → 決策 → 動畫／台詞／手機

## 限制
v2.4c 是本作業的固定版本；未驗證功能不當作已完成。

## 來源
[P01](../raw/elysia/P01.md) [S01](../raw/external/S01.md) [S04](../raw/external/S04.md) [S05](../raw/external/S05.md) [P02](../raw/elysia/P02.md) [P04](../raw/elysia/P04.md) [P06](../raw/elysia/P06.md) [P09](../raw/elysia/P09.md)

## 相關知識
[animation](animation.md)、[behavior](behavior.md)、[vision](vision.md)、[mobile](mobile.md)
