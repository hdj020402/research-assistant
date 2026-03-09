---
title: "SPECTRE: A Multimodal Spectral Transformer for Small Molecule Annotation"
title_zh: "SPECTRE: 用于小分子注释的多模态光谱变换器"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02444"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnP-2FQKzJF3jdcipkoTDwxrK4TgrpX4J86PaD4PwkiIq-2FJN6oPU5Tq2FkAJ3QwkB6eXrLDn1nmTkZy6-2Bes9zPNT1NVd-2FpnNgmvTsp2aZ7yrj8hRiIX-2FPcbBa2TuGa7-2FD4dCacJX__lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBVTnY3-2Bk3fXXQ8MPUwtpjKFNZjsiwyNBegON6s0tw7ZIi14ZhEUWnOnsdgApXAGcVS23xG3G7UFpX7JhwaYm6OoRtE-2FoxJ-2FlzNhlGXs7Z82e6F6c1tQeP0ESFsNr7HZzmC-2BiZKTIxoAa4WmkLh13cM99Gq1eyzvQuw6snjsWZ7IgUjdo5hYvcuiZIWGWVp0LI-3D"
pub_date: ""
tags: ["deep-learning", "transformer-model", "nmr-spectroscopy", "structure-elucidation", "molecular-fingerprinting"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# SPECTRE: A Multimodal Spectral Transformer for Small Molecule Annotation

**SPECTRE: 用于小分子注释的多模态光谱变换器**

## 精华总结
SPECTRE是一个基于transformer的最先进模型，用于结构去重复和注释，接受多种NMR数据类型实现灵活注释，并采用新颖的熵优化无碰撞分子二进制指纹提高候选分子检索精度。

**关键词**: NMR光谱、Transformer模型、结构注释、分子指纹、自然产物

## 摘要（英文）
Development of new pharmaceuticals such as penicillin and numerous anticancer compounds often begins with the discovery and characterization of natural products (NPs). Nuclear magnetic resonance (NMR) spectroscopy is an essential tool for elucidating the chemical structure of NPs. However, interpreting NMR spectra is a time-consuming process that requires considerable domain expertise. This has led to the development of computational tools that directly annotate structures from NMR spectra, accelerating this elucidation and discovery process. Here we introduce SPECTRE, a state-of-the-art transformer-based model for structure dereplication and annotation. Key contributions of this tool include (1) a novel, transformer-based structure annotation method that accepts several types of NMR data for flexible annotation; (2) a novel, entropy-optimized, and collision-free molecular binary fingerprint that enhances the accuracy when retrieving molecular candidates. SPECTRE achieves a new state of the art 80% top-1 annotation accuracy using a challenging search space of 526,163 molecules. SPECTRE is also the first tool to provide fine-grained similarity maps between predicted and retrieved structures. These maps enable substructure-level interpretation, offering interpretable visual cues that highlight matched chemical fragments. Even in cases where overall molecular similarity is low, these fragment-level hints offer valuable insights to chemists, guiding hypothesis generation and accelerating the structure elucidation process.

## 摘要（中文）
新药物如青霉素和许多抗癌化合物的开发通常始于天然产物 (np) 的发现和表征。核磁共振 (NMR) 光谱是阐明NPs化学结构的重要工具。然而，解释NMR光谱是一个耗时的过程，需要相当多的领域专业知识。这导致了直接从NMR光谱注释结构的计算工具的发展，加速了这一阐明和发现过程。在这里，我们介绍SPECTRE，这是一种基于最先进的变压器的模型，用于结构的复制和注释。该工具的主要贡献包括 (1) 一种新颖的基于转换器的结构注释方法，该方法接受几种类型的NMR数据以进行灵活的注释; (2) 一种新颖的，熵优化的，无碰撞的分子二进制指纹，可提高检索分子候选物时的准确性。SPECTRE使用具有挑战性的526,163分子搜索空间实现了80% top-1注释精度的最新技术。SPECTRE也是第一个在预测和检索结构之间提供细粒度相似性映射的工具。这些地图可以实现子结构级别的解释，提供可解释的视觉线索，突出显示匹配的化学片段。即使在总体分子相似性较低的情况下，这些片段级提示也为化学家提供了有价值的见解，指导了假设的产生并加速了结构阐明过程。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnP-2FQKzJF3jdcipkoTDwxrK4TgrpX4J86PaD4PwkiIq-2FJN6oPU5Tq2FkAJ3QwkB6eXrLDn1nmTkZy6-2Bes9zPNT1NVd-2FpnNgmvTsp2aZ7yrj8hRiIX-2FPcbBa2TuGa7-2FD4dCacJX__lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBVTnY3-2Bk3fXXQ8MPUwtpjKFNZjsiwyNBegON6s0tw7ZIi14ZhEUWnOnsdgApXAGcVS23xG3G7UFpX7JhwaYm6OoRtE-2FoxJ-2FlzNhlGXs7Z82e6F6c1tQeP0ESFsNr7HZzmC-2BiZKTIxoAa4WmkLh13cM99Gq1eyzvQuw6snjsWZ7IgUjdo5hYvcuiZIWGWVp0LI-3D)
