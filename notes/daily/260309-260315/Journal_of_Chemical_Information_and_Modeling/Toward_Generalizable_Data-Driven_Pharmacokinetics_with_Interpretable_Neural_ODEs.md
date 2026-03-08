---
title: "Toward Generalizable Data-Driven Pharmacokinetics with Interpretable Neural ODEs"
title_zh: "基于可解释神经微分方程的通用数据驱动药代动力学模型"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02924"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnP-2BC5LCoOzD71-2BC2MKt2ViF4uoDO93G9iDwzzHJndQYcAYZPw-2FLBwlxDAD9kvbqTnua6v9eGwqtnnacnc2wKTbAqvOlyMCmBBD6J55Mkj-2Bh-2FuHv1S7-2FTugfQhiTVwr1qqPtR2Q_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FCpYzkzyQ8K9Moac7C3kD2SLcLQvkWs9Rc2gKGowY08-2FrQ1g30FCPjVEJF632EiZLf1PTclKN8-2FpCJjZAfzvZcJ-2BTl7t6rzMbYocXUe0nbeAySAcdeSf0ahEPc-2F77k2XgF-2FlhYTzCgvItW5xOLrNt2MvvK-2B-2BBqLhbxo0t9lCgezjj0vaLuG9moHVleOOTJriG4-3D"
pub_date: ""
tags: ["neural-ode", "pharmacokinetics", "deep-learning", "drug-discovery", "precision-medicine"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Toward Generalizable Data-Driven Pharmacokinetics with Interpretable Neural ODEs

**基于可解释神经微分方程的通用数据驱动药代动力学模型**

## 精华总结
提出Uni-PK框架，结合分子表征与神经常微分方程，在机制驱动的药代动力学结构中直接建模药物浓度动态，为精准治疗提供可扩展、可解释的解决方案。

**关键词**: 神经常微分方程、药代动力学、分子表征、个性化医疗、深度学习

## 摘要（英文）
Accurate modeling of drug concentration-time (C-t) profiles is central to pharmacokinetics (PK) and plays a critical role in both early-stage compound selection and late-stage individualized dosing. Traditional PK models offer mechanistic interpretability but often rely on rigid assumptions and extensive parametrization, limiting their scalability across structurally diverse compounds and heterogeneous patient populations. In this work, we propose Uni-PK, a unified neural framework that combines molecular representations with neural ordinary differential equations (NODEs) embedded within a mechanistically grounded PK structure. Rather than solely predicting PK parameters, Uni-PK directly models the dynamic trajectory of drug concentrations from molecular and individual inputs, enabling end-to-end learning under data-scarce and noisy conditions. To account for interindividual variability, we incorporated auxiliary covariates─such as species and dosing regimen─via a flexible context encoder, supporting personalized preclinical and clinical settings. Evaluated on rat and human data sets spanning multiple administration routes and physiological states, Uni-PK showed robust performance while remaining consistent with established pharmacokinetic principles. By integration of chemical structure and individual-specific information within a dynamic modeling framework, Uni-PK offers a scalable, interpretable, and animal-sparing solution for next-generation PK modeling and precision therapeutics.

## 摘要（中文）
本研究提出Uni-PK框架，将分子表征与神经常微分方程（NODEs）融合于机制驱动的药代动力学结构中，直接从分子和个体输入建模药物浓度动态轨迹。通过灵活的上下文编码器整合物种、给药方案等协变量，支持个性化的临床前和临床应用。在大鼠和人类数据集上验证表明，该方法在保持药代原理一致性的同时展现出稳健性能，为下一代药代模型和精准治疗提供可扩展、可解释的解决方案。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnP-2BC5LCoOzD71-2BC2MKt2ViF4uoDO93G9iDwzzHJndQYcAYZPw-2FLBwlxDAD9kvbqTnua6v9eGwqtnnacnc2wKTbAqvOlyMCmBBD6J55Mkj-2Bh-2FuHv1S7-2FTugfQhiTVwr1qqPtR2Q_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FCpYzkzyQ8K9Moac7C3kD2SLcLQvkWs9Rc2gKGowY08-2FrQ1g30FCPjVEJF632EiZLf1PTclKN8-2FpCJjZAfzvZcJ-2BTl7t6rzMbYocXUe0nbeAySAcdeSf0ahEPc-2F77k2XgF-2FlhYTzCgvItW5xOLrNt2MvvK-2B-2BBqLhbxo0t9lCgezjj0vaLuG9moHVleOOTJriG4-3D)
