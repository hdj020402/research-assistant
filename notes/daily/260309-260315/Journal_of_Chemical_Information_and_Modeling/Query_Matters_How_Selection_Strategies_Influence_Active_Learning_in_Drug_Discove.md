---
title: "Query Matters: How Selection Strategies Influence Active Learning in Drug Discovery"
title_zh: "查询策略重要：选择策略如何影响药物发现中的主动学习"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02504"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPgXB0pDDJIdoi8OatcX3Jjvw2aYSfM-2FZBDbz76Xq4oZfRD8RiJpxW3kqConeeQ0uPGe2n4W9S1JSBlBcNefTWGYJsnZ-2Fyor2JV2m7v-2BwCenoJd5Pw8EQNyDinl5462QqDp8zb_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBuLQXZxM7jyrWmhgGsKhiQXqVpQ48dAEcCGxn7s121gfK4ZNMTFF89vBgdm8nj-2Bc7KzDWycmUk-2FCDY0wSKTCdBGzVY4S4tNcqY9eo5-2FrLbyD13Rld96WyjB9iKfVke3jiUcVusAL2A3GiXD5tMmxFEYWAGnmD4AUThB6n2X8IAKVv7rHSRTL03XZ0b87hVoZk-3D"
pub_date: ""
tags: ["active-learning", "drug-discovery", "machine-learning", "molecular-docking", "query-strategy"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Query Matters: How Selection Strategies Influence Active Learning in Drug Discovery

**查询策略重要：选择策略如何影响药物发现中的主动学习**

## 精华总结
SimDMTA框架模拟药物发现的设计-制造-测试-分析循环，证明不确定性采样策略在命中发现和模型泛化中显著优于其他方法。

**关键词**: 主动学习、不确定性采样、药物发现、机器学习、分子对接

## 摘要（英文）
We present SimDMTA, an in silico framework designed to simulate the Design-Make-Test-Analyze (DMTA) cycle used in preclinical drug discovery. Using docking scores as a proxy for biological assays, the simulations allow factors controlling the efficiency of the DMTA cycle to be explored in a manner that would not be feasible using traditional experiments due to time and cost constraints. In this workflow, a machine learning model predicts docking scores, selects compounds using various query strategies, docks selected molecules, and retrains iteratively. Starting from a broad chemical space, the model actively samples molecules derived from a 3,5-dimethyl-4-phenylisoxazole scaffold, an active warhead for the Bromodomain 4 (BRD4) BD1 binding site, to refine its predictions. Our results show that uncertainty-based sampling significantly outperforms greedy and hybrid approaches in both hit discovery and the ability of the model that predicts docking scores to generalize beyond its training set. Notably, by the final iteration, 37 of the top 50 ranked compounds were within the top 1% of the chemical space of all evaluated compounds. Strategies that include some random selection correct systematic biases more rapidly, but are less effective at predicting top-performing molecules. These findings underscore the value of incorporating molecular diversity and uncertainty into design strategies. While such strategies may deprioritize those molecules with the highest absolute predictions in early rounds, they markedly accelerate model refinement, ultimately leading to more effective hit identification in discovery driven by active learning.

## 摘要（中文）
我们提出SimDMTA框架，用于模拟药物发现中的设计-制造-测试-分析循环。该框架使用分子对接评分预测生物活性，通过机器学习模型迭代地选择化合物并进行对接。研究表明，不确定性采样策略在命中发现和模型泛化能力方面显著优于贪心和混合方法。最终迭代中，排名前50的化合物中有37个属于所有评估化合物的前1%。结果强调了在设计策略中融合分子多样性和不确定性的价值。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPgXB0pDDJIdoi8OatcX3Jjvw2aYSfM-2FZBDbz76Xq4oZfRD8RiJpxW3kqConeeQ0uPGe2n4W9S1JSBlBcNefTWGYJsnZ-2Fyor2JV2m7v-2BwCenoJd5Pw8EQNyDinl5462QqDp8zb_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBuLQXZxM7jyrWmhgGsKhiQXqVpQ48dAEcCGxn7s121gfK4ZNMTFF89vBgdm8nj-2Bc7KzDWycmUk-2FCDY0wSKTCdBGzVY4S4tNcqY9eo5-2FrLbyD13Rld96WyjB9iKfVke3jiUcVusAL2A3GiXD5tMmxFEYWAGnmD4AUThB6n2X8IAKVv7rHSRTL03XZ0b87hVoZk-3D)
