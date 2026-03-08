---
title: "SPECTRE: A Multimodal Spectral Transformer for Small Molecule Annotation"
title_zh: "SPECTRE: 小分子注释的多模态光谱Transformer"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02444"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnP-2FQKzJF3jdcipkoTDwxrK4TgrpX4J86PaD4PwkiIq-2FJN6oPU5Tq2FkAJ3QwkB6eXrLDn1nmTkZy6-2Bes9zPNT1NVd-2FpnNgmvTsp2aZ7yrj8hRiIX-2FPcbBa2TuGa7-2FD4dCacJX__lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBVTnY3-2Bk3fXXQ8MPUwtpjKFNZjsiwyNBegON6s0tw7ZIi14ZhEUWnOnsdgApXAGcVS23xG3G7UFpX7JhwaYm6OoRtE-2FoxJ-2FlzNhlGXs7Z82e6F6c1tQeP0ESFsNr7HZzmC-2BiZKTIxoAa4WmkLh13cM99Gq1eyzvQuw6snjsWZ7IgUjdo5hYvcuiZIWGWVp0LI-3D"
pub_date: ""
tags: ["deep-learning", "spectroscopy-analysis", "molecule-annotation", "transformer-models", "drug-discovery"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# SPECTRE: A Multimodal Spectral Transformer for Small Molecule Annotation

**SPECTRE: 小分子注释的多模态光谱Transformer**

## 精华总结
SPECTRE是一个最先进的基于Transformer的模型,用于结构去重复和注释,采用新颖的多模态NMR数据处理方法和熵优化分子指纹技术,实现了80%的顶-1注释准确率,并提供可解释的子结构相似性可视化。

**关键词**: Transformer、NMR光谱、结构注释、分子指纹、自然产物

## 摘要（英文）
Development of new pharmaceuticals such as penicillin and numerous anticancer compounds often begins with the discovery and characterization of natural products (NPs). Nuclear magnetic resonance (NMR) spectroscopy is an essential tool for elucidating the chemical structure of NPs. However, interpreting NMR spectra is a time-consuming process that requires considerable domain expertise. This has led to the development of computational tools that directly annotate structures from NMR spectra, accelerating this elucidation and discovery process. Here we introduce SPECTRE, a state-of-the-art transformer-based model for structure dereplication and annotation. Key contributions of this tool include (1) a novel, transformer-based structure annotation method that accepts several types of NMR data for flexible annotation; (2) a novel, entropy-optimized, and collision-free molecular binary fingerprint that enhances the accuracy when retrieving molecular candidates. SPECTRE achieves a new state of the art 80% top-1 annotation accuracy using a challenging search space of 526,163 molecules. SPECTRE is also the first tool to provide fine-grained similarity maps between predicted and retrieved structures. These maps enable substructure-level interpretation, offering interpretable visual cues that highlight matched chemical fragments. Even in cases where overall molecular similarity is low, these fragment-level hints offer valuable insights to chemists, guiding hypothesis generation and accelerating the structure elucidation process.

## 摘要（中文）
新型药物(如青霉素和众多抗癌化合物)的开发通常始于天然产物(NPs)的发现和表征。核磁共振(NMR)波谱学是阐明天然产物化学结构的重要工具。然而,解释NMR光谱是一个耗时的过程,需要相当的领域专业知识。这导致了计算工具的开发,这些工具直接从NMR光谱注释结构,加快了这一阐明和发现过程。在这里,我们介绍了SPECTRE,这是一个最先进的基于Transformer的模型,用于结构去重复和注释。该工具的主要贡献包括:(1)一种新颖的、基于Transformer的结构注释方法,接受多种类型的NMR数据以实现灵活注释;(2)一种新颖的、熵优化的、无碰撞的分子二进制指纹,增强了检索分子候选物时的准确性。SPECTRE使用526,163个分子的具有挑战性的搜索空间实现了80%的最新技术顶-1注释准确率。SPECTRE也是第一个提供预测结构和检索结构之间精细相似性图的工具。这些图使能子结构级别的解释,提供突出匹配化学片段的可解释的视觉线索。即使在整体分子相似性较低的情况下,这些片段级别的提示也为化学家提供了宝贵的见解,指导假设生成并加快结构阐明过程。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnP-2FQKzJF3jdcipkoTDwxrK4TgrpX4J86PaD4PwkiIq-2FJN6oPU5Tq2FkAJ3QwkB6eXrLDn1nmTkZy6-2Bes9zPNT1NVd-2FpnNgmvTsp2aZ7yrj8hRiIX-2FPcbBa2TuGa7-2FD4dCacJX__lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBVTnY3-2Bk3fXXQ8MPUwtpjKFNZjsiwyNBegON6s0tw7ZIi14ZhEUWnOnsdgApXAGcVS23xG3G7UFpX7JhwaYm6OoRtE-2FoxJ-2FlzNhlGXs7Z82e6F6c1tQeP0ESFsNr7HZzmC-2BiZKTIxoAa4WmkLh13cM99Gq1eyzvQuw6snjsWZ7IgUjdo5hYvcuiZIWGWVp0LI-3D)
