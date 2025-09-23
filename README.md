# Project Overview

This repository contains the implementation and results from the paper:  
**RBMD: RoBERTa-Based Module Detection in Multi-Programming Language Software Systems**  
**Cite this work**: [https://doi.org/10.1109/ICWR65219.2025.11006198](https://doi.org/10.1109/ICWR65219.2025.11006198)

---

## Abstract

The dynamic nature of web and software systems requires modularization methods that can adapt to frequent updates and diverse structures while maintaining scalability and efficiency. In this research, we propose a RoBERTa-based Module Detection (RBMD) framework that leverages transformer models to classify and manage software modules using the semantic content of source code, comments, and related textual data. Unlike traditional dependency graph-based methods, our content-driven approach offers a streamlined, scalable solution for software systems. This repository contains code, datasets, and evaluation results for the RBMD framework.

---

## Software Evaluations

This repository provides module detection results for three open-source software systems:

1. **Chromium**
2. **Mozilla 3.7**
3. **Mozilla 134**

Each folder contains the following:
- A `target` folder
- Two Python scripts: `Copy.py` and `roberta.py`

---

### Details

#### Chromium
- **Source**: [https://github.com/chromium/chromium](https://github.com/chromium/chromium)  
- **Results**: Achieved an outstanding accuracy and F1-score of **99.70%** after training.  
- **Details**: The `Copy.py` script filters and organizes data from 10 folders based on specific files.

#### Mozilla 3.7 (Developer Version)
- **Source**: [https://ftp.mozilla.org/pub/firefox/releases/devpreview/1.9.3a4/source/](https://ftp.mozilla.org/pub/firefox/releases/devpreview/1.9.3a4/source/)  
- **Source Paper**: [https://doi.org/10.1016/j.compeleceng.2019.106500](https://doi.org/10.1016/j.compeleceng.2019.106500)  
- **Results**: Achieved **92.55% accuracy** and **92.47% F1-score** after four epochs.  

#### Mozilla 134
- **Source**: [https://github.com/mozilla/gecko-dev/tree/master](https://github.com/mozilla/gecko-dev/tree/master)  
- **Results**: Achieved **98.13% accuracy** and **98.02% F1-score** with rapid convergence and minimal training loss.  

---

## Authors  

- [Masoud Kargar](https://scholar.google.com/citations?user=RtGIpEkAAAAJ&hl=en)  
- [Shahin Sharbaf Movassaghpour](https://scholar.google.com/citations?user=FHZWfc4AAAAJ&hl=en)  
- [Ali Bayani](https://scholar.google.com/citations?user=bACdbPYAAAAJ&hl=en)  


## Citation

Kargar, Masoud, Shahin Sharbaf Movassaghpour, and Ali Bayani. "RBMD: RoBERTa-Based Module Detection in Multi-Programming Language Software Systems." In 2025 11th International Conference on Web Research (ICWR), pp. 66-73. IEEE, 2025.


&copy; 2025 Masoud Kargar
