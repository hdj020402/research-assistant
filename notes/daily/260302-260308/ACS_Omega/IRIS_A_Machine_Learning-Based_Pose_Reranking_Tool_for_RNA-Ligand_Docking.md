---
title: "IRIS: A Machine Learning-Based Pose Reranking Tool for RNA-Ligand Docking"
title_zh: "IRIS：一种基于机器学习的RNA-配体对接姿态重排序工具"
journal: "ACS Omega"
doi: "10.1021/acsomega.5c11891"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6Rux07OK6ZAjTnzDd4vP47zwZB0KtBjdui-2FWq4i7qclNvQpZzmvd84dE0te1oDWZq7rvZE8qqFaGHHamW5mKAjVDSQaxYEOq8QJb3ZiUv-2FDHIPUTh9f9G-2Bl09oX5Bg54OPqYjNoQAYiWe6mjQQarNAH20u_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjyNnjjJYuofzjAi1t96KuWihIxhb3pRbBexokE0zbXmpBLSnvUhnChwjowWu9MDXDnnpNi-2FXp2nADfdkd0aPHvIUhbQQHliF2o2uGKE1SirXO2bDtAjXQLrAiVhjBbZOv183AdS2n4x0e0x8YU6RFNJnZQVs1A4yKJpQUaXqLF5rOBpfJcyNO-2BMFI3tnLXcxOXmQtwWN9YcJagtYzaNzS8CySxBfKaeX7cRN2wIaMhk4-3D"
pub_date: ""
tags: ["machine-learning", "rna-docking", "pose-ranking", "drug-discovery", "scoring-function"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# IRIS: A Machine Learning-Based Pose Reranking Tool for RNA-Ligand Docking

**IRIS：一种基于机器学习的RNA-配体对接姿态重排序工具**

## 精华总结
Intelligent RNA Interaction Scorer (IRIS)是一个基于机器学习的回归模型,通过物理化学和相互作用特征在最大的核酸-配体复合物数据集上训练,显著提高了RNA-配体对接中的姿态排序准确性,可无缝集成到分子对接管道中用于RNA靶向药物发现。

**关键词**: RNA-配体对接、机器学习、姿态排序、回归模型、药物发现

## 摘要（英文）
RNA-ligand docking remains challenging, due in part to intrinsic properties of RNA such as structural flexibility and a highly charged phosphate backbone. rDock, a widely used RNA docking program, can generate ligand poses close to the experimental structure, but its scoring function frequently fails to rank these poses above less accurate alternatives. To supplement rDock, here we introduce the Intelligent RNA Interaction Scorer (IRIS), a regression model leveraging physicochemical and interaction-based features and trained on the largest dataset of experimental nucleic acid-ligand complexes compiled to date (1,356 structures). IRIS improves rDock RNA-ligand pose ranking relative to the use of rDock scores alone. We find that at least one of the 100 top generated poses for any given complex is within 2.0 Å RMSD of the native pose in 79.4% of test complexes. Of these 79.4%%, the default rDock scoring function ranks the correct pose first in 40.2% of cases. IRIS improves this latter fraction to 52.7% and increases the success rate for selecting a near-native pose among the top five ranked poses from 55.4% to 73.2%. IRIS thus significantly enhances pose ranking accuracy and can be seamlessly integrated into docking pipelines to refine ligand poses in RNA-targeted drug discovery.

## 摘要（中文）
RNA-配体对接仍面临诸多挑战，部分原因在于RNA自身的特性，如结构灵活性和带高度负电荷的磷酸骨架。rDock是一款广泛使用的RNA分子对接程序，能够生成与实验结构高度接近的配体构象，但其打分函数往往无法将这些精确构象排列在准确性较低的备选构象之上。为补充rDock，我们在此介绍智能RNA相互作用评分器（IRIS），这是一种基于回归的模型，利用物理化学特征和基于相互作用的特征，并在迄今为止汇编的最大规模实验性核酸-配体复合物数据集（1,356个结构）上进行训练。与仅使用rDock打分相比，IRIS能更好地对RNA-配体复合物构象进行排序。我们发现，在79.4%的测试复合物中，针对任意给定复合物生成的100个最佳构象中，至少有一个构象与天然构象的RMSD在2.0 Å以内。在这79.4%的案例中，rDock默认打分函数能够在40.2%的情况下将正确构象排名首位。IRIS将后一比例提升至52.7%，并将从排名前五的构象中选出接近天然构象的成功率由55.4%提高至73.2%。因此，IRIS显著提升了构象排序的准确性，并可无缝集成到对接流程中，用于在RNA靶向药物发现中精炼配体构象。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6Rux07OK6ZAjTnzDd4vP47zwZB0KtBjdui-2FWq4i7qclNvQpZzmvd84dE0te1oDWZq7rvZE8qqFaGHHamW5mKAjVDSQaxYEOq8QJb3ZiUv-2FDHIPUTh9f9G-2Bl09oX5Bg54OPqYjNoQAYiWe6mjQQarNAH20u_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjyNnjjJYuofzjAi1t96KuWihIxhb3pRbBexokE0zbXmpBLSnvUhnChwjowWu9MDXDnnpNi-2FXp2nADfdkd0aPHvIUhbQQHliF2o2uGKE1SirXO2bDtAjXQLrAiVhjBbZOv183AdS2n4x0e0x8YU6RFNJnZQVs1A4yKJpQUaXqLF5rOBpfJcyNO-2BMFI3tnLXcxOXmQtwWN9YcJagtYzaNzS8CySxBfKaeX7cRN2wIaMhk4-3D)
