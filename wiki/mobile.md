# 手機連動、事件與推播

## 問題
如何離開電腦後仍得知遊戲結束？

## 基本概念
事件匯流排解耦生產與消費；HTTP 取快照，WebSocket 傳即時狀態，Web Push 可離線通知。

## 艾莉實作
CompanionEventBus 組合語意事件，MobileLinkService 驗證配對後傳快照及更新；PWA 可透過 Service Worker 接收推播，依規則只通知重要結果。

## 資料流程
遊戲事件 → Event Bus → HTTP／WebSocket／Push → 手機

## 限制
手機狀態唯讀；私人網路、權杖、限流；非所有情境或手機都已完成驗收，也不保證送達。

## 來源
[P09](../raw/elysia/P09.md) [S05](../raw/external/S05.md) [S06](../raw/external/S06.md)

## 相關知識
[progress](progress.md)、[settings](settings.md)
