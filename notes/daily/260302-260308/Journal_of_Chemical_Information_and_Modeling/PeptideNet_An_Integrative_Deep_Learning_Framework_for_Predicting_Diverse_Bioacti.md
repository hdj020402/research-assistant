---
title: "PeptideNet: An Integrative Deep Learning Framework for Predicting Diverse Bioactive Peptides Using Protein Language Model Embeddings"
title_zh: "Peptitenet: 一种使用蛋白质语言模型嵌入预测多种生物活性肽的集成深度学习框架"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02885"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPbvzMOM1MpReAto2GblfQhtOr2f4eUrcDK8GgYrUaVB4hQU644yTwSiGD0hl0vCE2t-2FI-2B1BgFYncIEd5s0YHuzbPf5VjilF6LKAgLc2TwsXqysEjePtcJR4z0LNIsIQ8AUzqk_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FDyk2GK4Jr1RI35MFP7JouLeH8NU-2Bepff-2F3vjuep3GqUdeVFdTfbR36mtu7mGH8IIQCO9knnyttBrypLpokXKNsXIGeJOqoyPPZ-2Ft-2FGYSBiO-2FYkx1bqqdUwc-2BqehwxuC06eElSXrWvvquCh3ikNLnR5c-2B9PTdI3c-2FWtIFe9GHGTfPZnH-2B7DNJfElbNo10-2FTgiI-3D"
pub_date: ""
tags: ["deep-learning", "peptide-prediction", "protein-language-models", "bioactivity-prediction", "drug-discovery"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# PeptideNet: An Integrative Deep Learning Framework for Predicting Diverse Bioactive Peptides Using Protein Language Model Embeddings

**Peptitenet: 一种使用蛋白质语言模型嵌入预测多种生物活性肽的集成深度学习框架**

## 精华总结
大型蛋白质语言模型嵌入与PeptideNet架构的整合使模型能够捕捉全局上下文信息和残基级特征，为多肽生物活性预测建立了一个通用且可解释的框架。

**关键词**: 蛋白质语言模型、肽生物活性预测、深度学习、ESM嵌入、多任务预测

## 摘要（英文）
Bioactive peptides are multifunctional biomolecules composed of short amino acid sequences that exhibit diverse biological activities, including antioxidative, antihemolytic, anticell-penetrating, antiviral, and antimicrobial effects. Accurate computational prediction of peptide bioactivity is essential for accelerating the discovery and design of peptide-based therapeutics. In this study, we investigated five categories of bioactive peptides using four distinct feature representations, including large protein language model embeddings (ESM1, ESM2, and ProtBert) and physicochemical descriptors. A total of 20 hybrid deep learning models integrating Convolutional Neural Networks (CNNs) and Bidirectional Gated Recurrent Units (BiGRUs) were developed to capture both local sequence motifs and long-range dependencies. The proposed PeptideNet model achieved robust predictive performance, with accuracies of 0.83, 0.87, 0.89, 0.92, and 0.94 for antioxidative, antihemolytic, anticell-penetrating, antiviral, and antimicrobial peptides, respectively, on the independent data set. Among the evaluated feature sets, ESM-2 embeddings consistently outperformed others across all peptide types, providing rich contextual and evolutionary information. Furthermore, t-SNE visualization of learned representations demonstrated effective generalization across peptide classes, while positional sequence logo analysis revealed conserved residue patterns contributing to peptide bioactivity. The integration of large protein language model embeddings with the PeptideNet architecture enables the model to capture both global contextual information and residue-level features, establishing a generalized and interpretable framework for multipeptide bioactivity prediction.

## 摘要（中文）
生物活性肽是由短氨基酸序列组成的多功能生物分子，具有多种生物活性，包括抗氧化，抗溶血，抗细胞穿透，抗病毒和抗微生物作用。肽生物活性的准确计算预测对于加速基于肽的疗法的发现和设计至关重要。在这项研究中，我们使用四种不同的特征表示研究了五类生物活性肽，包括大蛋白质语言模型嵌入 (ESM1，ESM2和ProtBert) 和物理化学描述符。总共开发了20个集成卷积神经网络 (cnn) 和双向门控循环单元 (bigru) 的混合深度学习模型，以捕获局部序列基序和远程依赖性。提出的PeptideNet模型实现了强大的预测性能，在独立数据集上，抗氧化，抗溶血，抗细胞穿透，抗病毒和抗微生物肽的准确性分别为0.83，0.87，0.89，0.92和0.94。在评估的特征集中，ESM-2嵌入在所有肽类型中始终优于其他肽，提供了丰富的上下文和进化信息。此外，学习表示的t-sne可视化证明了跨肽课程的有效概括，而位置序列徽标分析揭示了有助于肽生物活性的保守残基模式。大蛋白质语言模型嵌入与PeptideNet体系结构的集成使该模型能够捕获全局上下文信息和残基级别的特征，从而为多肽生物活性预测建立了通用且可解释的框架。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPbvzMOM1MpReAto2GblfQhtOr2f4eUrcDK8GgYrUaVB4hQU644yTwSiGD0hl0vCE2t-2FI-2B1BgFYncIEd5s0YHuzbPf5VjilF6LKAgLc2TwsXqysEjePtcJR4z0LNIsIQ8AUzqk_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FDyk2GK4Jr1RI35MFP7JouLeH8NU-2Bepff-2F3vjuep3GqUdeVFdTfbR36mtu7mGH8IIQCO9knnyttBrypLpokXKNsXIGeJOqoyPPZ-2Ft-2FGYSBiO-2FYkx1bqqdUwc-2BqehwxuC06eElSXrWvvquCh3ikNLnR5c-2B9PTdI3c-2FWtIFe9GHGTfPZnH-2B7DNJfElbNo10-2FTgiI-3D)
