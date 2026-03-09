---
title: "Fine-Tuning DiffDock-L for Allosteric Kinase Docking"
title_zh: "针对别构激酶对接的DiffDock-L微调"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02846"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPOIdu89OGOrhUZ2PvPYyPmQN9g1qbSkWYaud7umZ-2F724zoKLIqm9pAIaRalklstghI0MlkUXzKwOIWGMN58qNcnKdZgbgAjQDS7b2aVeS1gGM4Z1wry8R3dYalRF3AzMcPp6m_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjMiGhqYuNZSeljVi5kw6RDOwb5HTN1959abUlgudU81u7jVAM-2FhpZVTcTU3v3yX9EkEru6YWZZy5JVyLApaZM1Y89COrzOLAJxBePBWb0cMODf-2FTRmO7sQWx6ov7fiqXnt22Fwyh7nxT5-2BlJE6EYk-2BhvZBZ-2FQR8SrAo69s74NL8OGKmGdOKlW5ZNbpxo6FMxkjKotkhKB60-2FqwGBsTcdLgiGqQkIyaaIwFfaX9blXtn0-3D"
pub_date: ""
tags: ["molecular-docking", "deep-learning", "drug-discovery", "kinase-inhibitors", "diffusion-models"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Fine-Tuning DiffDock-L for Allosteric Kinase Docking

**针对别构激酶对接的DiffDock-L微调**

## 精华总结
通过对DiffDock-L模型进行针对性微调，该研究显著改善了变构激酶抑制剂的分子对接预测能力，同时保持了对ATP结合位点配体的预测性能。研究提供了实用指导，说明如何通过重新训练适应低数据量和高难度的激酶结构药物设计任务。

**关键词**: 分子对接、变构激酶抑制剂、扩散模型、深度学习、药物设计

## 摘要（英文）
Allosteric kinase inhibitors are an important modality for overcoming resistance and achieving selectivity, yet most structure-based docking and deep generative models are trained predominantly on orthosteric protein-ligand complexes. As a result, current methods often misplace allosteric kinase ligands into the adenosine triphosphate (ATP)-binding site and fail to recover the correct binding mode. Here we curate AlloSet, a kinome-wide, time-split data set of kinase-ligand complexes annotated by binding mode, to systematically evaluate and fine-tune the diffusion-based docking model DiffDock-L for allosteric pose prediction. We explore several fine-tuning strategies, including increased dropout, freezing of torsion parameters with translation/rotation-only fine-tuning, and molecular dynamics-based supersampling of receptor conformations and ligand poses. The resulting DiffDock-L-Allo model is found to markedly improve pose-recovery metrics for Type III/IV allosteric binders while preserving the performance on ATP-site ligands. Binding-mode-resolved evaluations and comparisons with cofolding models such as AlphaFold3 and Boltz-2 highlight how targeted retraining reshapes the generative model's sampling distribution, offering practical guidance for adapting AI-driven docking to challenging, low-data binding modes in kinase structure-based drug design.

## 摘要（中文）
别构激酶抑制剂是克服耐药性和实现选择性的重要策略，然而，大多数基于结构的对接方法和深度生成模型主要是在正构位点的蛋白质-配体复合物数据上进行训练的。因此，现有的方法常常会将变构激酶配体错误地定位到三磷酸腺苷（ATP）结合位点，而无法正确恢复其天然结合模式。在此，我们构建了AlloSet数据集——一个覆盖整个激酶组、按时间划分，并按结合模式进行注释的激酶-配体复合物数据集，用于系统性地评估和微调基于扩散的对接模型DiffDock-L在别构构象预测中的性能。我们探索了多种微调策略，包括增加丢弃率、在仅进行平移/旋转微调时冻结扭转参数，以及基于分子动力学对受体构象和配体构象进行超采样。结果表明，DiffDock-L-Allo模型在保持ATP结合位点配体性能的同时，显著提升了III型和IV型别构结合物的构象重构指标。基于结合模式的评估以及与AlphaFold3、Boltz-2等共折叠模型的对比分析表明，定向再训练能够显著重塑生成模型的采样分布，为将人工智能驱动的对接技术应用于激酶结构导向药物设计中那些数据稀缺、具有挑战性的结合模式提供了切实可行的指导。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPOIdu89OGOrhUZ2PvPYyPmQN9g1qbSkWYaud7umZ-2F724zoKLIqm9pAIaRalklstghI0MlkUXzKwOIWGMN58qNcnKdZgbgAjQDS7b2aVeS1gGM4Z1wry8R3dYalRF3AzMcPp6m_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjMiGhqYuNZSeljVi5kw6RDOwb5HTN1959abUlgudU81u7jVAM-2FhpZVTcTU3v3yX9EkEru6YWZZy5JVyLApaZM1Y89COrzOLAJxBePBWb0cMODf-2FTRmO7sQWx6ov7fiqXnt22Fwyh7nxT5-2BlJE6EYk-2BhvZBZ-2FQR8SrAo69s74NL8OGKmGdOKlW5ZNbpxo6FMxkjKotkhKB60-2FqwGBsTcdLgiGqQkIyaaIwFfaX9blXtn0-3D)
