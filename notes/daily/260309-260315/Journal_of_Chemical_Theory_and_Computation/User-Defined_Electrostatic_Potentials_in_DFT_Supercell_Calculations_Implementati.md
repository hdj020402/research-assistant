---
title: "User-Defined Electrostatic Potentials in DFT Supercell Calculations: Implementation and Application to Electrified Interfaces"
title_zh: "DFT超晶胞计算中用户自定义静电势的实现与应用：带电界面研究"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c02150"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE13tl7pXyb7pfJl4M6xOtNG2Pj692ojEeEtQD4iEqL5Mp9k93exKbKRkmCVHjRR2lJarVovBBsIHqhTXFiFrfH0X-2FXFKpOhEgsmwUfX8pe9l47JVbvROWv59DvKOt0mFbPI2zN_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXd-2Bs-2FjdZ-2B6MQcz89WplACPIUwCPIXXmRc-2Bs7Nk-2Fne4JYMs9uw2P6BsgHqJo17bn6-2F6yvjA8AyO-2FbsbwTFP93CHs4AW9LK-2BFz-2FzaiIFb4lD04DRTccTc75mIvdwXU4Fl0o39Vf7-2BF-2F94bOVMapsdbgzEz-2B6hEUI37PKLyd9tgb0rdF8qcueYmOYCAGgUmJ5VthA-3D"
pub_date: ""
tags: ["dft-methods", "electrochemistry", "computational-materials", "interface-simulation"]
ai_relevance: 2
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# User-Defined Electrostatic Potentials in DFT Supercell Calculations: Implementation and Application to Electrified Interfaces

**DFT超晶胞计算中用户自定义静电势的实现与应用：带电界面研究**

## 精华总结
通过VASP-Python接口在标准VASP软件中实现用户自定义电场的直接应用，为电化学过程和带电界面的DFT研究提供了灵活高效的工具。

**关键词**: DFT计算、静电势、电化学界面、VASP-Python接口、带电表面

## 摘要（英文）
Introducing electric fields into density functional theory (DFT) calculations is essential for understanding electrochemical processes, interfacial phenomena, and the behavior of materials under applied bias. However, applying user-defined electrostatic potentials in DFT is nontrivial and often requires direct modification to the specific DFT code. In this work, we present an implementation for supercell DFT calculations under arbitrary electric fields and discuss the required corrections to the energies and forces. The implementation is realized through the recently released VASP-Python interface, enabling the application of user-defined fields directly within the standard VASP software and providing great flexibility and control. We demonstrate the application of this approach with diverse case studies, including molecular adsorption on electrified surfaces, field ion microscopy, electrochemical solid-water interfaces, and implicit solvent models.

## 摘要（中文）
本工作介绍了在任意电场下进行超晶胞DFT计算的实现方法，并讨论了能量和力的必要修正。通过新发布的VASP-Python接口实现该方法，使得用户可在标准VASP软件中直接应用自定义电场，提供了更大的灵活性和控制力。通过分子在带电表面吸附、场离子显微镜、电化学固液界面和隐式溶剂模型等多个应用案例验证了该方法的有效性。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE13tl7pXyb7pfJl4M6xOtNG2Pj692ojEeEtQD4iEqL5Mp9k93exKbKRkmCVHjRR2lJarVovBBsIHqhTXFiFrfH0X-2FXFKpOhEgsmwUfX8pe9l47JVbvROWv59DvKOt0mFbPI2zN_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXd-2Bs-2FjdZ-2B6MQcz89WplACPIUwCPIXXmRc-2Bs7Nk-2Fne4JYMs9uw2P6BsgHqJo17bn6-2F6yvjA8AyO-2FbsbwTFP93CHs4AW9LK-2BFz-2FzaiIFb4lD04DRTccTc75mIvdwXU4Fl0o39Vf7-2BF-2F94bOVMapsdbgzEz-2B6hEUI37PKLyd9tgb0rdF8qcueYmOYCAGgUmJ5VthA-3D)
