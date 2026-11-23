# 桌面座標與輕量物理

## 問題
如何讓角色跳起、落地或站在視窗上？

## 基本概念
螢幕 y 向下增加；每個 tick 更新垂直速度，腳底跨越平台就落地。

## 艾莉實作
DesktopEngine.physics_tick 用 vy = min(vy + gravity, terminal)，預測新腳底位置，確認平台接觸或地板，再限制位置；支援視窗附著和多螢幕。

## 資料流程
速度更新 → 預測位置 → 平台判定 → 落地

## 限制
這是輕量 2D 幾何，不是通用物理引擎；特殊視窗可能不適用。

## 來源
[P03](../raw/elysia/P03.md) [S02](../raw/external/S02.md)

## 相關知識
[animation](animation.md)、[behavior](behavior.md)
