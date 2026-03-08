---
title: "DVMMHGNN: A Dual View Multi-Modal Heterogeneous Graph Neural Network with Contrastive Learning for Microbe-Informed Drug Repurposing"
title_zh: "DVMMHGNN:用于微生物信息指导的药物重新定位的对比学习双视图多模态异构图神经网络"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c03158"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPfSl1cpPpZRROwNUCh2xYZrLJXNIj2bNB1JWdrWLQ9FdNaNV5kCnC8zUZysRwt3slf07aZjy6MOG3f9ipQYcXbNpz1q6FHKxcrXB7HN8ibQU6ozS7hqLotnPTS0DEHtIvoZgT_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FCmClyx6seiBBM4koyFexH8D3ixEVxsII8w2Qjrve8aJZQ28I9r9wx9xQDLcByWr1JSFxGN-2Bw0e9jBxBfEjscClj0FCddYSU5GnY8CgYybH3VTap1fxLjNs8OihxD-2F4Gn95TrpnLnG0w0-2FS-2FMBzghrUfAyrYNIp5VjkxlctKbi-2B4YN3bQSOY-2BLI6rchb8FAj9c-3D"
pub_date: ""
tags: ["graph-neural-networks", "drug-repurposing", "contrastive-learning", "multimodal-integration", "computational-chemistry"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# DVMMHGNN: A Dual View Multi-Modal Heterogeneous Graph Neural Network with Contrastive Learning for Microbe-Informed Drug Repurposing

**DVMMHGNN:用于微生物信息指导的药物重新定位的对比学习双视图多模态异构图神经网络**

## 精华总结
DVMMHGNN是一个异构图对比学习框架，用于微生物信息指导的药物重新定位，联合整合结构和元路径信息，在预测药物-疾病关联方面持续超越九种最先进的方法。

**关键词**: 药物重新定位、图神经网络、对比学习、多模态学习、药物-疾病关联预测

## 摘要（英文）
Drug repurposing (DR) offers an efficient and cost-effective strategy for pharmaceutical development by identifying new therapeutic applications for existing drugs. The effectiveness of this approach relies on accurately uncovering potential drug-disease associations; however, capturing the complex biological interactions underlying these associations remains a major challenge. Current computational approaches frequently overlook the critical regulatory role of the microbiota in modulating drug action pathways. Moreover, many methods fail to preserve semantic consistency during multimodal biological data integration and heterogeneous graph augmentation, thereby limiting their representational capacity. To overcome these limitations, we propose DVMMHGNN, a heterogeneous graph contrastive learning framework for microbe informed drug repurposing that jointly integrates structural and meta-path information. First, a multimodal feature fusion module embeds heterogeneous biological entities into a unified latent space to ensure cross-modal feature alignment. Second, a graph-masked autoencoder is employed to capture high-order representations from similarity networks. Finally, DVMMHGNN enhances semantic coherence through contrastive learning at both the structural and meta-path levels, aligning embeddings across multiple views to effectively capture both local and global semantics. Experimental evaluations on the constructed benchmark data set demonstrate that DVMMHGNN consistently outperforms nine state-of-the-art methods in predicting drug-disease associations, achieving superior performance across AUC, AUPR, and F1-score metrics. Ablation studies further validate the contribution of each model component, while case analyses highlight the potential of DVMMHGNN to identify novel drug indications and guide therapeutic strategy development.

## 摘要（中文）
本研究提出DVMMHGNN框架，用于微生物信息指导的药物重新定位。该方法通过多模态特征融合模块将异构生物实体嵌入统一的潜在空间，采用图掩码自编码器捕获相似网络中的高阶表征，并通过结构和元路径两个层次的对比学习增强语义一致性。在基准数据集上的实验表明，该方法在预测药物-疾病关联方面超越九种最先进的方法，在AUC、AUPR和F1-score指标上表现优异。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPfSl1cpPpZRROwNUCh2xYZrLJXNIj2bNB1JWdrWLQ9FdNaNV5kCnC8zUZysRwt3slf07aZjy6MOG3f9ipQYcXbNpz1q6FHKxcrXB7HN8ibQU6ozS7hqLotnPTS0DEHtIvoZgT_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FCmClyx6seiBBM4koyFexH8D3ixEVxsII8w2Qjrve8aJZQ28I9r9wx9xQDLcByWr1JSFxGN-2Bw0e9jBxBfEjscClj0FCddYSU5GnY8CgYybH3VTap1fxLjNs8OihxD-2F4Gn95TrpnLnG0w0-2FS-2FMBzghrUfAyrYNIp5VjkxlctKbi-2B4YN3bQSOY-2BLI6rchb8FAj9c-3D)
