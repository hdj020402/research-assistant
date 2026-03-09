---
title: "Improving Fidelity and Diversity in Chemical Language Transformers for Inverse Molecular Design"
title_zh: "提高用于逆分子设计的化学语言转换器的保真度和多样性"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c03062"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPVU0Kt6yn7IQ-2Bb8RVOgmVxfS73f6APjPx3BJWBy53hRFqwDH3U4gKQo3iYFP6iPZ8ZQXJnm8sr2-2BupbBCMHKW17QOXaQ6PUDWviINntZufFkFPeSRDrSkI93H4V53si7ad9sk_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjMiGhqYuNZSeljVi5kw6RDOwb5HTN1959abUlgudU81sChnIVYBqhIeptXXrPrpqgJ7H3j-2BTPIaBBmektYijGCIcZQI7K7o8rXXc7ihnURtd5Duar-2FR1h5fAWYQHpwxmTTb5as8zDRJ3hCDCm-2FKAySSEFoSNt3HS-2BrH-2FPRMNCygrXzb-2FP-2B-2FWGFGpFbIiJmuXD1z9JJJKOs-2FkFuKOfiTgRJITgBLHPCO4Xgq149e5juCU-3D"
pub_date: ""
tags: ["deep-learning", "molecular-design", "language-models", "generative-models", "inverse-design"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Improving Fidelity and Diversity in Chemical Language Transformers for Inverse Molecular Design

**提高用于逆分子设计的化学语言转换器的保真度和多样性**

## 精华总结
本文提出了一个基于化学语言转换器的逆向分子设计框架，通过往返保真度指标量化解码器诱导的潜在空间漂移，并采用后解码重排序和预测器引导的最小编辑修复来改进生成分子的有效性和多样性。该框架在表面活性剂临界胶束浓度设计中实现了约90%的有效分子比例和接近1%的目标性质误差。

**关键词**: 化学语言模型、逆向分子设计、转换器、条件生成、分子优化

## 摘要（英文）
Rapid, sustainable redesign of large functional molecules demands efficient exploration of vast chemical spaces. Chemical language models (CLMs), especially transformers, learn long-range structure-property relations and enable swift, batched candidate generation after training. However, inverse molecular design is often ill-posed─many structures can meet a target─and conditioned generation often decodes to invalid or off-spec molecules. To address this challenge, we propose a novel CLM-based inverse design framework that optimizes latent representations toward desired target properties. Our approach introduces a round-trip fidelity metric to quantify and diagnose decoder-induced latent-space drift, which we mitigate via postdecoding re-ranking and predictor-guided minimal-edit repair to correct invalid structures. To demonstrate the framework, we target the surfactant critical micelle concentration (CMC) and compare large pretrained CLMs, our lightweight CLM, a fragment-based genetic algorithm, and a prompt-conditioned ChatGPT baseline. We observe that our framework yields a high proportion of valid and diverse molecules (∼90%) while maintaining a target property error close to 1%. Moreover, interpretability analysis confirms that the designed molecular structures adhere to established physical design rules, highlighting the framework's ability to extract physical insights for molecular design. Therefore, the current framework provides an efficient and broadly applicable solution to the inverse design of novel functional molecules.

## 摘要（中文）
大功能分子的快速，可持续的重新设计需要对广阔的化学空间进行有效的探索。化学语言模型 (clm)，尤其是transformers，可以学习远程结构-属性关系，并在训练后快速生成批量候选者。但是，反向分子设计通常是不正确的-许多结构可以满足目标-并且条件生成通常会解码为无效或不合格的分子。为了应对这一挑战，我们提出了一种新颖的基于CLM的逆向设计框架，该框架可针对所需的目标属性优化潜在表示。我们的方法引入了往返保真度度量来量化和诊断解码器引起的潜在空间漂移，我们通过解码后重新排序和预测器引导的最小编辑修复来纠正无效结构来缓解这种漂移。为了演示该框架，我们以表面活性剂临界胶束浓度 (CMC) 为目标，并比较了大型预训练的CLM，我们的轻量级CLM，基于片段的遗传算法和即时条件的ChatGPT基线。我们观察到，我们的框架产生了高比例的有效和多样化的分子 (∼ 90%)，同时保持了接近1% 的目标属性误差。此外，可解释性分析证实，所设计的分子结构符合既定的物理设计规则，突出了框架提取分子设计的物理见解的能力。因此，当前的框架提供了一种有效且广泛适用的解决方案，用于新型功能分子的逆向设计。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPVU0Kt6yn7IQ-2Bb8RVOgmVxfS73f6APjPx3BJWBy53hRFqwDH3U4gKQo3iYFP6iPZ8ZQXJnm8sr2-2BupbBCMHKW17QOXaQ6PUDWviINntZufFkFPeSRDrSkI93H4V53si7ad9sk_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjMiGhqYuNZSeljVi5kw6RDOwb5HTN1959abUlgudU81sChnIVYBqhIeptXXrPrpqgJ7H3j-2BTPIaBBmektYijGCIcZQI7K7o8rXXc7ihnURtd5Duar-2FR1h5fAWYQHpwxmTTb5as8zDRJ3hCDCm-2FKAySSEFoSNt3HS-2BrH-2FPRMNCygrXzb-2FP-2B-2FWGFGpFbIiJmuXD1z9JJJKOs-2FkFuKOfiTgRJITgBLHPCO4Xgq149e5juCU-3D)
