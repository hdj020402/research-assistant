---
title: "Toward Generalizable Data-Driven Pharmacokinetics with Interpretable Neural ODEs"
title_zh: "基于可解释神经常微分方程的通用数据驱动药动学模型"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02924"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnP-2BC5LCoOzD71-2BC2MKt2ViF4uoDO93G9iDwzzHJndQYcAYZPw-2FLBwlxDAD9kvbqTnua6v9eGwqtnnacnc2wKTbAqvOlyMCmBBD6J55Mkj-2Bh-2FuHv1S7-2FTugfQhiTVwr1qqPtR2Q_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FCpYzkzyQ8K9Moac7C3kD2SLcLQvkWs9Rc2gKGowY08-2FrQ1g30FCPjVEJF632EiZLf1PTclKN8-2FpCJjZAfzvZcJ-2BTl7t6rzMbYocXUe0nbeAySAcdeSf0ahEPc-2F77k2XgF-2FlhYTzCgvItW5xOLrNt2MvvK-2B-2BBqLhbxo0t9lCgezjj0vaLuG9moHVleOOTJriG4-3D"
pub_date: ""
tags: ["neural-ode", "pharmacokinetics", "drug-modeling", "deep-learning", "precision-medicine"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Toward Generalizable Data-Driven Pharmacokinetics with Interpretable Neural ODEs

**基于可解释神经常微分方程的通用数据驱动药动学模型**

## 精华总结
提出Uni-PK框架，将分子表示与神经常微分方程结合在机制基础的PK结构中，为下一代药动学建模和精准医学提供可扩展、可解释且减少动物使用的解决方案。

**关键词**: 神经常微分方程、药动学、分子表示、个性化医学、深度学习

## 摘要（英文）
Accurate modeling of drug concentration-time (C-t) profiles is central to pharmacokinetics (PK) and plays a critical role in both early-stage compound selection and late-stage individualized dosing. Traditional PK models offer mechanistic interpretability but often rely on rigid assumptions and extensive parametrization, limiting their scalability across structurally diverse compounds and heterogeneous patient populations. In this work, we propose Uni-PK, a unified neural framework that combines molecular representations with neural ordinary differential equations (NODEs) embedded within a mechanistically grounded PK structure. Rather than solely predicting PK parameters, Uni-PK directly models the dynamic trajectory of drug concentrations from molecular and individual inputs, enabling end-to-end learning under data-scarce and noisy conditions. To account for interindividual variability, we incorporated auxiliary covariates─such as species and dosing regimen─via a flexible context encoder, supporting personalized preclinical and clinical settings. Evaluated on rat and human data sets spanning multiple administration routes and physiological states, Uni-PK showed robust performance while remaining consistent with established pharmacokinetic principles. By integration of chemical structure and individual-specific information within a dynamic modeling framework, Uni-PK offers a scalable, interpretable, and animal-sparing solution for next-generation PK modeling and precision therapeutics.

## 摘要（中文）
准确模拟药物浓度-时间（C-t）曲线是药动学（PK）的核心，对早期化合物筛选和晚期个体化给药都起着至关重要的作用。传统的PK模型提供了机制可解释性，但通常依赖于严格的假设和大量的参数化，限制了其在结构多样化合物和异质患者群体中的可扩展性。在这项工作中，我们提出了Uni-PK，这是一个统一的神经框架，将分子表示与嵌入在机制基础PK结构中的神经常微分方程（NODEs）相结合。Uni-PK不仅仅预测PK参数，而是直接从分子和个体输入建模药物浓度的动态轨迹，能够在数据稀缺和噪声条件下进行端到端学习。为了解释个体间的变异性，我们通过灵活的上下文编码器纳入了辅助协变量（如物种和给药方案），支持个性化的临床前和临床设置。在跨越多种给药途径和生理状态的大鼠和人类数据集上的评估表明，Uni-PK展现了稳健的性能，同时与既定的药动学原理保持一致。通过在动态建模框架中整合化学结构和个体特异性信息，Uni-PK为下一代PK建模和精准治疗学提供了一个可扩展的、可解释的、减少动物使用的解决方案。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnP-2BC5LCoOzD71-2BC2MKt2ViF4uoDO93G9iDwzzHJndQYcAYZPw-2FLBwlxDAD9kvbqTnua6v9eGwqtnnacnc2wKTbAqvOlyMCmBBD6J55Mkj-2Bh-2FuHv1S7-2FTugfQhiTVwr1qqPtR2Q_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FCpYzkzyQ8K9Moac7C3kD2SLcLQvkWs9Rc2gKGowY08-2FrQ1g30FCPjVEJF632EiZLf1PTclKN8-2FpCJjZAfzvZcJ-2BTl7t6rzMbYocXUe0nbeAySAcdeSf0ahEPc-2F77k2XgF-2FlhYTzCgvItW5xOLrNt2MvvK-2B-2BBqLhbxo0t9lCgezjj0vaLuG9moHVleOOTJriG4-3D)
