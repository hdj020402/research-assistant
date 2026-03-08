---
title: "LCMS-Net: Deep Learning for Raw High Resolution Mass Spectrometry Data Applied to Forensic Cause-of-Death Screening"
title_zh: "LCMS-Net：用于法医死因筛查的深度学习应用于原始高分辨质谱数据"
journal: "Analytical Chemistry"
doi: "10.1021/acs.analchem.5c05404"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6m9dwOKKpz9-2BWBhH0scpkFR-2FLdRmnp1EN72-2FuAv6IsmXIm4wlUYrFi1T24AoFa-2BUZiQcMnShNvZpyk0NCvxJb-2FZbgyoK-2FHZG20pq6BBAYCQZsMu-2Fog-2Fl5IFwgGboMaBCGevkvKDWPw72LP7xAVYstBpJFX_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjGwpEj2H7owzqYEdyo186pK6iN5aTK8WBkO-2Ff68T8E23n3guZj3Aau3RJf6gbbSl1F56sP11XMpENF4v8ix7WxVqL2rk0uw01XdT1baQ97ueuVXBiZ-2BpM5U1xx0-2FtTV5KRoHyKHbo18nhSH25wCCaNl9G-2BtwVJEWThCDCpKvZoJ998t84UoANSR4X4mRAz1O4vlEwNr9hXoRR-2FzUpfNY2j1vFoHBy63MZeuaOFT8tDZc-3D"
pub_date: ""
tags: ["deep-learning", "mass-spectrometry", "metabolomics", "forensic-analysis", "end-to-end-learning"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# LCMS-Net: Deep Learning for Raw High Resolution Mass Spectrometry Data Applied to Forensic Cause-of-Death Screening

**LCMS-Net：用于法医死因筛查的深度学习应用于原始高分辨质谱数据**

## 精华总结
LCMS-Net通过直接处理原始LC-HRMS数据并显式建模其空间特性，消除手动数据预处理的需要，使工作流更快速高效。

**关键词**: 深度学习、质谱分析、代谢组学、死因筛查、批次效应

## 摘要（英文）
Current preprocessing workflows for untargeted metabolomics using liquid chromatography-high resolution mass spectrometry (LC-HRMS) are time-consuming and require significant domain knowledge. Furthermore, they lack reproducibility or may fail to detect some metabolites entirely. We introduce LCMS-Net, an end-to-end deep learning model for the analysis of LC-HRMS data, to address these challenges. LCMS-Net mitigates the need for manual data preprocessing by operating directly on the raw LC-HRMS data and explicitly modeling its spatial properties. The effectiveness of this fully automated workflow is shown through two case-studies, cause-of-death (CoD) screening and colon cancer detection. For the cause-of-death screening task, LCMS-Net achieved a 9% improvement in F1-score compared to the previous state-of-the-art model (OPLS-DA). For the colon cancer detection task, LCMS-Net achieved an F1-score improvement of 1.8% compared to the previous state-of-the-art model (DeepMSProfiler). Furthermore, LCMS-Net significantly reduces batch effects that are a common source of bias in metabolomics data analyses. This was shown by using a training and test set from different measurement instruments, where the performance only differed by at most 3% as to using data from the same instrument. Compared to other end-to-end deep learning methods for LC-HRMS data, LCMS-Net is also structurally simpler and does not rely on pretraining, which makes it faster and computationally more efficient.

## 摘要（中文）
液相色谱-高分辨质谱法(LC-HRMS)的非靶向代谢组学预处理工作流耗时且需要专业知识。本研究提出LCMS-Net，一个端到端的深度学习模型，直接作用于原始LC-HRMS数据，显式建模其空间特性，无需手动预处理。在死因筛查和结肠癌检测任务中，该模型相比现有方法F1-score分别提升9%和1.8%，同时显著降低批次效应，在不同仪器间的性能差异仅为3%。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6m9dwOKKpz9-2BWBhH0scpkFR-2FLdRmnp1EN72-2FuAv6IsmXIm4wlUYrFi1T24AoFa-2BUZiQcMnShNvZpyk0NCvxJb-2FZbgyoK-2FHZG20pq6BBAYCQZsMu-2Fog-2Fl5IFwgGboMaBCGevkvKDWPw72LP7xAVYstBpJFX_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjGwpEj2H7owzqYEdyo186pK6iN5aTK8WBkO-2Ff68T8E23n3guZj3Aau3RJf6gbbSl1F56sP11XMpENF4v8ix7WxVqL2rk0uw01XdT1baQ97ueuVXBiZ-2BpM5U1xx0-2FtTV5KRoHyKHbo18nhSH25wCCaNl9G-2BtwVJEWThCDCpKvZoJ998t84UoANSR4X4mRAz1O4vlEwNr9hXoRR-2FzUpfNY2j1vFoHBy63MZeuaOFT8tDZc-3D)
