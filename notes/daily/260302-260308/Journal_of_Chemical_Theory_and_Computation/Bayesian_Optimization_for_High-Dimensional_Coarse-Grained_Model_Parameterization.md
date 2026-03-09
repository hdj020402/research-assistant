---
title: "Bayesian Optimization for High-Dimensional Coarse-Grained Model Parameterization: A Case Study on Pebax Polymer"
title_zh: "高维粗粒度模型参数化的贝叶斯优化: 以Pebax聚合物为例"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01500"
url: "https://app.acspubs.org/e/er?s=1913652004&lid=109588&pci=CACSR000013623915&elqTrackId=b1a26c2857424180b9083642f357dc95&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF5E85ED303AD08530CE3111AC129C7E830DF669D1886211F10624EBC003E655BFD"
pub_date: ""
tags: ["bayesian-optimization", "coarse-grained-modeling", "force-field-parameterization", "materials-simulation", "hyperparameter-optimization"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Bayesian Optimization for High-Dimensional Coarse-Grained Model Parameterization: A Case Study on Pebax Polymer

**高维粗粒度模型参数化的贝叶斯优化: 以Pebax聚合物为例**

## 精华总结
本研究成功将贝叶斯优化（特别是树结构Parzen估计器）扩展到高维粗粒化力场模型参数化，以Pebax聚合物为例，同时优化41个参数并准确再现原子表示的关键物理性质。该方法相比传统算法收敛更快，打破了贝叶斯优化仅限于低维优化的假设。

**关键词**: 贝叶斯优化、粗粒化模型、力场参数化、高维优化、树结构Parzen估计器

## 摘要（英文）
Coarse-grained (CG) force field models are extensively utilized in material simulations because of their scalability. Ordinarily, these models are parametrized using hybrid strategies that sequentially integrate top-down and bottom-up approaches. However, this combination restricts the capacity to jointly optimize all parameters. Although Bayesian optimization (BO) has been explored as an alternative search strategy to identify well-optimized CG parameters, its application has conventionally been limited to low-dimensional scenarios. This has contributed to the assumption that BO is unsuitable for more complex CG models, which often involve a large number of parameters. In this study, we challenge this assumption by successfully extending BO, using the tree-structured Parzen estimator (TPE) model, to optimize a high-dimensional CG model. Specifically, we show that a 41-parameter CG model of Pebax-1657, a copolymer composed of alternating polyamide and polyether segments, can be effectively parametrized using BO, resulting in a model that accurately reproduces the key physical properties of its parent atomistic representation. Our optimization framework simultaneously targets structural and thermodynamic properties, namely, density, radius of gyration, and glass transition temperature. Compared to traditional search algorithms, BO-TPE not only converges faster but also delivers consistent improvements over more standard parametrization approaches.

## 摘要（中文）
粗粒度 (CG) 力场模型由于其可扩展性而广泛用于材料模拟中。通常，这些模型是使用混合策略进行参数化的，这些策略依次集成了自上而下和自下而上的方法。然而，这种组合限制了联合优化所有参数的能力。尽管已经探索了贝叶斯优化 (BO) 作为识别良好优化的CG参数的替代搜索策略，但其应用通常限于低维场景。这有助于假设BO不适合更复杂的CG模型，这些模型通常涉及大量参数。在这项研究中，我们通过使用树结构的Parzen估计器 (TPE) 模型成功扩展BO来优化高维CG模型，从而挑战了这一假设。具体来说，我们表明，Pebax-1657的41参数CG模型，一种由交替的聚酰胺和聚醚链段组成的共聚物，可以使用BO有效地参数化，从而产生一个准确再现其母体原子表示的关键物理性质的模型。我们的优化框架同时针对结构和热力学性质，即密度，回转半径和玻璃化转变温度。与传统的搜索算法相比，bo-tpe不仅收敛速度更快，而且在更标准的参数化方法上提供了一致的改进。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](https://app.acspubs.org/e/er?s=1913652004&lid=109588&pci=CACSR000013623915&elqTrackId=b1a26c2857424180b9083642f357dc95&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF5E85ED303AD08530CE3111AC129C7E830DF669D1886211F10624EBC003E655BFD)
