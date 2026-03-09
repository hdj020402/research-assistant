---
title: "Coarse-Grained Mapping of Fluid Particles via Evolutionary Fuzzy Clustering: Membership-Evolution Term as a Pressure Correction Mechanism"
title_zh: "通过进化模糊聚类对流体颗粒进行粗粒度映射: 隶属进化项作为压力校正机制"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01867"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1US8EKTjTxS2OmW4-2B0mjRUPqGGQS4yxDw1yTZZuM2GpRoGGxPIriYdNQ9eYXef9zjTCW389G7b9f3SY72tEt4hHMf3t4SmRRoXv46erLP4-2B1nY41iFExQkGYoefXrQ59rUZDI_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXc2RYNe3UlLS9pq-2BEMdtMXEs8oRUs7Pon-2B4zQV6XjgAKbCQnIIBQGtKdNzKY6cmS-2ByXXEJXkbQjUc4mk20adAPQp10uYTWoNl0WXsM1JbZyT0EUjKFBxAuvilOuFjtpRYqSN3ZbA57sw8EI42QvcaiIhVknC0qbYhcZkamYgi21cj6RuuGjLEcH8-2Bjz2BdaC8Q-3D"
pub_date: ""
tags: ["coarse-graining", "fuzzy-clustering", "molecular-dynamics", "machine-learning", "soft-matter"]
ai_relevance: 3
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Coarse-Grained Mapping of Fluid Particles via Evolutionary Fuzzy Clustering: Membership-Evolution Term as a Pressure Correction Mechanism

**通过进化模糊聚类对流体颗粒进行粗粒度映射: 隶属进化项作为压力校正机制**

## 精华总结
提出了一种基于熵正则化的模糊聚类方法，通过演化的模糊粒子-簇隶属度项作为压力修正机制，实现了流体粒子系统的有效粗粒化映射。该方法在Lennard-Jones流体和水分子系统中验证了中等模糊度水平能最好地保留结构特征，为粗粒化动力学模拟中的压力修正提供了物理基础。

**关键词**: 粗粒化、模糊聚类、熵正则化、压力修正、流体模拟

## 摘要（英文）
Coarse-graining is an effective approach for bridging atomistic and mesoscopic descriptions of fluid particle systems. However, fixed coarse-grained (CG) mappings do not account for the unbundled nature of fluid particles. We propose an entropy-regularized fuzzy clustering method with temporal smoothness constraints, examining in detail the role of the evolution of fuzzy particle-cluster membership degrees throughout the coarse-graining process. Entropy regularization controls the level of spatial fuzziness, while the temporal smoothness constraints enhance the continuity of cluster position evolution. Within a bottom-up force-matching framework, the interactions between clusters are decomposed into two contributions: a particle-interaction term, which is the weighted sum of interactions between particles, and a membership-evolution term, which originates from the temporal variation of membership degrees. Analyses based on the Lennard-Jones (L-J) fluid particle system and the water molecule system show that an intermediate level of fuzziness yields the most pronounced structural features in the radial distribution functions. The particle-interaction term exhibits system-dependent characteristics, whereas the membership-evolution term consistently provides a repulsive contribution across different systems. Moreover, CG dynamics simulations of the L-J fluid demonstrate that including the membership-evolution term effectively restores the system pressure, which could be interpreted as a pressure correction scheme. This finding provides a physical perspective on the transition from microscopic particle interactions to macroscopic fluid pressure constraints and reveals a bottom-up origin for incorporating additional pressure corrections into fluid CG dynamics, which could be beneficial for the future design of coarse-graining strategies.

## 摘要（中文）
粗粒化是一种有效的方法，用于衔接流体粒子系统的原子尺度描述与介观尺度描述。然而，固定的粗粒化映射无法考虑流体粒子的非捆绑特性。我们提出了一种具有时间平滑性约束的熵正则化模糊聚类方法，并详细探讨了在粗粒化过程中模糊粒子—聚类隶属度演化所起的作用。熵正则化控制空间模糊程度，而时间平滑约束则增强聚类位置演变的连续性。在自下而上的力匹配框架下，簇之间的相互作用被分解为两项：一项是粒子间相互作用项，即粒子间相互作用的加权和；另一项是成员关系演化项，它源于成员隶属度随时间的变化。基于Lennard-Jones（L-J）流体粒子系统和水分子系统的分析表明，适中的模糊程度能使径向分布函数呈现出最为显著的结构特征。粒子间相互作用项表现出与具体系统相关的特性，而隶属度演化项则在不同系统中始终提供排斥性贡献。此外，对L-J流体进行的计算流体力学动力学模拟表明，引入成员关系演化项能够有效恢复系统压力，这可被解释为一种压力校正方案。这一发现从物理视角阐释了从微观粒子相互作用到宏观流体压力约束的转变过程，并揭示了在流体粗粒化动力学中引入附加压力修正项的自下而上起源，这对未来粗粒化策略的设计具有重要启示意义。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1US8EKTjTxS2OmW4-2B0mjRUPqGGQS4yxDw1yTZZuM2GpRoGGxPIriYdNQ9eYXef9zjTCW389G7b9f3SY72tEt4hHMf3t4SmRRoXv46erLP4-2B1nY41iFExQkGYoefXrQ59rUZDI_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXc2RYNe3UlLS9pq-2BEMdtMXEs8oRUs7Pon-2B4zQV6XjgAKbCQnIIBQGtKdNzKY6cmS-2ByXXEJXkbQjUc4mk20adAPQp10uYTWoNl0WXsM1JbZyT0EUjKFBxAuvilOuFjtpRYqSN3ZbA57sw8EI42QvcaiIhVknC0qbYhcZkamYgi21cj6RuuGjLEcH8-2Bjz2BdaC8Q-3D)
