---
title: "User-Defined Electrostatic Potentials in DFT Supercell Calculations: Implementation and Application to Electrified Interfaces"
title_zh: "DFT超晶胞计算中用户自定义静电势的实现与应用于电化学界面"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c02150"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE13tl7pXyb7pfJl4M6xOtNG2Pj692ojEeEtQD4iEqL5Mp9k93exKbKRkmCVHjRR2lJarVovBBsIHqhTXFiFrfH0X-2FXFKpOhEgsmwUfX8pe9l47JVbvROWv59DvKOt0mFbPI2zN_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXd-2Bs-2FjdZ-2B6MQcz89WplACPIUwCPIXXmRc-2Bs7Nk-2Fne4JYMs9uw2P6BsgHqJo17bn6-2F6yvjA8AyO-2FbsbwTFP93CHs4AW9LK-2BFz-2FzaiIFb4lD04DRTccTc75mIvdwXU4Fl0o39Vf7-2BF-2F94bOVMapsdbgzEz-2B6hEUI37PKLyd9tgb0rdF8qcueYmOYCAGgUmJ5VthA-3D"
pub_date: ""
tags: ["dft-calculations", "electrochemical-interfaces", "electric-fields", "computational-chemistry", "vasp-modeling"]
ai_relevance: 2
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# User-Defined Electrostatic Potentials in DFT Supercell Calculations: Implementation and Application to Electrified Interfaces

**DFT超晶胞计算中用户自定义静电势的实现与应用于电化学界面**

## 精华总结
通过最新发布的VASP-Python接口实现了用户自定义电场在标准VASP软件中的直接应用,提供了高度的灵活性和控制能力。该方法可广泛应用于电化学界面和材料偏置行为的研究。

**关键词**: DFT计算、电场、超晶胞、电化学界面、VASP

## 摘要（英文）
Introducing electric fields into density functional theory (DFT) calculations is essential for understanding electrochemical processes, interfacial phenomena, and the behavior of materials under applied bias. However, applying user-defined electrostatic potentials in DFT is nontrivial and often requires direct modification to the specific DFT code. In this work, we present an implementation for supercell DFT calculations under arbitrary electric fields and discuss the required corrections to the energies and forces. The implementation is realized through the recently released VASP-Python interface, enabling the application of user-defined fields directly within the standard VASP software and providing great flexibility and control. We demonstrate the application of this approach with diverse case studies, including molecular adsorption on electrified surfaces, field ion microscopy, electrochemical solid-water interfaces, and implicit solvent models.

## 摘要（中文）
本工作针对DFT计算中引入电场以理解电化学过程和界面现象的需求,通过VASP-Python接口实现了任意电场下的超晶胞DFT计算方法,讨论了能量和力的必要修正。该方法具有高度灵活性,在分子吸附、场离子显微镜、电化学固液界面和隐式溶剂模型等多个体系中得到验证。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE13tl7pXyb7pfJl4M6xOtNG2Pj692ojEeEtQD4iEqL5Mp9k93exKbKRkmCVHjRR2lJarVovBBsIHqhTXFiFrfH0X-2FXFKpOhEgsmwUfX8pe9l47JVbvROWv59DvKOt0mFbPI2zN_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXd-2Bs-2FjdZ-2B6MQcz89WplACPIUwCPIXXmRc-2Bs7Nk-2Fne4JYMs9uw2P6BsgHqJo17bn6-2F6yvjA8AyO-2FbsbwTFP93CHs4AW9LK-2BFz-2FzaiIFb4lD04DRTccTc75mIvdwXU4Fl0o39Vf7-2BF-2F94bOVMapsdbgzEz-2B6hEUI37PKLyd9tgb0rdF8qcueYmOYCAGgUmJ5VthA-3D)
