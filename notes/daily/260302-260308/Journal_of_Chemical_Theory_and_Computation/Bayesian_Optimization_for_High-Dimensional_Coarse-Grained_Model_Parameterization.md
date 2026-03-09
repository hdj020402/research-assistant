---
title: "Bayesian Optimization for High-Dimensional Coarse-Grained Model Parameterization: A Case Study on Pebax Polymer"
title_zh: "高维粗粒化模型参数化的贝叶斯优化：以Pebax聚合物为例"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01500"
url: "https://app.acspubs.org/e/er?s=1913652004&lid=109588&pci=CACSR000013623915&elqTrackId=b1a26c2857424180b9083642f357dc95&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF5E85ED303AD08530CE3111AC129C7E830DF669D1886211F10624EBC003E655BFD"
pub_date: ""
tags: ["bayesian-optimization", "coarse-grained-models", "force-field-parameterization", "polymer-simulation", "hyperparameter-optimization"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Bayesian Optimization for High-Dimensional Coarse-Grained Model Parameterization: A Case Study on Pebax Polymer

**高维粗粒化模型参数化的贝叶斯优化：以Pebax聚合物为例**

## 精华总结
本研究成功将贝叶斯优化（BO）与树结构Parzen估计器（TPE）扩展应用于高维粗粒化力场模型参数化，以Pebax聚合物为例，展示了BO相比传统方法在参数优化中的优越性和快速收敛特性。该框架能够同时优化结构和热力学性质，包括密度、回旋半径和玻璃转化温度。

**关键词**: 贝叶斯优化、粗粒化模型、参数化、树结构Parzen估计器、聚合物模拟

## 摘要（英文）
Coarse-grained (CG) force field models are extensively utilized in material simulations because of their scalability. Ordinarily, these models are parametrized using hybrid strategies that sequentially integrate top-down and bottom-up approaches. However, this combination restricts the capacity to jointly optimize all parameters. Although Bayesian optimization (BO) has been explored as an alternative search strategy to identify well-optimized CG parameters, its application has conventionally been limited to low-dimensional scenarios. This has contributed to the assumption that BO is unsuitable for more complex CG models, which often involve a large number of parameters. In this study, we challenge this assumption by successfully extending BO, using the tree-structured Parzen estimator (TPE) model, to optimize a high-dimensional CG model. Specifically, we show that a 41-parameter CG model of Pebax-1657, a copolymer composed of alternating polyamide and polyether segments, can be effectively parametrized using BO, resulting in a model that accurately reproduces the key physical properties of its parent atomistic representation. Our optimization framework simultaneously targets structural and thermodynamic properties, namely, density, radius of gyration, and glass transition temperature. Compared to traditional search algorithms, BO-TPE not only converges faster but also delivers consistent improvements over more standard parametrization approaches.

## 摘要（中文）
粗粒化力场模型因其可扩展性而在材料模拟中得到广泛应用。通常，这些模型采用混合策略进行参数化，该策略依次整合自上而下和自下而上的方法。然而，这种组合限制了对所有参数进行联合优化的能力。尽管贝叶斯优化（BO）已被探索作为一种替代搜索策略，用于识别优化良好的CG参数，但其应用传统上一直局限于低维场景。这导致了一种假设，即BO不适合用于更复杂的计算机图形学模型，因为这类模型通常涉及大量参数。在本研究中，我们通过成功地将贝叶斯优化方法扩展至高维计算流体力学模型的优化，并采用树结构帕尔森估计器模型，对这一假设提出了挑战。具体而言，我们表明，对于由聚酰胺和聚醚嵌段交替组成的共聚物Pebax-1657，一个包含41个力场参数的粗粒化模型可以通过贝叶斯优化有效拟合参数，从而得到一个能够准确再现其原子级参考模型关键物理性质的模型。我们的优化框架同时以结构和热力学性质为目标，即密度、回转半径和玻璃化转变温度。与传统搜索算法相比，BO-TPE不仅收敛速度更快，而且在性能上持续优于更标准的超参数调优方法。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](https://app.acspubs.org/e/er?s=1913652004&lid=109588&pci=CACSR000013623915&elqTrackId=b1a26c2857424180b9083642f357dc95&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF5E85ED303AD08530CE3111AC129C7E830DF669D1886211F10624EBC003E655BFD)
