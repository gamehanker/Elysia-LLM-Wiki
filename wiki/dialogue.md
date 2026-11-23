# 角色台詞與互動反應

## 問題
她說話時一定使用生成式 AI 嗎？

## 基本概念
預寫台詞可依分類、語氣、稀有度與冷卻選擇；和 LLM 生成新文字是兩種技術。

## 艾莉實作
DialogueSelector 在 320 條台詞中依 pool 篩選及加權，排除近期句子與冷卻中句子，必要時按規則放寬；ReactionPolicy 可決定台詞、動作或沉默。

## 資料流程
情境事件 → 反應政策 → 候選台詞 → 加權選擇

## 限制
v2.4c 未找到 LLM API 實作證據；本作業的 LLM 用於 Wiki，而非桌寵即時語言生成。

## 來源
[P08](../raw/elysia/P08.md)

## 相關知識
[behavior](behavior.md)、[awareness](awareness.md)、[mobile](mobile.md)
