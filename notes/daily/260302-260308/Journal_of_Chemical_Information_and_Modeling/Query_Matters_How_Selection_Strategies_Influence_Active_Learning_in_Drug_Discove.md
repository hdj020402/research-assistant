---
title: "Query Matters: How Selection Strategies Influence Active Learning in Drug Discovery"
title_zh: "问题: 选择策略如何影响药物发现中的主动学习"
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

**问题: 选择策略如何影响药物发现中的主动学习**

## 精华总结
SimDMTA是一个模拟药物发现中设计-制造-测试-分析(DMTA)循环的在硅框架,研究表明基于不确定性的采样在命中发现和模型泛化能力上明显优于贪心和混合方法。

**关键词**: 主动学习、药物发现、查询策略、不确定性采样、DMTA循环

## 摘要（英文）
We present SimDMTA, an in silico framework designed to simulate the Design-Make-Test-Analyze (DMTA) cycle used in preclinical drug discovery. Using docking scores as a proxy for biological assays, the simulations allow factors controlling the efficiency of the DMTA cycle to be explored in a manner that would not be feasible using traditional experiments due to time and cost constraints. In this workflow, a machine learning model predicts docking scores, selects compounds using various query strategies, docks selected molecules, and retrains iteratively. Starting from a broad chemical space, the model actively samples molecules derived from a 3,5-dimethyl-4-phenylisoxazole scaffold, an active warhead for the Bromodomain 4 (BRD4) BD1 binding site, to refine its predictions. Our results show that uncertainty-based sampling significantly outperforms greedy and hybrid approaches in both hit discovery and the ability of the model that predicts docking scores to generalize beyond its training set. Notably, by the final iteration, 37 of the top 50 ranked compounds were within the top 1% of the chemical space of all evaluated compounds. Strategies that include some random selection correct systematic biases more rapidly, but are less effective at predicting top-performing molecules. These findings underscore the value of incorporating molecular diversity and uncertainty into design strategies. While such strategies may deprioritize those molecules with the highest absolute predictions in early rounds, they markedly accelerate model refinement, ultimately leading to more effective hit identification in discovery driven by active learning.

## 摘要（中文）
我们介绍了SimDMTA，这是一个计算机框架，旨在模拟临床前药物发现中使用的设计-制造-测试一下-分析 (DMTA) 循环。使用对接分数作为生物测定的代理，模拟允许以由于时间和成本限制而使用传统实验不可行的方式探索控制DMTA循环效率的因素。在这个工作流程中，机器学习模型预测对接分数，使用各种查询策略选择化合物，对接选定的分子，并迭代地重新训练。从广阔的化学空间开始，该模型积极地对源自3，5-二甲基-4-苯基异恶唑支架的分子进行采样，该支架是溴结构域4 (BRD4) BD1结合位点的活性弹头，以完善其预测。我们的结果表明，基于不确定性的采样在命中发现和模型预测对接分数以超越其训练集的能力方面均显着优于贪婪和混合方法。值得注意的是，通过最后的迭代，前50个排序的化合物中的37个在所有评估的化合物的化学空间的前1% 个内。包括一些随机选择的策略可以更快地纠正系统偏差，但在预测表现最好的分子方面效果较差。这些发现强调了将分子多样性和不确定性纳入设计策略的价值。虽然这些策略可能会在早期几轮中降低那些具有最高绝对预测的分子的优先级，但它们显着加速了模型的完善，最终导致在主动学习驱动的发现中更有效的命中识别。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPgXB0pDDJIdoi8OatcX3Jjvw2aYSfM-2FZBDbz76Xq4oZfRD8RiJpxW3kqConeeQ0uPGe2n4W9S1JSBlBcNefTWGYJsnZ-2Fyor2JV2m7v-2BwCenoJd5Pw8EQNyDinl5462QqDp8zb_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBuLQXZxM7jyrWmhgGsKhiQXqVpQ48dAEcCGxn7s121gfK4ZNMTFF89vBgdm8nj-2Bc7KzDWycmUk-2FCDY0wSKTCdBGzVY4S4tNcqY9eo5-2FrLbyD13Rld96WyjB9iKfVke3jiUcVusAL2A3GiXD5tMmxFEYWAGnmD4AUThB6n2X8IAKVv7rHSRTL03XZ0b87hVoZk-3D)
