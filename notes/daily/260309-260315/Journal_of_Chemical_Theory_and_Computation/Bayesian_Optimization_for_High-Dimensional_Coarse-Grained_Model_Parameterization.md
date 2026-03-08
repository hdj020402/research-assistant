---
title: "Bayesian Optimization for High-Dimensional Coarse-Grained Model Parameterization: A Case Study on Pebax Polymer"
title_zh: "贝叶斯优化在高维粗粒化模型参数化中的应用：Pebax聚合物案例研究"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01500"
url: "https://app.acspubs.org/e/er?s=1913652004&lid=109588&pci=CACSR000013623915&elqTrackId=b1a26c2857424180b9083642f357dc95&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF5E85ED303AD08530CE3111AC129C7E830DF669D1886211F10624EBC003E655BFD"
pub_date: ""
tags: ["bayesian-optimization", "coarse-grained-modeling", "polymer-simulation", "hyperparameter-optimization", "high-dimensional-search"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Bayesian Optimization for High-Dimensional Coarse-Grained Model Parameterization: A Case Study on Pebax Polymer

**贝叶斯优化在高维粗粒化模型参数化中的应用：Pebax聚合物案例研究**

## 精华总结
首次成功将贝叶斯优化应用于高维粗粒化模型参数化（41维），通过TPE方法同时优化多个物理性质，实现了比传统方法更快的收敛和更准确的参数化结果。

**关键词**: 贝叶斯优化、粗粒化模型、参数化、聚合物模拟、树结构Parzen估计器

## 摘要（英文）
Coarse-grained (CG) force field models are extensively utilized in material simulations because of their scalability. Ordinarily, these models are parametrized using hybrid strategies that sequentially integrate top-down and bottom-up approaches. However, this combination restricts the capacity to jointly optimize all parameters. Although Bayesian optimization (BO) has been explored as an alternative search strategy to identify well-optimized CG parameters, its application has conventionally been limited to low-dimensional scenarios. This has contributed to the assumption that BO is unsuitable for more complex CG models, which often involve a large number of parameters. In this study, we challenge this assumption by successfully extending BO, using the tree-structured Parzen estimator (TPE) model, to optimize a high-dimensional CG model. Specifically, we show that a 41-parameter CG model of Pebax-1657, a copolymer composed of alternating polyamide and polyether segments, can be effectively parametrized using BO, resulting in a model that accurately reproduces the key physical properties of its parent atomistic representation. Our optimization framework simultaneously targets structural and thermodynamic properties, namely, density, radius of gyration, and glass transition temperature. Compared to traditional search algorithms, BO-TPE not only converges faster but also delivers consistent improvements over more standard parametrization approaches.

## 摘要（中文）
粗粒化力场模型因其可扩展性在材料模拟中被广泛应用。传统参数化方法采用混合策略，顺序整合自上而下和自下而上的方法，限制了全局联合优化的能力。本研究成功将贝叶斯优化（BO）与树结构Parzen估计器（TPE）模型扩展到高维粗粒化模型，对含有41个参数的Pebax-1657共聚物模型进行参数化。该方法同时优化密度、回转半径和玻璃转变温度，相比传统搜索算法收敛速度更快，参数化效果更优。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](https://app.acspubs.org/e/er?s=1913652004&lid=109588&pci=CACSR000013623915&elqTrackId=b1a26c2857424180b9083642f357dc95&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF5E85ED303AD08530CE3111AC129C7E830DF669D1886211F10624EBC003E655BFD)
