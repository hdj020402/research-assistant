---
title: "IRIS: A Machine Learning-Based Pose Reranking Tool for RNA-Ligand Docking"
title_zh: "IRIS: 一种基于机器学习的RNA-配体对接姿态重新排序工具"
journal: "ACS Omega"
doi: "10.1021/acsomega.5c11891"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6Rux07OK6ZAjTnzDd4vP47zwZB0KtBjdui-2FWq4i7qclNvQpZzmvd84dE0te1oDWZq7rvZE8qqFaGHHamW5mKAjVDSQaxYEOq8QJb3ZiUv-2FDHIPUTh9f9G-2Bl09oX5Bg54OPqYjNoQAYiWe6mjQQarNAH20u_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjyNnjjJYuofzjAi1t96KuWihIxhb3pRbBexokE0zbXmpBLSnvUhnChwjowWu9MDXDnnpNi-2FXp2nADfdkd0aPHvIUhbQQHliF2o2uGKE1SirXO2bDtAjXQLrAiVhjBbZOv183AdS2n4x0e0x8YU6RFNJnZQVs1A4yKJpQUaXqLF5rOBpfJcyNO-2BMFI3tnLXcxOXmQtwWN9YcJagtYzaNzS8CySxBfKaeX7cRN2wIaMhk4-3D"
pub_date: ""
tags: ["machine-learning", "molecular-docking", "rna-ligand-interaction", "pose-ranking", "drug-discovery"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# IRIS: A Machine Learning-Based Pose Reranking Tool for RNA-Ligand Docking

**IRIS: 一种基于机器学习的RNA-配体对接姿态重新排序工具**

## 精华总结
智能RNA相互作用评分器(IRIS)是一个回归模型,利用物理化学和相互作用特征,在迄今为止最大的实验核酸-配体复合物数据集(1,356个结构)上训练,显著提高了姿态排序准确性,可无缝集成到对接流程中以优化RNA靶向药物发现中的配体姿态。

**关键词**: RNA对接、机器学习、姿态排序、配体设计、药物发现

## 摘要（英文）
RNA-ligand docking remains challenging, due in part to intrinsic properties of RNA such as structural flexibility and a highly charged phosphate backbone. rDock, a widely used RNA docking program, can generate ligand poses close to the experimental structure, but its scoring function frequently fails to rank these poses above less accurate alternatives. To supplement rDock, here we introduce the Intelligent RNA Interaction Scorer (IRIS), a regression model leveraging physicochemical and interaction-based features and trained on the largest dataset of experimental nucleic acid-ligand complexes compiled to date (1,356 structures). IRIS improves rDock RNA-ligand pose ranking relative to the use of rDock scores alone. We find that at least one of the 100 top generated poses for any given complex is within 2.0 Å RMSD of the native pose in 79.4% of test complexes. Of these 79.4%%, the default rDock scoring function ranks the correct pose first in 40.2% of cases. IRIS improves this latter fraction to 52.7% and increases the success rate for selecting a near-native pose among the top five ranked poses from 55.4% to 73.2%. IRIS thus significantly enhances pose ranking accuracy and can be seamlessly integrated into docking pipelines to refine ligand poses in RNA-targeted drug discovery.

## 摘要（中文）
RNA-配体对接仍然具有挑战性，部分原因是RNA的固有特性，例如结构柔性和高度带电的磷酸主链。rDock是一种广泛使用的RNA对接程序，可以生成接近实验结构的配体姿势，但其评分功能经常无法将这些姿势排在不太准确的替代方案之上。为了补充rDock，我们在这里介绍了智能RNA相互作用评分器 (IRIS)，这是一种利用物理化学和基于相互作用的特征的回归模型，并在迄今为止编译的实验核酸-配体复合物的最大数据集 (1,356结构) 上进行了训练。相对于单独使用rDock评分，IRIS改善了rDock RNA-配体姿态排序。我们发现，对于任何给定的复合体，100个顶部生成的姿势中至少有一个在测试一下复合体79.4% 原生姿势的2.0 Å RMSD之内。在这79.4% % 中，默认的rDock评分函数在40.2% 情况下将正确的姿势排在第一位。IRIS将后一分数提高到52.7%，并提高了从55.4% 到73.2% 的前五个排名姿势中选择接近原生姿势的成功率。因此，IRIS显著提高了姿态排序的准确性，并且可以无缝集成到对接管道中，以在RNA靶向药物发现中优化配体姿态。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6Rux07OK6ZAjTnzDd4vP47zwZB0KtBjdui-2FWq4i7qclNvQpZzmvd84dE0te1oDWZq7rvZE8qqFaGHHamW5mKAjVDSQaxYEOq8QJb3ZiUv-2FDHIPUTh9f9G-2Bl09oX5Bg54OPqYjNoQAYiWe6mjQQarNAH20u_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjyNnjjJYuofzjAi1t96KuWihIxhb3pRbBexokE0zbXmpBLSnvUhnChwjowWu9MDXDnnpNi-2FXp2nADfdkd0aPHvIUhbQQHliF2o2uGKE1SirXO2bDtAjXQLrAiVhjBbZOv183AdS2n4x0e0x8YU6RFNJnZQVs1A4yKJpQUaXqLF5rOBpfJcyNO-2BMFI3tnLXcxOXmQtwWN9YcJagtYzaNzS8CySxBfKaeX7cRN2wIaMhk4-3D)
