---
title: "PeptideNet: An Integrative Deep Learning Framework for Predicting Diverse Bioactive Peptides Using Protein Language Model Embeddings"
title_zh: "PeptideNet：整合蛋白质语言模型嵌入的深度学习框架用于预测多种生物活性肽"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02885"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPbvzMOM1MpReAto2GblfQhtOr2f4eUrcDK8GgYrUaVB4hQU644yTwSiGD0hl0vCE2t-2FI-2B1BgFYncIEd5s0YHuzbPf5VjilF6LKAgLc2TwsXqysEjePtcJR4z0LNIsIQ8AUzqk_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FDyk2GK4Jr1RI35MFP7JouLeH8NU-2Bepff-2F3vjuep3GqUdeVFdTfbR36mtu7mGH8IIQCO9knnyttBrypLpokXKNsXIGeJOqoyPPZ-2Ft-2FGYSBiO-2FYkx1bqqdUwc-2BqehwxuC06eElSXrWvvquCh3ikNLnR5c-2B9PTdI3c-2FWtIFe9GHGTfPZnH-2B7DNJfElbNo10-2FTgiI-3D"
pub_date: ""
tags: ["deep-learning", "protein-language-models", "peptide-prediction", "bioactivity-prediction", "drug-discovery"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# PeptideNet: An Integrative Deep Learning Framework for Predicting Diverse Bioactive Peptides Using Protein Language Model Embeddings

**PeptideNet：整合蛋白质语言模型嵌入的深度学习框架用于预测多种生物活性肽**

## 精华总结
大型蛋白质语言模型嵌入与PeptideNet架构的整合实现了对全局语境信息和残基水平特征的有效捕获，为多种生物活性肽预测建立了一个通用且可解释的框架。

**关键词**: 生物活性肽、蛋白质语言模型、深度学习、生物信息学、药物发现

## 摘要（英文）
Bioactive peptides are multifunctional biomolecules composed of short amino acid sequences that exhibit diverse biological activities, including antioxidative, antihemolytic, anticell-penetrating, antiviral, and antimicrobial effects. Accurate computational prediction of peptide bioactivity is essential for accelerating the discovery and design of peptide-based therapeutics. In this study, we investigated five categories of bioactive peptides using four distinct feature representations, including large protein language model embeddings (ESM1, ESM2, and ProtBert) and physicochemical descriptors. A total of 20 hybrid deep learning models integrating Convolutional Neural Networks (CNNs) and Bidirectional Gated Recurrent Units (BiGRUs) were developed to capture both local sequence motifs and long-range dependencies. The proposed PeptideNet model achieved robust predictive performance, with accuracies of 0.83, 0.87, 0.89, 0.92, and 0.94 for antioxidative, antihemolytic, anticell-penetrating, antiviral, and antimicrobial peptides, respectively, on the independent data set. Among the evaluated feature sets, ESM-2 embeddings consistently outperformed others across all peptide types, providing rich contextual and evolutionary information. Furthermore, t-SNE visualization of learned representations demonstrated effective generalization across peptide classes, while positional sequence logo analysis revealed conserved residue patterns contributing to peptide bioactivity. The integration of large protein language model embeddings with the PeptideNet architecture enables the model to capture both global contextual information and residue-level features, establishing a generalized and interpretable framework for multipeptide bioactivity prediction.

## 摘要（中文）
本研究开发了PeptideNet深度学习框架，用于预测五类生物活性肽的多种功能。该框架整合了蛋白质语言模型嵌入（ESM1、ESM2、ProtBert）和物理化学描述符，采用CNN-BiGRU混合模型架构来捕获序列局部基序和长程依赖关系。在独立测试集上，PeptideNet对抗氧化肽、溶血肽、细胞穿透肽、抗病毒肽和抗菌肽的预测准确率分别达到0.83、0.87、0.89、0.92和0.94。ESM-2嵌入在所有肽类型中表现最优，为模型提供丰富的进化和语境信息。该框架为多肽生物活性预测建立了通用且可解释的方法。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPbvzMOM1MpReAto2GblfQhtOr2f4eUrcDK8GgYrUaVB4hQU644yTwSiGD0hl0vCE2t-2FI-2B1BgFYncIEd5s0YHuzbPf5VjilF6LKAgLc2TwsXqysEjePtcJR4z0LNIsIQ8AUzqk_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FDyk2GK4Jr1RI35MFP7JouLeH8NU-2Bepff-2F3vjuep3GqUdeVFdTfbR36mtu7mGH8IIQCO9knnyttBrypLpokXKNsXIGeJOqoyPPZ-2Ft-2FGYSBiO-2FYkx1bqqdUwc-2BqehwxuC06eElSXrWvvquCh3ikNLnR5c-2B9PTdI3c-2FWtIFe9GHGTfPZnH-2B7DNJfElbNo10-2FTgiI-3D)
