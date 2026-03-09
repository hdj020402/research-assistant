---
title: "Coarse-Grained Martini 3 Model of Chondroitin Sulfate A"
title_zh: "硫酸软骨素A的粗粒马提尼3模型"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01743"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1wLy-2FiIIlpbaUoL-2FK-2FS6jrxRxJi0OMDHUs7kwUCfR5xlrvgcuWoOUMLHirGqVQ-2ByFJ9nuSqH-2B6GGWZ8IcKtlLFXuSmTE7B6EhfW6f0BD0QtiRWCom0DGcMcxFNiD2ZUgQ98I2_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXchnp8Dqdz-2BiEHl1pBSzTE9eytuCbc0bf31Mw3GhhFGXkrUn-2BP5Kj4drihSTEO5CKU6a6ZrkOCIJDFBsnoqelc8TBLqAgV11WTLpCBSxpFhgkycK-2F-2BPpN6cB05rl-2Bcb5Y-2BmXVx4lPhNoXIniCc3NCbYHKnzB2MOV5IvxWUAAFNT04-2BTiS7XCYOZ0tA6Ho83ErE-3D"
pub_date: ""
tags: ["molecular-dynamics", "coarse-graining", "force-field", "biomolecules", "computational-chemistry"]
ai_relevance: 2
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Coarse-Grained Martini 3 Model of Chondroitin Sulfate A

**硫酸软骨素A的粗粒马提尼3模型**

## 精华总结
该研究基于Martini 3力场开发了硫酸软骨素A的粗粒化分子动力学模拟模型,能够再现其原子性质和聚合物结构,同时显著降低计算成本。通过改进静电参数处理,解决了默认参数导致过度聚集的问题,为高度带电系统的粗粒化模型发展提供了指导。

**关键词**: 粗粒化分子动力学、硫酸软骨素A、Martini力场、静电相互作用、计算模型

## 摘要（英文）
Chondroitin sulfate A (CSA) is a negatively charged linear glycosaminoglycan which plays a vital role in many biological processes. Research on CSA has been challenging due to its size, chemical heterogeneity, and multitude of binding partners. To address these issues, we developed a model of CSA for coarse-grained molecular dynamics simulations based on the Martini 3 force-field. We demonstrate that this model is capable of reproducing atomistic properties of the repeating CSA disaccharide unit, including its molecular volume and bonded interactions, and structural polymer properties of CSA chains of different lengths. In particular, for biologically-relevant long chains and despite of using an explicit solvent, the computational cost is significantly reduced, relative to the cost equivalent atomistic simulations would require. The compatibility of the model with the Martini Gō protein model was tested by retrieving the forceresponse of the CSA–malaria adhesin VAR2CSA complex. Importantly, we explored the influence of electrostatics on CSA aggregation. We show that the default Martini 3 parameters lead to over-aggregation. We provide at least three different strategies to alleviate this issue, making use of a bigger bead for sodium cations, reflecting its hydration shell, partial ionic charges, as a mean-field resource to take into account electronic polarizability, and, optionally, particle-mesh Ewald summation as a more robust treatment of long-range electrostatics. Our model opens the door for predictive modeling of CSA and potentially other chondroitin sulfates. In addition, this model provides insights for the further development of coarse-grained models of highly-charged systems.

## 摘要（中文）
硫酸软骨素A (CSA) 是一种带负电荷的线性糖胺聚糖，在许多生物过程中起着至关重要的作用。对CSA的研究由于其大小、化学异质性和众多的结合配偶体而具有挑战性。为了解决这些问题，我们基于Martini 3力场开发了用于粗粒分子动力学模拟的CSA模型。我们证明该模型能够再现重复CSA二糖单元的原子特性，包括其分子体积和键合相互作用，以及不同长度CSA链的结构聚合物特性。特别地，对于生物学相关的长链，尽管使用显式溶剂，但相对于等效原子模拟所需的成本，计算成本显著降低。通过检索CSA-疟疾粘附素VAR2CSA复合物的响应，测试了该模型与marting ō 蛋白模型的兼容性。重要的是，我们探讨了静电对CSA聚集的影响。我们证明了默认的Martini 3参数会导致过度聚合。我们提供了至少三种不同的策略来缓解这个问题，利用更大的钠阳离子珠，反映其水合壳，部分离子电荷，作为考虑电子极化率的平均场资源，并且可选地，粒子网格Ewald求和作为远程静电的更稳健的处理。我们的模型为CSA和潜在的其他硫酸软骨素的预测建模打开了大门。此外，该模型为进一步开发高电荷系统的粗粒度模型提供了见解。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1wLy-2FiIIlpbaUoL-2FK-2FS6jrxRxJi0OMDHUs7kwUCfR5xlrvgcuWoOUMLHirGqVQ-2ByFJ9nuSqH-2B6GGWZ8IcKtlLFXuSmTE7B6EhfW6f0BD0QtiRWCom0DGcMcxFNiD2ZUgQ98I2_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXchnp8Dqdz-2BiEHl1pBSzTE9eytuCbc0bf31Mw3GhhFGXkrUn-2BP5Kj4drihSTEO5CKU6a6ZrkOCIJDFBsnoqelc8TBLqAgV11WTLpCBSxpFhgkycK-2F-2BPpN6cB05rl-2Bcb5Y-2BmXVx4lPhNoXIniCc3NCbYHKnzB2MOV5IvxWUAAFNT04-2BTiS7XCYOZ0tA6Ho83ErE-3D)
