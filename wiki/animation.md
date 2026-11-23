# 透明視窗與逐幀動畫

## 問題
如何讓角色像是直接站在桌面？

## 基本概念
Sprite 是一張角色圖；Frame 是動畫中的一幀；定時顯示多張圖形成動作。

## 艾莉實作
PetWindow 設定無框透明視窗，QLabel 顯示 QPixmap；QTimer 觸發 next_frame，利用取餘數循環播放。另有 GIF 動作與固定幀序列。

## 資料流程
素材 → 定時器 → 下一幀 → QLabel

## 限制
靜態優先設定可能停止待機逐幀更新；定時器不保證精準 FPS。

## 來源
[P02](../raw/elysia/P02.md) [S01](../raw/external/S01.md) [S02](../raw/external/S02.md)

## 相關知識
[physics](physics.md)、[fsm](fsm.md)
