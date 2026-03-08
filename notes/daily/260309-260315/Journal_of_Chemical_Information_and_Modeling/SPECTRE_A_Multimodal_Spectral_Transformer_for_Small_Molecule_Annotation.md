---
title: "SPECTRE: A Multimodal Spectral Transformer for Small Molecule Annotation"
title_zh: "SPECTRE：用于小分子注解的多模态光谱变换器"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02444"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnP-2FQKzJF3jdcipkoTDwxrK4TgrpX4J86PaD4PwkiIq-2FJN6oPU5Tq2FkAJ3QwkB6eXrLDn1nmTkZy6-2Bes9zPNT1NVd-2FpnNgmvTsp2aZ7yrj8hRiIX-2FPcbBa2TuGa7-2FD4dCacJX__lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBVTnY3-2Bk3fXXQ8MPUwtpjKFNZjsiwyNBegON6s0tw7ZIi14ZhEUWnOnsdgApXAGcVS23xG3G7UFpX7JhwaYm6OoRtE-2FoxJ-2FlzNhlGXs7Z82e6F6c1tQeP0ESFsNr7HZzmC-2BiZKTIxoAa4WmkLh13cM99Gq1eyzvQuw6snjsWZ7IgUjdo5hYvcuiZIWGWVp0LI-3D"
pub_date: ""
tags: ["transformer-models", "nmr-spectroscopy", "structure-prediction", "molecular-fingerprints", "deep-learning"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# SPECTRE: A Multimodal Spectral Transformer for Small Molecule Annotation

**SPECTRE：用于小分子注解的多模态光谱变换器**

## 精华总结
SPECTRE是一种最先进的基于变换器的模型，用于结构去重和注解，采用熵优化的分子指纹和细粒度相似性图谱实现可解释的结构预测。

**关键词**: 变换器模型、NMR光谱、结构注解、分子指纹、深度学习

## 摘要（英文）
Development of new pharmaceuticals such as penicillin and numerous anticancer compounds often begins with the discovery and characterization of natural products (NPs). Nuclear magnetic resonance (NMR) spectroscopy is an essential tool for elucidating the chemical structure of NPs. However, interpreting NMR spectra is a time-consuming process that requires considerable domain expertise. This has led to the development of computational tools that directly annotate structures from NMR spectra, accelerating this elucidation and discovery process. Here we introduce SPECTRE, a state-of-the-art transformer-based model for structure dereplication and annotation. Key contributions of this tool include (1) a novel, transformer-based structure annotation method that accepts several types of NMR data for flexible annotation; (2) a novel, entropy-optimized, and collision-free molecular binary fingerprint that enhances the accuracy when retrieving molecular candidates. SPECTRE achieves a new state of the art 80% top-1 annotation accuracy using a challenging search space of 526,163 molecules. SPECTRE is also the first tool to provide fine-grained similarity maps between predicted and retrieved structures. These maps enable substructure-level interpretation, offering interpretable visual cues that highlight matched chemical fragments. Even in cases where overall molecular similarity is low, these fragment-level hints offer valuable insights to chemists, guiding hypothesis generation and accelerating the structure elucidation process.

## 摘要（中文）
本文介绍SPECTRE，一种基于变换器的最先进模型，用于结构去重和注解。该工具在526,163个分子的具有挑战性的搜索空间中实现了80%的顶级注解准确率。SPECTRE采用新颖的熵优化无碰撞分子二进制指纹，并提供细粒度相似性图谱，实现亚结构级解释，为化学家提供可视化提示，加速天然产物NMR光谱的结构解析过程。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnP-2FQKzJF3jdcipkoTDwxrK4TgrpX4J86PaD4PwkiIq-2FJN6oPU5Tq2FkAJ3QwkB6eXrLDn1nmTkZy6-2Bes9zPNT1NVd-2FpnNgmvTsp2aZ7yrj8hRiIX-2FPcbBa2TuGa7-2FD4dCacJX__lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBVTnY3-2Bk3fXXQ8MPUwtpjKFNZjsiwyNBegON6s0tw7ZIi14ZhEUWnOnsdgApXAGcVS23xG3G7UFpX7JhwaYm6OoRtE-2FoxJ-2FlzNhlGXs7Z82e6F6c1tQeP0ESFsNr7HZzmC-2BiZKTIxoAa4WmkLh13cM99Gq1eyzvQuw6snjsWZ7IgUjdo5hYvcuiZIWGWVp0LI-3D)
