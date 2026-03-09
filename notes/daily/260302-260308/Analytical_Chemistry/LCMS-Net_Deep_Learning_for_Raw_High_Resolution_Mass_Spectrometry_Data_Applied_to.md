---
title: "LCMS-Net: Deep Learning for Raw High Resolution Mass Spectrometry Data Applied to Forensic Cause-of-Death Screening"
title_zh: "Lcms-net: 用于法医死因筛查的原始高分辨率质谱数据的深度学习"
journal: "Analytical Chemistry"
doi: "10.1021/acs.analchem.5c05404"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6m9dwOKKpz9-2BWBhH0scpkFR-2FLdRmnp1EN72-2FuAv6IsmXIm4wlUYrFi1T24AoFa-2BUZiQcMnShNvZpyk0NCvxJb-2FZbgyoK-2FHZG20pq6BBAYCQZsMu-2Fog-2Fl5IFwgGboMaBCGevkvKDWPw72LP7xAVYstBpJFX_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjGwpEj2H7owzqYEdyo186pK6iN5aTK8WBkO-2Ff68T8E23n3guZj3Aau3RJf6gbbSl1F56sP11XMpENF4v8ix7WxVqL2rk0uw01XdT1baQ97ueuVXBiZ-2BpM5U1xx0-2FtTV5KRoHyKHbo18nhSH25wCCaNl9G-2BtwVJEWThCDCpKvZoJ998t84UoANSR4X4mRAz1O4vlEwNr9hXoRR-2FzUpfNY2j1vFoHBy63MZeuaOFT8tDZc-3D"
pub_date: ""
tags: ["deep-learning", "mass-spectrometry", "metabolomics", "forensic-toxicology", "automated-preprocessing"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# LCMS-Net: Deep Learning for Raw High Resolution Mass Spectrometry Data Applied to Forensic Cause-of-Death Screening

**Lcms-net: 用于法医死因筛查的原始高分辨率质谱数据的深度学习**

## 精华总结
LCMS-Net通过直接处理原始LC-HRMS数据并显式建模其空间特性，消除了手动数据预处理的需要，使其更快且计算效率更高。

**关键词**: 深度学习、液相色谱-高分辨质谱、代谢组学、法医毒理学、端到端模型

## 摘要（英文）
Current preprocessing workflows for untargeted metabolomics using liquid chromatography-high resolution mass spectrometry (LC-HRMS) are time-consuming and require significant domain knowledge. Furthermore, they lack reproducibility or may fail to detect some metabolites entirely. We introduce LCMS-Net, an end-to-end deep learning model for the analysis of LC-HRMS data, to address these challenges. LCMS-Net mitigates the need for manual data preprocessing by operating directly on the raw LC-HRMS data and explicitly modeling its spatial properties. The effectiveness of this fully automated workflow is shown through two case-studies, cause-of-death (CoD) screening and colon cancer detection. For the cause-of-death screening task, LCMS-Net achieved a 9% improvement in F1-score compared to the previous state-of-the-art model (OPLS-DA). For the colon cancer detection task, LCMS-Net achieved an F1-score improvement of 1.8% compared to the previous state-of-the-art model (DeepMSProfiler). Furthermore, LCMS-Net significantly reduces batch effects that are a common source of bias in metabolomics data analyses. This was shown by using a training and test set from different measurement instruments, where the performance only differed by at most 3% as to using data from the same instrument. Compared to other end-to-end deep learning methods for LC-HRMS data, LCMS-Net is also structurally simpler and does not rely on pretraining, which makes it faster and computationally more efficient.

## 摘要（中文）
当前使用液相色谱-高分辨率质谱 (lc-hrms) 的非靶向代谢组学的预处理工作流程非常耗时，并且需要大量的领域知识。此外，它们缺乏可重复性或可能无法完全检测某些代谢物。我们引入lcms-net，这是一种用于分析lc-hrms数据的端到端深度学习模型，以解决这些挑战。Lcms-net通过直接对原始lc-hrms数据进行操作并对其空间属性进行显式建模，从而减轻了对手动数据预处理的需求。通过两个案例研究，死亡原因 (CoD) 筛查和结肠癌检测显示了这种全自动工作流程的有效性。对于死因筛查任务，与以前的最新模型 (opls-da) 相比，lcms-net在F1-score方面取得了9% 的进步。对于结肠癌检测任务，lcms-net与以前的最新模型 (DeepMSProfiler) 相比，F1-score提高了1.8%。此外，lcms-net显着降低了批次效应，这是代谢组学数据分析中常见的偏倚来源。这通过使用来自不同测量仪器的训练和测试一下集来显示，其中性能仅与使用来自相同仪器的数据相差至多3%。与lc-hrms数据的其他端到端深度学习方法相比，lcms-net在结构上也更简单，并且不依赖于预训练，这使其速度更快，计算效率更高。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6m9dwOKKpz9-2BWBhH0scpkFR-2FLdRmnp1EN72-2FuAv6IsmXIm4wlUYrFi1T24AoFa-2BUZiQcMnShNvZpyk0NCvxJb-2FZbgyoK-2FHZG20pq6BBAYCQZsMu-2Fog-2Fl5IFwgGboMaBCGevkvKDWPw72LP7xAVYstBpJFX_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjGwpEj2H7owzqYEdyo186pK6iN5aTK8WBkO-2Ff68T8E23n3guZj3Aau3RJf6gbbSl1F56sP11XMpENF4v8ix7WxVqL2rk0uw01XdT1baQ97ueuVXBiZ-2BpM5U1xx0-2FtTV5KRoHyKHbo18nhSH25wCCaNl9G-2BtwVJEWThCDCpKvZoJ998t84UoANSR4X4mRAz1O4vlEwNr9hXoRR-2FzUpfNY2j1vFoHBy63MZeuaOFT8tDZc-3D)
