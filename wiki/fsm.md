# 有限狀態機與動畫優先權

## 問題
如果正在閱讀，使用者突然拖曳她呢？

## 基本概念
FSM 保存當前狀態；優先權、鎖定時間與冷卻用來限制狀態轉換。

## 艾莉實作
AnimationStateMachine.can_start 檢查 cooldown 與 locked_until；預設 idle=0、reading=10、dragging=100、falling=90；高優先權可打斷低優先權。

## 資料流程
請求動作 → 檢查冷卻與 priority → 切換／拒絕

## 限制
同優先權也可能通過；此處不宣稱有固定的完整轉移表。

## 來源
[P04](../raw/elysia/P04.md) [S02](../raw/external/S02.md)

## 相關知識
[behavior](behavior.md)、[animation](animation.md)
