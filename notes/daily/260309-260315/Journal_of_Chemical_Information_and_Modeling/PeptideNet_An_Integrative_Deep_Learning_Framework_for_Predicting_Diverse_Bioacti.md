---
title: "PeptideNet: An Integrative Deep Learning Framework for Predicting Diverse Bioactive Peptides Using Protein Language Model Embeddings"
title_zh: "PeptideNet：基于蛋白质语言模型嵌入的生物活性肽多样性预测的综合深度学习框架"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02885"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPbvzMOM1MpReAto2GblfQhtOr2f4eUrcDK8GgYrUaVB4hQU644yTwSiGD0hl0vCE2t-2FI-2B1BgFYncIEd5s0YHuzbPf5VjilF6LKAgLc2TwsXqysEjePtcJR4z0LNIsIQ8AUzqk_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FDyk2GK4Jr1RI35MFP7JouLeH8NU-2Bepff-2F3vjuep3GqUdeVFdTfbR36mtu7mGH8IIQCO9knnyttBrypLpokXKNsXIGeJOqoyPPZ-2Ft-2FGYSBiO-2FYkx1bqqdUwc-2BqehwxuC06eElSXrWvvquCh3ikNLnR5c-2B9PTdI3c-2FWtIFe9GHGTfPZnH-2B7DNJfElbNo10-2FTgiI-3D"
pub_date: ""
tags: ["deep-learning", "protein-language-models", "peptide-prediction", "bioactivity-prediction", "neural-networks"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# PeptideNet: An Integrative Deep Learning Framework for Predicting Diverse Bioactive Peptides Using Protein Language Model Embeddings

**PeptideNet：基于蛋白质语言模型嵌入的生物活性肽多样性预测的综合深度学习框架**

## 精华总结
大型蛋白质语言模型嵌入与PeptideNet架构的整合使得模型能够捕获全局上下文信息和残基级特征，为多肽生物活性预测建立了一个泛化和可解释的框架。

**关键词**: 生物活性肽、深度学习、蛋白质语言模型、生物信息学、肽设计

## 摘要（英文）
Bioactive peptides are multifunctional biomolecules composed of short amino acid sequences that exhibit diverse biological activities, including antioxidative, antihemolytic, anticell-penetrating, antiviral, and antimicrobial effects. Accurate computational prediction of peptide bioactivity is essential for accelerating the discovery and design of peptide-based therapeutics. In this study, we investigated five categories of bioactive peptides using four distinct feature representations, including large protein language model embeddings (ESM1, ESM2, and ProtBert) and physicochemical descriptors. A total of 20 hybrid deep learning models integrating Convolutional Neural Networks (CNNs) and Bidirectional Gated Recurrent Units (BiGRUs) were developed to capture both local sequence motifs and long-range dependencies. The proposed PeptideNet model achieved robust predictive performance, with accuracies of 0.83, 0.87, 0.89, 0.92, and 0.94 for antioxidative, antihemolytic, anticell-penetrating, antiviral, and antimicrobial peptides, respectively, on the independent data set. Among the evaluated feature sets, ESM-2 embeddings consistently outperformed others across all peptide types, providing rich contextual and evolutionary information. Furthermore, t-SNE visualization of learned representations demonstrated effective generalization across peptide classes, while positional sequence logo analysis revealed conserved residue patterns contributing to peptide bioactivity. The integration of large protein language model embeddings with the PeptideNet architecture enables the model to capture both global contextual information and residue-level features, establishing a generalized and interpretable framework for multipeptide bioactivity prediction.

## 摘要（中文）
本研究开发了PeptideNet框架，用于预测包括抗氧化、抗溶血、抗细胞穿透、抗病毒和抗菌等五类生物活性肽。模型采用蛋白质语言模型嵌入（ESM1、ESM2和ProtBert）和理化描述符，集成卷积神经网络（CNN）和双向门控循环单元（BiGRU）的20个混合深度学习模型。在独立数据集上，该框架对五类肽的预测准确率分别达到0.83、0.87、0.89、0.92和0.94，其中ESM-2嵌入表现最优。t-SNE可视化和序列标志分析证实了模型的泛化性和可解释性。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPbvzMOM1MpReAto2GblfQhtOr2f4eUrcDK8GgYrUaVB4hQU644yTwSiGD0hl0vCE2t-2FI-2B1BgFYncIEd5s0YHuzbPf5VjilF6LKAgLc2TwsXqysEjePtcJR4z0LNIsIQ8AUzqk_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FDyk2GK4Jr1RI35MFP7JouLeH8NU-2Bepff-2F3vjuep3GqUdeVFdTfbR36mtu7mGH8IIQCO9knnyttBrypLpokXKNsXIGeJOqoyPPZ-2Ft-2FGYSBiO-2FYkx1bqqdUwc-2BqehwxuC06eElSXrWvvquCh3ikNLnR5c-2B9PTdI3c-2FWtIFe9GHGTfPZnH-2B7DNJfElbNo10-2FTgiI-3D)
