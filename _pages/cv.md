---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* **Ph.D. in Biomedical Engineering**, Northwestern University, Chicago, USA
  *Expected April 2026*

* **M.S.E. in Electrical Engineering (Machine Learning)**, University of Pennsylvania, Philadelphia, USA  
  *August 2017 – May 2019*

* **B.Tech. in Electrical and Electronics Engineering**, Vellore Institute of Technology, India  
  *June 2013 – May 2017*

*Relevant coursework:* Signal Processing, Machine Learning, Data Mining, Deep Learning for Biomedical Imaging, Computational Neuroscience, Brain–Machine Interfaces, Dynamical Systems

---

Research Experience
======
* **Decoding speech from neural signals (PhD thesis)**
  *Northwestern University*
  *2020 – Present*
  * Analyzed large-scale intracranial electrophysiology datasets (ECoG) from human neurosurgical recordings to study speech-related neural activity.
  * Built end-to-end pipelines for processing and aggregating neural, behavioral, and audio data across subjects and recording sessions.
  * Generated statistical analyses and visualizations to characterize neural dynamics and evaluate model performance across experimental conditions.
  * Developed machine learning models (SVM, XGBoost, contrastive learning) to decode speech-related signals and investigate phoneme-level and sequence-level representations.
  * Evaluated variability across sessions and participants, focusing on robustness and generalization in clinical datasets.
  * Supported intraoperative data collection in operating room environments, working with clinicians and engineers to ensure high-quality recordings.
  * Presented results to interdisciplinary teams, translating analytical findings into insights that informed experimental design and research direction.

* **Classification of imagined movements from neural signals**  
  * Applied feature engineering, signal processing, and machine learning methods to classify imagined limb movements.  
  * Achieved significant accuracy using ensemble classifiers including XGBoost and Random Forest.

* **Reinforcement learning based rule for optimizing neural networks**
  * Contributed to the design and testing of a reinforcement learning based algorithm for learning in Neural networks.
  * Conducted experiments with TensorFlow to optimize deep learning architectures including ANNs and CNNs for improved performance.

* **Wheelchair control via visually evoked potentials (EEG)**  
  * Acquired EEG during visual stimulation to elicit steady-state visual evoked potentials.  
  * Implemented correlation-based decoding to generate wheelchair control signals.

---

Work Experience
======
* **Research Engineer**, Feinberg School of Medicine, Northwestern University
  *May 2019 – June 2020*
  * Contributed to developing a multi-layered perceptron classifier to detect sleep stages from heart rate data, aimed to improve learning in stroke survivors by monitoring sleep patterns.
  * Analyzed EMG and neuromodulation (TMS) datasets from human studies, quantifying neural and motor responses across experimental conditions.
  * Developed data processing and visualization workflows for physiological time-series data in clinical research settings.
  * Investigated mechanisms of recovery in stroke survivors by developing a real-time electromyography (EMG) acquisition interface and a custom game using Python.
  * Implemented deep learning-based pose estimation (OpenPose) algorithm to track recovery outcomes in stroke survivors.

---

Publications
======
<ul>
{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}
</ul>

---

Talks
======
<ul>
{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html %}
{% endfor %}
</ul>

---

Teaching
======
<ul>
{% for post in site.teaching reversed %}
  {% include archive-single-cv.html %}
{% endfor %}
</ul>

---

Teaching
======
* **Graduate Teaching Assistant for Machine learning for Biomedical applications**, Northwestern University
  *March 2023 – May 2023*
  * Organized office hours to help students with projects and clarify questions about concepts and code in Python.

* **Graduate Teaching Assistant for Data Mining**, University of Pennsylvania
  *August 2018 – December 2018*
  * Designed projects for a class of 80 students. Interacted with students on a weekly basis to clarify concepts taught in class.

---

Honors and Awards
======
* Recipient of Travel Award, Brain Computer Interface Society, Belgium, June 2023

---

Technical Skills
======
* **Languages:** Python, SQL, C++, MATLAB
* **Python:** Scikit-Learn, XGBoost, PyTorch, TensorFlow, Keras, Pandas, sklearn, scipy, OpenCV, Simple-ITK, nibabel, NLTK, pygame, MistralAI, Hugging Face
* **Data Visualization Tools:** Matplotlib, Ggplot, Seaborn, Plotly
* **Other Technical Skills:** Linux, LabStreamingLayer, Git, BCI2000
