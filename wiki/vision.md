# 電腦視覺：ROI 與模板比對

## 問題
艾莉怎麼知道遊戲畫面出現結算？

## 基本概念
ROI（感興趣區域）縮小搜尋範圍；模板比對找相似圖樣；閾值決定是否接受。

## 艾莉實作
RecognitionEngine 針對 label 呼叫 detector，TemplateDetector 在 ROI 內比對多個尺度；HSV 使用 CCOEFF_NORMED，SQDIFF_NORMED 則轉為 1−raw，最後與閾值比較。

## 資料流程
WGC 畫格 → ROI → 比對分數 → 場景證據

## 限制
分數不是校準後的機率；遮擋、縮放、畫質或未知畫面可能辨識失敗。

## 來源
[P06](../raw/elysia/P06.md) [S03](../raw/external/S03.md) [S04](../raw/external/S04.md)

## 相關知識
[awareness](awareness.md)、[progress](progress.md)
