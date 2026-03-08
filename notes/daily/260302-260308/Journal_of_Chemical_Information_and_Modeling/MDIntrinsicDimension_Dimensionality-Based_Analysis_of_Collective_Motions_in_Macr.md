---
title: "MDIntrinsicDimension: Dimensionality-Based Analysis of Collective Motions in Macromolecules from Molecular Dynamics Trajectories"
title_zh: "MDIntrinsicDimension：从分子动力学轨迹分析大分子集体运动的维度方法"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02716"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPFfeHtP5KW830HGm8QaNSP4cZ03Z7emEFq6FEV8Z6GprJ6C6dxUGbwLUoart-2F1p-2BLiEIcsybtsdcDOISlL1vp31ImhZLmynSnrb9z-2FPWwSoVnj-2FrxAAKJOv-2BurNarhzvzvrVC_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FDjjO9MD0Eh7xaZBZ4hbuJTF6KwpQO9fPtwAqW81e2UFKRM3qHxZtHrQQrIvN1sMQlcMWH4oFA-2BvekTtoqnWLMHcCtWaeTxyQY9FoIwDyo-2F3Q8UicosntKycx-2F2IIolcrDCR9TlUnQq0JUHIylT9EkA4MIpCrYYlPJNgB2rjgGOkLmjr4bflFKbSpzFW3bzWQI-3D"
pub_date: ""
tags: ["molecular-dynamics", "dimensionality-reduction", "intrinsic-dimension", "protein-dynamics", "computational-chemistry"]
ai_relevance: 3
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# MDIntrinsicDimension: Dimensionality-Based Analysis of Collective Motions in Macromolecules from Molecular Dynamics Trajectories

**MDIntrinsicDimension：从分子动力学轨迹分析大分子集体运动的维度方法**

## 精华总结
MDIntrinsicDimension是一个开源Python包，通过将旋转和平移不变的分子投影与最先进的估计器相结合，直接从分子动力学轨迹估计固有维数，可以突出空间局部灵活性、区分结构片段并识别亚稳定构象。

**关键词**: 分子动力学、固有维数、维度分析、生物分子动力学、蛋白质折叠

## 摘要（英文）
Molecular dynamics (MD) simulations provide atomistic insights into the structure, dynamics, and function of biomolecules by generating time-resolved, high-dimensional trajectories. Analyzing such data benefits from estimating the minimal number of variables required to describe the explored conformational manifold, known as the intrinsic dimension (ID). We present MDIntrinsicDimension, an open-source Python package that estimates ID directly from MD trajectories by combining rotation- and translation-invariant molecular projections with state-of-the-art estimators. The package provides three complementary analysis modes: whole-molecule ID, sliding windows along the sequence, and per-secondary-structure elements. It computes both overall ID (a single summary value) and instantaneous, time-resolved ID that can reveal transitions and heterogeneity over time. We illustrate the approach on fast folding-unfolding trajectories from the DESRES dataset, demonstrating that ID complements conventional geometric descriptors by highlighting spatially localized flexibility, differentiating structural segments, and identifying a metastable configuration.

## 摘要（中文）
分子动力学(MD)模拟通过生成时间分辨的高维轨迹，为生物分子的结构、动力学和功能提供原子水平的洞察。分析此类数据受益于估计描述所探索构象流形所需的最少变量数，这被称为固有维数(ID)。我们提出了MDIntrinsicDimension，一个开源Python包，通过将旋转和平移不变的分子投影与最先进的估计器相结合，直接从MD轨迹估计ID。该包提供三种互补的分析模式：整体分子ID、沿序列的滑动窗口和每个二级结构元素的ID。它计算总体ID(单个汇总值)和瞬时的、时间分辨的ID，可以揭示时间内的转变和异质性。我们在来自DESRES数据集的快速折叠-展开轨迹上演示了该方法，证明ID通过突出空间局部灵活性、区分结构片段和识别亚稳定构象，补充了传统几何描述符。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPFfeHtP5KW830HGm8QaNSP4cZ03Z7emEFq6FEV8Z6GprJ6C6dxUGbwLUoart-2F1p-2BLiEIcsybtsdcDOISlL1vp31ImhZLmynSnrb9z-2FPWwSoVnj-2FrxAAKJOv-2BurNarhzvzvrVC_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FDjjO9MD0Eh7xaZBZ4hbuJTF6KwpQO9fPtwAqW81e2UFKRM3qHxZtHrQQrIvN1sMQlcMWH4oFA-2BvekTtoqnWLMHcCtWaeTxyQY9FoIwDyo-2F3Q8UicosntKycx-2F2IIolcrDCR9TlUnQq0JUHIylT9EkA4MIpCrYYlPJNgB2rjgGOkLmjr4bflFKbSpzFW3bzWQI-3D)
