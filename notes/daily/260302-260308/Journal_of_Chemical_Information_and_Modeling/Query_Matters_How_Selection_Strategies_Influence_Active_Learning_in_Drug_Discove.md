---
title: "Query Matters: How Selection Strategies Influence Active Learning in Drug Discovery"
title_zh: "研究议题：选择策略如何影响药物发现中的主动学习"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02504"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPgXB0pDDJIdoi8OatcX3Jjvw2aYSfM-2FZBDbz76Xq4oZfRD8RiJpxW3kqConeeQ0uPGe2n4W9S1JSBlBcNefTWGYJsnZ-2Fyor2JV2m7v-2BwCenoJd5Pw8EQNyDinl5462QqDp8zb_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBuLQXZxM7jyrWmhgGsKhiQXqVpQ48dAEcCGxn7s121gfK4ZNMTFF89vBgdm8nj-2Bc7KzDWycmUk-2FCDY0wSKTCdBGzVY4S4tNcqY9eo5-2FrLbyD13Rld96WyjB9iKfVke3jiUcVusAL2A3GiXD5tMmxFEYWAGnmD4AUThB6n2X8IAKVv7rHSRTL03XZ0b87hVoZk-3D"
pub_date: ""
tags: ["active-learning", "drug-discovery", "machine-learning", "molecular-docking", "compound-selection"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Query Matters: How Selection Strategies Influence Active Learning in Drug Discovery

**研究议题：选择策略如何影响药物发现中的主动学习**

## 精华总结
SimDMTA是一个模拟药物发现中设计-制造-测试-分析(DMTA)循环的硅学框架,研究表明基于不确定性的采样策略在命中发现和模型泛化能力上明显优于贪心和混合方法。

**关键词**: 主动学习、药物发现、查询策略、不确定性采样、分子对接

## 摘要（英文）
We present SimDMTA, an in silico framework designed to simulate the Design-Make-Test-Analyze (DMTA) cycle used in preclinical drug discovery. Using docking scores as a proxy for biological assays, the simulations allow factors controlling the efficiency of the DMTA cycle to be explored in a manner that would not be feasible using traditional experiments due to time and cost constraints. In this workflow, a machine learning model predicts docking scores, selects compounds using various query strategies, docks selected molecules, and retrains iteratively. Starting from a broad chemical space, the model actively samples molecules derived from a 3,5-dimethyl-4-phenylisoxazole scaffold, an active warhead for the Bromodomain 4 (BRD4) BD1 binding site, to refine its predictions. Our results show that uncertainty-based sampling significantly outperforms greedy and hybrid approaches in both hit discovery and the ability of the model that predicts docking scores to generalize beyond its training set. Notably, by the final iteration, 37 of the top 50 ranked compounds were within the top 1% of the chemical space of all evaluated compounds. Strategies that include some random selection correct systematic biases more rapidly, but are less effective at predicting top-performing molecules. These findings underscore the value of incorporating molecular diversity and uncertainty into design strategies. While such strategies may deprioritize those molecules with the highest absolute predictions in early rounds, they markedly accelerate model refinement, ultimately leading to more effective hit identification in discovery driven by active learning.

## 摘要（中文）
我们提出了SimDMTA，这是一个用于模拟临床前药物发现中所用的设计-制造-测试一下-分析（DMTA）循环的计算机模拟框架。以对接评分作为生物活性测定的替代指标，这些模拟研究能够探讨调控DMTA循环效率的各种因素，而这种研究若采用传统实验方法，则会因时间和成本限制而难以实施。在该工作流中，机器学习模型首先预测对接分数，然后采用多种查询策略筛选化合物，对接所选分子，并迭代地进行模型再训练。该模型从广阔的化学空间出发，主动采样源自3,5-二甲基-4-苯基异噁唑骨架的分子——该骨架是溴结构域4（BRD4）BD1结合位点的有效药效基团——以优化其预测结果。我们的研究结果表明，基于不确定性的采样方法在命中化合物的发现以及预测对接评分的模型对其训练集之外数据的泛化能力方面，均显著优于贪心策略和混合策略。值得注意的是，在最后一轮迭代中，排名前50的化合物中有37种位于所有已评估化合物化学空间的前1%范围内。包含随机选择环节的策略能够更快地纠正系统性偏差，但在预测表现最佳的分子方面效果较差。这些发现强调了在设计策略中纳入分子多样性和不确定性的重要性。尽管这类策略在早期迭代中可能会降低对绝对预测值最高的分子的优先级，但它们能显著加速模型精炼过程，最终在主动学习驱动的药物发现中实现更高效的苗头化合物识别。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPgXB0pDDJIdoi8OatcX3Jjvw2aYSfM-2FZBDbz76Xq4oZfRD8RiJpxW3kqConeeQ0uPGe2n4W9S1JSBlBcNefTWGYJsnZ-2Fyor2JV2m7v-2BwCenoJd5Pw8EQNyDinl5462QqDp8zb_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBuLQXZxM7jyrWmhgGsKhiQXqVpQ48dAEcCGxn7s121gfK4ZNMTFF89vBgdm8nj-2Bc7KzDWycmUk-2FCDY0wSKTCdBGzVY4S4tNcqY9eo5-2FrLbyD13Rld96WyjB9iKfVke3jiUcVusAL2A3GiXD5tMmxFEYWAGnmD4AUThB6n2X8IAKVv7rHSRTL03XZ0b87hVoZk-3D)
