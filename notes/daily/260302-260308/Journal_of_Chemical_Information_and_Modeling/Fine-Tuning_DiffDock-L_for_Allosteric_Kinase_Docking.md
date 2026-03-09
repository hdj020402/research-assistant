---
title: "Fine-Tuning DiffDock-L for Allosteric Kinase Docking"
title_zh: "针对别构激酶对接的DiffDock-L微调"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02846"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPOIdu89OGOrhUZ2PvPYyPmQN9g1qbSkWYaud7umZ-2F724zoKLIqm9pAIaRalklstghI0MlkUXzKwOIWGMN58qNcnKdZgbgAjQDS7b2aVeS1gGM4Z1wry8R3dYalRF3AzMcPp6m_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjMiGhqYuNZSeljVi5kw6RDOwb5HTN1959abUlgudU81u7jVAM-2FhpZVTcTU3v3yX9EkEru6YWZZy5JVyLApaZM1Y89COrzOLAJxBePBWb0cMODf-2FTRmO7sQWx6ov7fiqXnt22Fwyh7nxT5-2BlJE6EYk-2BhvZBZ-2FQR8SrAo69s74NL8OGKmGdOKlW5ZNbpxo6FMxkjKotkhKB60-2FqwGBsTcdLgiGqQkIyaaIwFfaX9blXtn0-3D"
pub_date: ""
tags: ["protein-ligand-docking", "diffusion-models", "kinase-inhibitors", "generative-ai", "drug-design"]
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
通过靶向重训练调整生成模型的采样分布，为将AI驱动对接方法适应激酶结构设计中具有挑战性的低数据绑定模式提供实践指导。

**关键词**: 扩散模型、异位点对接、激酶抑制剂、深度学习、蛋白质-配体结合

## 摘要（英文）
Allosteric kinase inhibitors are an important modality for overcoming resistance and achieving selectivity, yet most structure-based docking and deep generative models are trained predominantly on orthosteric protein-ligand complexes. As a result, current methods often misplace allosteric kinase ligands into the adenosine triphosphate (ATP)-binding site and fail to recover the correct binding mode. Here we curate AlloSet, a kinome-wide, time-split data set of kinase-ligand complexes annotated by binding mode, to systematically evaluate and fine-tune the diffusion-based docking model DiffDock-L for allosteric pose prediction. We explore several fine-tuning strategies, including increased dropout, freezing of torsion parameters with translation/rotation-only fine-tuning, and molecular dynamics-based supersampling of receptor conformations and ligand poses. The resulting DiffDock-L-Allo model is found to markedly improve pose-recovery metrics for Type III/IV allosteric binders while preserving the performance on ATP-site ligands. Binding-mode-resolved evaluations and comparisons with cofolding models such as AlphaFold3 and Boltz-2 highlight how targeted retraining reshapes the generative model's sampling distribution, offering practical guidance for adapting AI-driven docking to challenging, low-data binding modes in kinase structure-based drug design.

## 摘要（中文）
变构激酶抑制剂是克服抗性和实现选择性的重要方式，然而大多数基于结构的对接和深度生成模型主要在正构蛋白质-配体复合物上训练。结果，目前的方法经常将变构激酶配体错位到三磷酸腺苷 (ATP) 结合位点，并且不能恢复正确的结合模式。在这里，我们策划了AlloSet，一个由结合模式注释的激酶-配体复合物的全kinome时间分割数据集，以系统地评估和微调用于变构姿势预测的基于扩散的对接模型diffdock-l。我们探索了几种微调策略，包括增加辍学，仅通过平移/旋转微调冻结扭转参数以及基于分子动力学的受体构象和配体姿势的超采样。发现所得的diffdock-l-allo模型显着改善了III/IV型变构结合剂的姿态恢复指标，同时保留了ATP位点配体的性能。结合模式解决的评估和与诸如AlphaFold3和Boltz-2等共折叠模型的比较突出了针对性的再训练如何重塑生成模型的采样分布，为使AI驱动的对接适应基于激酶结构的药物设计中具有挑战性的低数据结合模式提供了实用指导。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPOIdu89OGOrhUZ2PvPYyPmQN9g1qbSkWYaud7umZ-2F724zoKLIqm9pAIaRalklstghI0MlkUXzKwOIWGMN58qNcnKdZgbgAjQDS7b2aVeS1gGM4Z1wry8R3dYalRF3AzMcPp6m_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjMiGhqYuNZSeljVi5kw6RDOwb5HTN1959abUlgudU81u7jVAM-2FhpZVTcTU3v3yX9EkEru6YWZZy5JVyLApaZM1Y89COrzOLAJxBePBWb0cMODf-2FTRmO7sQWx6ov7fiqXnt22Fwyh7nxT5-2BlJE6EYk-2BhvZBZ-2FQR8SrAo69s74NL8OGKmGdOKlW5ZNbpxo6FMxkjKotkhKB60-2FqwGBsTcdLgiGqQkIyaaIwFfaX9blXtn0-3D)
