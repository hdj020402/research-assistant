---
title: "A Hybrid Physics-Driven Neural Network Force Field for Liquid Electrolytes"
title_zh: "用于液体电解质的混合物理驱动神经网络力场"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c02100"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE12QfciIZkxKQch3GRPSBJ6NHXl-2BQhbBarlxYTZ8rCbijxOdkcURwaMrl3iG7RxxSw4PO77NZJ2UJp0LtPriOMrQ7qDs5V2MP30-2Flbv1xA9XrqnvGamN0CAi6JrOIfr3QyNYWt_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjW7AaooT4Kl7cFUzD7LieLOKneDI-2B5uQ7uNzJXnkKHZ0OOapcnIwBC8-2BH3YMQT-2FpdU-2F9yl-2BwuUwnOk5UlmVY3XSPoww-2F0hjBS7VXjuGIOVk4YTmtqngN1u-2Bk-2F1hwyqXghQo-2FRdXmBruPElx5jr3tr4mFgXZlpnSnrI1Tb-2F-2BxMC2tZ9ezmNkYOP0e2wM7Uv2zbZZoCVHOY8ZoLpuUo5mk877NvbR-2F-2Fz-2FEIneY-2F7E1TOhE-3D"
pub_date: ""
tags: ["neural-network-potential", "force-field", "electrolyte-design", "machine-learning-interatomic-potential", "physics-informed-ml"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# A Hybrid Physics-Driven Neural Network Force Field for Liquid Electrolytes

**用于液体电解质的混合物理驱动神经网络力场**

## 精华总结
本工作提出PhyNEO-Electrolyte方法，结合物理驱动和数据驱动的混合策略，通过仅依赖单体和二聚体能量分解分析数据，显著改进了机器学习原子间势的数据效率和可迁移性，实现了对电解质体相性质的可靠预测。该方法为电解质设计空间的探索提供了通用工具，突破了传统力场和现有机器学习势函数的局限。

**关键词**: 混合物理驱动神经网络、机器学习原子间势、电解质设计、力场开发、能量分解分析

## 摘要（英文）
Electrolyte design plays an important role in the development of lithium-ion batteries and sodium-ion batteries. Battery electrolytes feature a large design space composed of different solvents, additives, and salts, which is difficult to explore experimentally. High-fidelity molecular simulation can accurately predict the bulk properties of electrolytes by employing accurate potential energy surfaces, thus guiding the molecule and formula engineering. At present, the overly simplified classic force fields rely heavily on experimental data for fine-tuning, thus its predictive power on microscopic level is under question. In contrast, the newly emerged machine learning interatomic potential (MLIP) can accurately reproduce the ab initio data, demonstrating excellent fitting ability. However, it is still haunted by problems such as low transferability, insufficient stability in the prediction of bulk properties, and poor training cost scaling. Therefore, it cannot yet be used as a robust and universal tool for the exploration of electrolyte design space. In this work, we introduce a highly scalable and fully bottom-up force field construction strategy called PhyNEO-Electrolyte. It adopts a hybrid physics-driven and data-driven method that relies only on monomer and dimer EDA (energy decomposition analysis) data. With a careful separation of long/short-range and nonbonding/bonding interactions, we rigorously restore the long-range asymptotic behavior, which is critical in the description of electrolyte systems. Through this approach, we significantly improve the data efficiency of MLIP training, allowing us to achieve much larger chemical space coverage using much less data while retaining reliable quantitative prediction power in bulk phase calculations. PhyNEO-Electrolyte thus serves as an important tool for future electrolyte optimization.

## 摘要（中文）
电解液设计在锂离子电池和钠离子电池的发展中发挥着重要作用。电池电解液具有由不同溶剂、添加剂和盐类组成的广阔设计空间，而这一空间在实验上难以充分探索。高保真分子模拟通过采用精确的势能面，能够准确预测电解质的宏观性质，从而指导分子设计和配方优化。目前，过于简化的经典力场在参数微调过程中严重依赖实验数据，因此其在微观尺度上的预测能力备受质疑。相比之下，新近提出的机器学习原子间势能函数（MLIP）能够精确地复现从头计算数据，展现出优异的拟合能力。然而，它仍然受到诸如迁移性低、对体相性质的预测稳定性不足以及训练成本扩展性差等问题的困扰。因此，它目前还不能作为探索电解液设计空间的稳健且通用的工具。在本工作中，我们提出了一种高度可扩展且完全自下而上的力场构建策略，称为PhyNEO-电解质。该方法采用混合的物理驱动与数据驱动相结合的策略，仅依赖单体和二聚体的EDA（能量分解分析）数据。通过细致地区分长程/短程相互作用以及非键合/键合相互作用，我们严格恢复了长程渐近行为，而这一行为对于电解质体系的描述至关重要。通过这种方法，我们显著提升了MLIP训练的数据效率，在使用更少数据的情况下实现了对更大化学空间的覆盖，同时在体相计算中仍能保持可靠的定量预测能力。因此，PhyNEO-电解液已成为未来电解液优化的重要工具。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE12QfciIZkxKQch3GRPSBJ6NHXl-2BQhbBarlxYTZ8rCbijxOdkcURwaMrl3iG7RxxSw4PO77NZJ2UJp0LtPriOMrQ7qDs5V2MP30-2Flbv1xA9XrqnvGamN0CAi6JrOIfr3QyNYWt_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjW7AaooT4Kl7cFUzD7LieLOKneDI-2B5uQ7uNzJXnkKHZ0OOapcnIwBC8-2BH3YMQT-2FpdU-2F9yl-2BwuUwnOk5UlmVY3XSPoww-2F0hjBS7VXjuGIOVk4YTmtqngN1u-2Bk-2F1hwyqXghQo-2FRdXmBruPElx5jr3tr4mFgXZlpnSnrI1Tb-2F-2BxMC2tZ9ezmNkYOP0e2wM7Uv2zbZZoCVHOY8ZoLpuUo5mk877NvbR-2F-2Fz-2FEIneY-2F7E1TOhE-3D)
