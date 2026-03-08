---
title: "LCMS-Net: Deep Learning for Raw High Resolution Mass Spectrometry Data Applied to Forensic Cause-of-Death Screening"
title_zh: "LCMS-Net：用于法医死因检测的原始高分辨质谱数据深度学习分析"
journal: "Analytical Chemistry"
doi: "10.1021/acs.analchem.5c05404"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6m9dwOKKpz9-2BWBhH0scpkFR-2FLdRmnp1EN72-2FuAv6IsmXIm4wlUYrFi1T24AoFa-2BUZiQcMnShNvZpyk0NCvxJb-2FZbgyoK-2FHZG20pq6BBAYCQZsMu-2Fog-2Fl5IFwgGboMaBCGevkvKDWPw72LP7xAVYstBpJFX_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjGwpEj2H7owzqYEdyo186pK6iN5aTK8WBkO-2Ff68T8E23n3guZj3Aau3RJf6gbbSl1F56sP11XMpENF4v8ix7WxVqL2rk0uw01XdT1baQ97ueuVXBiZ-2BpM5U1xx0-2FtTV5KRoHyKHbo18nhSH25wCCaNl9G-2BtwVJEWThCDCpKvZoJ998t84UoANSR4X4mRAz1O4vlEwNr9hXoRR-2FzUpfNY2j1vFoHBy63MZeuaOFT8tDZc-3D"
pub_date: ""
tags: ["deep-learning", "mass-spectrometry", "metabolomics", "analytical-chemistry", "medical-diagnostics"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# LCMS-Net: Deep Learning for Raw High Resolution Mass Spectrometry Data Applied to Forensic Cause-of-Death Screening

**LCMS-Net：用于法医死因检测的原始高分辨质谱数据深度学习分析**

## 精华总结
LCMS-Net通过直接操作原始LC-HRMS数据并显式建模其空间特性，消除了对手动数据预处理的需求，使其在计算速度和效率方面更优。

**关键词**: 深度学习、液相色谱-高分辨质谱、代谢组学、死因检测、端到端学习

## 摘要（英文）
Current preprocessing workflows for untargeted metabolomics using liquid chromatography-high resolution mass spectrometry (LC-HRMS) are time-consuming and require significant domain knowledge. Furthermore, they lack reproducibility or may fail to detect some metabolites entirely. We introduce LCMS-Net, an end-to-end deep learning model for the analysis of LC-HRMS data, to address these challenges. LCMS-Net mitigates the need for manual data preprocessing by operating directly on the raw LC-HRMS data and explicitly modeling its spatial properties. The effectiveness of this fully automated workflow is shown through two case-studies, cause-of-death (CoD) screening and colon cancer detection. For the cause-of-death screening task, LCMS-Net achieved a 9% improvement in F1-score compared to the previous state-of-the-art model (OPLS-DA). For the colon cancer detection task, LCMS-Net achieved an F1-score improvement of 1.8% compared to the previous state-of-the-art model (DeepMSProfiler). Furthermore, LCMS-Net significantly reduces batch effects that are a common source of bias in metabolomics data analyses. This was shown by using a training and test set from different measurement instruments, where the performance only differed by at most 3% as to using data from the same instrument. Compared to other end-to-end deep learning methods for LC-HRMS data, LCMS-Net is also structurally simpler and does not rely on pretraining, which makes it faster and computationally more efficient.

## 摘要（中文）
当前使用液相色谱-高分辨质谱法(LC-HRMS)进行非靶向代谢组学分析的预处理工作流程耗时冗长，需要大量的领域知识。此外，这些方法的重现性差，可能无法完全检测某些代谢物。我们引入LCMS-Net，一个用于LC-HRMS数据分析的端到端深度学习模型，以解决这些挑战。LCMS-Net通过直接操作原始LC-HRMS数据并显式建模其空间特性，减轻了对手动数据预处理的需求。该全自动工作流程的有效性通过两个案例研究得到展示：死因(CoD)筛选和结肠癌检测。对于死因筛选任务，LCMS-Net相比之前的最先进模型(OPLS-DA)在F1分数上提高了9%。对于结肠癌检测任务，LCMS-Net相比之前的最先进模型(DeepMSProfiler)在F1分数上提高了1.8%。此外，LCMS-Net显著降低了代谢组学数据分析中常见的批次效应偏差。使用来自不同测量仪器的训练集和测试集时，性能差异仅为3%以内，这证明了该方法的有效性。与其他用于LC-HRMS数据的端到端深度学习方法相比，LCMS-Net在结构上更简洁，不依赖于预训练，使其更快且计算效率更高。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6m9dwOKKpz9-2BWBhH0scpkFR-2FLdRmnp1EN72-2FuAv6IsmXIm4wlUYrFi1T24AoFa-2BUZiQcMnShNvZpyk0NCvxJb-2FZbgyoK-2FHZG20pq6BBAYCQZsMu-2Fog-2Fl5IFwgGboMaBCGevkvKDWPw72LP7xAVYstBpJFX_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjGwpEj2H7owzqYEdyo186pK6iN5aTK8WBkO-2Ff68T8E23n3guZj3Aau3RJf6gbbSl1F56sP11XMpENF4v8ix7WxVqL2rk0uw01XdT1baQ97ueuVXBiZ-2BpM5U1xx0-2FtTV5KRoHyKHbo18nhSH25wCCaNl9G-2BtwVJEWThCDCpKvZoJ998t84UoANSR4X4mRAz1O4vlEwNr9hXoRR-2FzUpfNY2j1vFoHBy63MZeuaOFT8tDZc-3D)
