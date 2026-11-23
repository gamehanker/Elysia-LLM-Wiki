# 自主行為與加權決策

## 問題
如何讓艾莉不必等待指令也會自己行動？

## 基本概念
規則決定必要行為，權重決定其他候選行為的相對機率。

## 艾莉實作
BehaviorEngine 維護 mood、energy、curiosity、boredom、attention、sleepiness；夜晚與閒置會更新狀態。睡意 ≥82 或精力 ≤16 優先睡覺，其他情境以加權抽樣選動作。

## 資料流程
時間／使用者活動 → 隱藏狀態 → 規則及加權 → 動作

## 限制
這是規則式決策，不是情緒感知模型或強化學習；權重不等於真實情緒。

## 來源
[P04](../raw/elysia/P04.md) [S02](../raw/external/S02.md)

## 相關知識
[fsm](fsm.md)、[dialogue](dialogue.md)
