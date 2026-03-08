---
title: "Toward Generalizable Data-Driven Pharmacokinetics with Interpretable Neural ODEs"
title_zh: "可解释神经常微分方程在通用药代动力学中的应用"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02924"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnP-2BC5LCoOzD71-2BC2MKt2ViF4uoDO93G9iDwzzHJndQYcAYZPw-2FLBwlxDAD9kvbqTnua6v9eGwqtnnacnc2wKTbAqvOlyMCmBBD6J55Mkj-2Bh-2FuHv1S7-2FTugfQhiTVwr1qqPtR2Q_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FCpYzkzyQ8K9Moac7C3kD2SLcLQvkWs9Rc2gKGowY08-2FrQ1g30FCPjVEJF632EiZLf1PTclKN8-2FpCJjZAfzvZcJ-2BTl7t6rzMbYocXUe0nbeAySAcdeSf0ahEPc-2F77k2XgF-2FlhYTzCgvItW5xOLrNt2MvvK-2B-2BBqLhbxo0t9lCgezjj0vaLuG9moHVleOOTJriG4-3D"
pub_date: ""
tags: ["neural-odes", "pharmacokinetics", "deep-learning", "drug-discovery", "personalized-medicine"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Toward Generalizable Data-Driven Pharmacokinetics with Interpretable Neural ODEs

**可解释神经常微分方程在通用药代动力学中的应用**

## 精华总结
提出Uni-PK框架，整合分子表征与神经常微分方程以建立可解释的药代动力学模型，支持个性化医疗和减少动物实验。

**关键词**: 神经常微分方程、药代动力学、机器学习、分子表征、精准医疗

## 摘要（英文）
Accurate modeling of drug concentration-time (C-t) profiles is central to pharmacokinetics (PK) and plays a critical role in both early-stage compound selection and late-stage individualized dosing. Traditional PK models offer mechanistic interpretability but often rely on rigid assumptions and extensive parametrization, limiting their scalability across structurally diverse compounds and heterogeneous patient populations. In this work, we propose Uni-PK, a unified neural framework that combines molecular representations with neural ordinary differential equations (NODEs) embedded within a mechanistically grounded PK structure. Rather than solely predicting PK parameters, Uni-PK directly models the dynamic trajectory of drug concentrations from molecular and individual inputs, enabling end-to-end learning under data-scarce and noisy conditions. To account for interindividual variability, we incorporated auxiliary covariates─such as species and dosing regimen─via a flexible context encoder, supporting personalized preclinical and clinical settings. Evaluated on rat and human data sets spanning multiple administration routes and physiological states, Uni-PK showed robust performance while remaining consistent with established pharmacokinetic principles. By integration of chemical structure and individual-specific information within a dynamic modeling framework, Uni-PK offers a scalable, interpretable, and animal-sparing solution for next-generation PK modeling and precision therapeutics.

## 摘要（中文）
本研究提出Uni-PK框架，将分子表征与神经常微分方程集成在机制清晰的药代动力学结构中，直接模拟药物浓度-时间动态轨迹。该方法结合辅助协变量处理个体差异，在数据稀缺和噪声条件下实现端到端学习。在大鼠和人体数据集上验证表明，Uni-PK具有鲁棒性、可解释性和替代动物实验的潜力，为精准医疗的下一代药代动力学建模提供了可扩展方案。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnP-2BC5LCoOzD71-2BC2MKt2ViF4uoDO93G9iDwzzHJndQYcAYZPw-2FLBwlxDAD9kvbqTnua6v9eGwqtnnacnc2wKTbAqvOlyMCmBBD6J55Mkj-2Bh-2FuHv1S7-2FTugfQhiTVwr1qqPtR2Q_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FCpYzkzyQ8K9Moac7C3kD2SLcLQvkWs9Rc2gKGowY08-2FrQ1g30FCPjVEJF632EiZLf1PTclKN8-2FpCJjZAfzvZcJ-2BTl7t6rzMbYocXUe0nbeAySAcdeSf0ahEPc-2F77k2XgF-2FlhYTzCgvItW5xOLrNt2MvvK-2B-2BBqLhbxo0t9lCgezjj0vaLuG9moHVleOOTJriG4-3D)
