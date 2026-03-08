---
title: "Coarse-Grained Mapping of Fluid Particles via Evolutionary Fuzzy Clustering: Membership-Evolution Term as a Pressure Correction Mechanism"
title_zh: "通过演化模糊聚类的流体粒子粗粒化映射：膜贡献项作为压力修正机制"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01867"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1US8EKTjTxS2OmW4-2B0mjRUPqGGQS4yxDw1yTZZuM2GpRoGGxPIriYdNQ9eYXef9zjTCW389G7b9f3SY72tEt4hHMf3t4SmRRoXv46erLP4-2B1nY41iFExQkGYoefXrQ59rUZDI_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXc2RYNe3UlLS9pq-2BEMdtMXEs8oRUs7Pon-2B4zQV6XjgAKbCQnIIBQGtKdNzKY6cmS-2ByXXEJXkbQjUc4mk20adAPQp10uYTWoNl0WXsM1JbZyT0EUjKFBxAuvilOuFjtpRYqSN3ZbA57sw8EI42QvcaiIhVknC0qbYhcZkamYgi21cj6RuuGjLEcH8-2Bjz2BdaC8Q-3D"
pub_date: ""
tags: ["coarse-graining", "fuzzy-clustering", "molecular-dynamics", "force-matching", "machine-learning"]
ai_relevance: 3
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Coarse-Grained Mapping of Fluid Particles via Evolutionary Fuzzy Clustering: Membership-Evolution Term as a Pressure Correction Mechanism

**通过演化模糊聚类的流体粒子粗粒化映射：膜贡献项作为压力修正机制**

## 精华总结
本研究提出了一种熵正则化模糊聚类方法用于流体粒子粗粒化，通过分解隶属度演化项发现了压力修正的物理起源。该方法为设计更有效的粗粒化策略提供了新的理论视角和实验证据。

**关键词**: 粗粒化、模糊聚类、压力修正、分子动力学、强制匹配

## 摘要（英文）
Coarse-graining is an effective approach for bridging atomistic and mesoscopic descriptions of fluid particle systems. However, fixed coarse-grained (CG) mappings do not account for the unbundled nature of fluid particles. We propose an entropy-regularized fuzzy clustering method with temporal smoothness constraints, examining in detail the role of the evolution of fuzzy particle-cluster membership degrees throughout the coarse-graining process. Entropy regularization controls the level of spatial fuzziness, while the temporal smoothness constraints enhance the continuity of cluster position evolution. Within a bottom-up force-matching framework, the interactions between clusters are decomposed into two contributions: a particle-interaction term, which is the weighted sum of interactions between particles, and a membership-evolution term, which originates from the temporal variation of membership degrees. Analyses based on the Lennard-Jones (L-J) fluid particle system and the water molecule system show that an intermediate level of fuzziness yields the most pronounced structural features in the radial distribution functions. The particle-interaction term exhibits system-dependent characteristics, whereas the membership-evolution term consistently provides a repulsive contribution across different systems. Moreover, CG dynamics simulations of the L-J fluid demonstrate that including the membership-evolution term effectively restores the system pressure, which could be interpreted as a pressure correction scheme. This finding provides a physical perspective on the transition from microscopic particle interactions to macroscopic fluid pressure constraints and reveals a bottom-up origin for incorporating additional pressure corrections into fluid CG dynamics, which could be beneficial for the future design of coarse-graining strategies.

## 摘要（中文）
粗粒化是连接流体粒子系统原子论和介观描述的有效方法。然而，固定的粗粒化映射不能解释流体粒子的非束缚特性。我们提出了一种具有时间平滑约束的熵正则化模糊聚类方法，详细研究了粗粒化过程中模糊粒子-簇隶属度演化的作用。熵正则化控制空间模糊程度，而时间平滑约束增强簇位置演化的连续性。在自下而上的力匹配框架内，簇之间的相互作用分解为两个贡献：粒子相互作用项（粒子间相互作用的加权和）和隶属度演化项（来自隶属度的时间变化）。基于Lennard-Jones流体粒子系统和水分子系统的分析表明，中等程度的模糊性在径向分布函数中产生最显著的结构特征。粒子相互作用项表现出系统依赖性，而隶属度演化项在不同系统中始终提供排斥贡献。此外，L-J流体的粗粒化动力学模拟表明，包含隶属度演化项能有效恢复系统压力，这可被解释为压力修正方案。该发现为从微观粒子相互作用到宏观流体压力约束的过渡提供了物理视角，揭示了将额外压力修正纳入流体粗粒化动力学的自下而上起源，这对未来粗粒化策略的设计可能有益。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1US8EKTjTxS2OmW4-2B0mjRUPqGGQS4yxDw1yTZZuM2GpRoGGxPIriYdNQ9eYXef9zjTCW389G7b9f3SY72tEt4hHMf3t4SmRRoXv46erLP4-2B1nY41iFExQkGYoefXrQ59rUZDI_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXc2RYNe3UlLS9pq-2BEMdtMXEs8oRUs7Pon-2B4zQV6XjgAKbCQnIIBQGtKdNzKY6cmS-2ByXXEJXkbQjUc4mk20adAPQp10uYTWoNl0WXsM1JbZyT0EUjKFBxAuvilOuFjtpRYqSN3ZbA57sw8EI42QvcaiIhVknC0qbYhcZkamYgi21cj6RuuGjLEcH8-2Bjz2BdaC8Q-3D)
