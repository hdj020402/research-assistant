---
title: "IRIS: A Machine Learning-Based Pose Reranking Tool for RNA-Ligand Docking"
title_zh: "IRIS：基于机器学习的RNA-配体对接位姿重排工具"
journal: "ACS Omega"
doi: "10.1021/acsomega.5c11891"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6Rux07OK6ZAjTnzDd4vP47zwZB0KtBjdui-2FWq4i7qclNvQpZzmvd84dE0te1oDWZq7rvZE8qqFaGHHamW5mKAjVDSQaxYEOq8QJb3ZiUv-2FDHIPUTh9f9G-2Bl09oX5Bg54OPqYjNoQAYiWe6mjQQarNAH20u_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjyNnjjJYuofzjAi1t96KuWihIxhb3pRbBexokE0zbXmpBLSnvUhnChwjowWu9MDXDnnpNi-2FXp2nADfdkd0aPHvIUhbQQHliF2o2uGKE1SirXO2bDtAjXQLrAiVhjBbZOv183AdS2n4x0e0x8YU6RFNJnZQVs1A4yKJpQUaXqLF5rOBpfJcyNO-2BMFI3tnLXcxOXmQtwWN9YcJagtYzaNzS8CySxBfKaeX7cRN2wIaMhk4-3D"
pub_date: ""
tags: ["machine-learning", "rna-docking", "pose-ranking", "drug-discovery", "regression-model"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# IRIS: A Machine Learning-Based Pose Reranking Tool for RNA-Ligand Docking

**IRIS：基于机器学习的RNA-配体对接位姿重排工具**

## 精华总结
基于机器学习的IRIS模型通过利用物理化学和相互作用特征，在最大的核酸-配体复合物数据集上训练，显著提升了RNA-配体对接中的位姿排序准确性，可直接应用于药物发现管道。

**关键词**: RNA对接、机器学习、位姿排序、回归模型、药物发现

## 摘要（英文）
RNA-ligand docking remains challenging, due in part to intrinsic properties of RNA such as structural flexibility and a highly charged phosphate backbone. rDock, a widely used RNA docking program, can generate ligand poses close to the experimental structure, but its scoring function frequently fails to rank these poses above less accurate alternatives. To supplement rDock, here we introduce the Intelligent RNA Interaction Scorer (IRIS), a regression model leveraging physicochemical and interaction-based features and trained on the largest dataset of experimental nucleic acid-ligand complexes compiled to date (1,356 structures). IRIS improves rDock RNA-ligand pose ranking relative to the use of rDock scores alone. We find that at least one of the 100 top generated poses for any given complex is within 2.0 Å RMSD of the native pose in 79.4% of test complexes. Of these 79.4%%, the default rDock scoring function ranks the correct pose first in 40.2% of cases. IRIS improves this latter fraction to 52.7% and increases the success rate for selecting a near-native pose among the top five ranked poses from 55.4% to 73.2%. IRIS thus significantly enhances pose ranking accuracy and can be seamlessly integrated into docking pipelines to refine ligand poses in RNA-targeted drug discovery.

## 摘要（中文）
RNA-配体对接面临挑战，主要由于RNA的结构灵活性和高度带电的磷酸骨架。本研究引入智能RNA相互作用评分器(IRIS)，这是一个回归模型，利用物理化学和相互作用特征，在迄今最大的1,356个核酸-配体复合物实验数据集上训练。IRIS通过显著改进位姿排序精度，提高了RNA-配体对接的准确性，可无缝集成到对接管道中，用于RNA靶向药物发现中的配体位姿优化。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6Rux07OK6ZAjTnzDd4vP47zwZB0KtBjdui-2FWq4i7qclNvQpZzmvd84dE0te1oDWZq7rvZE8qqFaGHHamW5mKAjVDSQaxYEOq8QJb3ZiUv-2FDHIPUTh9f9G-2Bl09oX5Bg54OPqYjNoQAYiWe6mjQQarNAH20u_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjyNnjjJYuofzjAi1t96KuWihIxhb3pRbBexokE0zbXmpBLSnvUhnChwjowWu9MDXDnnpNi-2FXp2nADfdkd0aPHvIUhbQQHliF2o2uGKE1SirXO2bDtAjXQLrAiVhjBbZOv183AdS2n4x0e0x8YU6RFNJnZQVs1A4yKJpQUaXqLF5rOBpfJcyNO-2BMFI3tnLXcxOXmQtwWN9YcJagtYzaNzS8CySxBfKaeX7cRN2wIaMhk4-3D)
