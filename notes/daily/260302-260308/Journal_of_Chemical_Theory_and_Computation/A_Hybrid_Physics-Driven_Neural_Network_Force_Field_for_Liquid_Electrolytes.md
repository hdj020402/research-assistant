---
title: "A Hybrid Physics-Driven Neural Network Force Field for Liquid Electrolytes"
title_zh: "用于液体电解质的混合物理驱动神经网络力场"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c02100"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE12QfciIZkxKQch3GRPSBJ6NHXl-2BQhbBarlxYTZ8rCbijxOdkcURwaMrl3iG7RxxSw4PO77NZJ2UJp0LtPriOMrQ7qDs5V2MP30-2Flbv1xA9XrqnvGamN0CAi6JrOIfr3QyNYWt_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjW7AaooT4Kl7cFUzD7LieLOKneDI-2B5uQ7uNzJXnkKHZ0OOapcnIwBC8-2BH3YMQT-2FpdU-2F9yl-2BwuUwnOk5UlmVY3XSPoww-2F0hjBS7VXjuGIOVk4YTmtqngN1u-2Bk-2F1hwyqXghQo-2FRdXmBruPElx5jr3tr4mFgXZlpnSnrI1Tb-2F-2BxMC2tZ9ezmNkYOP0e2wM7Uv2zbZZoCVHOY8ZoLpuUo5mk877NvbR-2F-2Fz-2FEIneY-2F7E1TOhE-3D"
pub_date: ""
tags: ["machine-learning", "force-field", "electrolyte-design", "neural-networks", "molecular-simulation"]
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
本研究提出PhyNEO-Electrolyte方法，通过物理驱动和数据驱动混合策略构建力场，仅需单体和二聚体EDA数据即可实现对电解质系统的高精度描述，显著提高了机器学习原子间势的数据效率和化学空间覆盖范围。

**关键词**: 混合物理驱动神经网络、机器学习原子间势、电解质设计、力场、能量分解分析

## 摘要（英文）
Electrolyte design plays an important role in the development of lithium-ion batteries and sodium-ion batteries. Battery electrolytes feature a large design space composed of different solvents, additives, and salts, which is difficult to explore experimentally. High-fidelity molecular simulation can accurately predict the bulk properties of electrolytes by employing accurate potential energy surfaces, thus guiding the molecule and formula engineering. At present, the overly simplified classic force fields rely heavily on experimental data for fine-tuning, thus its predictive power on microscopic level is under question. In contrast, the newly emerged machine learning interatomic potential (MLIP) can accurately reproduce the ab initio data, demonstrating excellent fitting ability. However, it is still haunted by problems such as low transferability, insufficient stability in the prediction of bulk properties, and poor training cost scaling. Therefore, it cannot yet be used as a robust and universal tool for the exploration of electrolyte design space. In this work, we introduce a highly scalable and fully bottom-up force field construction strategy called PhyNEO-Electrolyte. It adopts a hybrid physics-driven and data-driven method that relies only on monomer and dimer EDA (energy decomposition analysis) data. With a careful separation of long/short-range and nonbonding/bonding interactions, we rigorously restore the long-range asymptotic behavior, which is critical in the description of electrolyte systems. Through this approach, we significantly improve the data efficiency of MLIP training, allowing us to achieve much larger chemical space coverage using much less data while retaining reliable quantitative prediction power in bulk phase calculations. PhyNEO-Electrolyte thus serves as an important tool for future electrolyte optimization.

## 摘要（中文）
电解质设计在锂离子电池和钠离子电池的发展中起着重要作用。电池电解液的特点是由不同的溶剂，添加剂和盐组成的大设计空间，这很难通过实验进行探索。高保真分子模拟可以通过使用精确的势能表面来准确预测电解质的整体性质，从而指导分子和配方工程。目前，过于简化的经典力场在很大程度上依赖于实验数据进行微调，因此其在微观水平上的预测能力受到质疑。相比之下，新出现的机器学习原子间势 (mlp) 可以准确地再现从头算数据，显示出出色的拟合能力。但是，它仍然存在诸如可转移性低，整体性能预测稳定性不足以及训练成本缩放性差等问题。因此，它还不能用作探索电解质设计空间的强大且通用的工具。在这项工作中，我们引入了一种高度可扩展且完全自下而上的力场构建策略，称为PhyNEO-电解质。它采用混合物理驱动和数据驱动的方法，该方法仅依赖于单体和二聚体EDA (能量分解分析) 数据。通过仔细分离长/短程和非键合/键合相互作用，我们严格恢复了长程渐近行为，这对于描述电解质系统至关重要。通过这种方法，我们显着提高了mlp训练的数据效率，使我们能够使用更少的数据实现更大的化学空间覆盖，同时在体相计算中保留可靠的定量预测能力。因此，PhyNEO电解质是未来电解质优化的重要工具。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE12QfciIZkxKQch3GRPSBJ6NHXl-2BQhbBarlxYTZ8rCbijxOdkcURwaMrl3iG7RxxSw4PO77NZJ2UJp0LtPriOMrQ7qDs5V2MP30-2Flbv1xA9XrqnvGamN0CAi6JrOIfr3QyNYWt_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjW7AaooT4Kl7cFUzD7LieLOKneDI-2B5uQ7uNzJXnkKHZ0OOapcnIwBC8-2BH3YMQT-2FpdU-2F9yl-2BwuUwnOk5UlmVY3XSPoww-2F0hjBS7VXjuGIOVk4YTmtqngN1u-2Bk-2F1hwyqXghQo-2FRdXmBruPElx5jr3tr4mFgXZlpnSnrI1Tb-2F-2BxMC2tZ9ezmNkYOP0e2wM7Uv2zbZZoCVHOY8ZoLpuUo5mk877NvbR-2F-2Fz-2FEIneY-2F7E1TOhE-3D)
