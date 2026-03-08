---
title: "DVMMHGNN: A Dual View Multi-Modal Heterogeneous Graph Neural Network with Contrastive Learning for Microbe-Informed Drug Repurposing"
title_zh: "DVMMHGNN：一种用于微生物信息指导的药物重新定位的双视图多模态异构图神经网络与对比学习"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c03158"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPfSl1cpPpZRROwNUCh2xYZrLJXNIj2bNB1JWdrWLQ9FdNaNV5kCnC8zUZysRwt3slf07aZjy6MOG3f9ipQYcXbNpz1q6FHKxcrXB7HN8ibQU6ozS7hqLotnPTS0DEHtIvoZgT_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FCmClyx6seiBBM4koyFexH8D3ixEVxsII8w2Qjrve8aJZQ28I9r9wx9xQDLcByWr1JSFxGN-2Bw0e9jBxBfEjscClj0FCddYSU5GnY8CgYybH3VTap1fxLjNs8OihxD-2F4Gn95TrpnLnG0w0-2FS-2FMBzghrUfAyrYNIp5VjkxlctKbi-2B4YN3bQSOY-2BLI6rchb8FAj9c-3D"
pub_date: ""
tags: ["drug-repurposing", "graph-neural-networks", "contrastive-learning", "microbiome-modeling", "knowledge-graphs"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# DVMMHGNN: A Dual View Multi-Modal Heterogeneous Graph Neural Network with Contrastive Learning for Microbe-Informed Drug Repurposing

**DVMMHGNN：一种用于微生物信息指导的药物重新定位的双视图多模态异构图神经网络与对比学习**

## 精华总结
提出DVMMHGNN，一个异构图对比学习框架，用于微生物信息指导的药物重新定位，联合整合结构和元路径信息，在药物-疾病关联预测中持续优于九种最先进方法。

**关键词**: 药物重新定位、异构图神经网络、对比学习、微生物组、多模态融合

## 摘要（英文）
Drug repurposing (DR) offers an efficient and cost-effective strategy for pharmaceutical development by identifying new therapeutic applications for existing drugs. The effectiveness of this approach relies on accurately uncovering potential drug-disease associations; however, capturing the complex biological interactions underlying these associations remains a major challenge. Current computational approaches frequently overlook the critical regulatory role of the microbiota in modulating drug action pathways. Moreover, many methods fail to preserve semantic consistency during multimodal biological data integration and heterogeneous graph augmentation, thereby limiting their representational capacity. To overcome these limitations, we propose DVMMHGNN, a heterogeneous graph contrastive learning framework for microbe informed drug repurposing that jointly integrates structural and meta-path information. First, a multimodal feature fusion module embeds heterogeneous biological entities into a unified latent space to ensure cross-modal feature alignment. Second, a graph-masked autoencoder is employed to capture high-order representations from similarity networks. Finally, DVMMHGNN enhances semantic coherence through contrastive learning at both the structural and meta-path levels, aligning embeddings across multiple views to effectively capture both local and global semantics. Experimental evaluations on the constructed benchmark data set demonstrate that DVMMHGNN consistently outperforms nine state-of-the-art methods in predicting drug-disease associations, achieving superior performance across AUC, AUPR, and F1-score metrics. Ablation studies further validate the contribution of each model component, while case analyses highlight the potential of DVMMHGNN to identify novel drug indications and guide therapeutic strategy development.

## 摘要（中文）
药物重新定位（DR）通过为现有药物发现新的治疗应用，为药物开发提供了一种高效且经济有效的策略。该方法的有效性取决于准确揭示潜在的药物-疾病关联；然而，捕捉这些关联背后的复杂生物相互作用仍然是一个主要挑战。当前的计算方法经常忽视微生物群落在调节药物作用途径中的关键调控作用。此外，许多方法在多模态生物数据集成和异构图增强过程中未能保持语义一致性，从而限制了其表示能力。为了克服这些限制，我们提出了DVMMHGNN，一个用于微生物信息指导的药物重新定位的异构图对比学习框架，该框架联合整合了结构和元路径信息。首先，多模态特征融合模块将异构生物实体嵌入到统一的潜在空间中，以确保跨模态特征对齐。其次，采用图掩蔽自编码器从相似性网络中捕捉高阶表示。最后，DVMMHGNN通过在结构和元路径层次上进行对比学习来增强语义一致性，在多个视图中对齐嵌入，以有效捕捉局部和全局语义。在构建的基准数据集上的实验评估表明，DVMMHGNN在预测药物-疾病关联方面始终优于九种最先进的方法，在AUC、AUPR和F1-score指标上实现了优异的性能。消融研究进一步验证了每个模型组件的贡献，而案例分析突出了DVMMHGNN在识别新的药物适应症和指导治疗策略开发中的潜力。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPfSl1cpPpZRROwNUCh2xYZrLJXNIj2bNB1JWdrWLQ9FdNaNV5kCnC8zUZysRwt3slf07aZjy6MOG3f9ipQYcXbNpz1q6FHKxcrXB7HN8ibQU6ozS7hqLotnPTS0DEHtIvoZgT_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FCmClyx6seiBBM4koyFexH8D3ixEVxsII8w2Qjrve8aJZQ28I9r9wx9xQDLcByWr1JSFxGN-2Bw0e9jBxBfEjscClj0FCddYSU5GnY8CgYybH3VTap1fxLjNs8OihxD-2F4Gn95TrpnLnG0w0-2FS-2FMBzghrUfAyrYNIp5VjkxlctKbi-2B4YN3bQSOY-2BLI6rchb8FAj9c-3D)
