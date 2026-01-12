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
  *Expected February 2026*

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
  * Led collection of human intracortical neural recordings (ECoG and microelectrode arrays) during speech production tasks.  
  * Designed synchronization pipelines across neural, audio, and behavioral acquisition systems.  
  * Developed signal processing and machine learning pipelines to decode speech intent from neural activity.  
  * Integrated language-model-based approaches to capture phoneme sequence dynamics during word production.

* **Classification of imagined movements from neural signals**  
  * Applied feature engineering, signal processing, and machine learning methods to classify imagined limb movements.  
  * Achieved significant accuracy using ensemble classifiers including XGBoost and Random Forest.

* **Reinforcement-learning-based optimization of neural networks**  
  * Contributed to the design of reinforcement-learning-based training rules for neural networks.  
  * Evaluated ANN and CNN architectures using TensorFlow.

* **Wheelchair control via visually evoked potentials (EEG)**  
  * Acquired EEG during visual stimulation to elicit steady-state visual evoked potentials.  
  * Implemented correlation-based decoding to generate wheelchair control signals.

---

Work Experience
======
* **Research Engineer**, Feinberg School of Medicine, Northwestern University  
  *May 2019 – June 2020*  
  * Developed a multilayer perceptron classifier to infer sleep stages from heart-rate data in stroke survivors.  
  * Built a real-time EMG acquisition interface and a custom rehabilitation game in Python.  
  * Applied deep-learning-based pose estimation (OpenPose) to quantify motor recovery outcomes.

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

Honors and Awards
======
* Travel Award Recipient, Brain–Computer Interface Society, 2023

---

Technical Skills
======
* **Programming:** Python, MATLAB, C++, SQL  
* **Machine Learning:** PyTorch, TensorFlow, Keras, scikit-learn, XGBoost  
* **Neural & Signal Processing:** EEG, ECoG, EMG, BCI2000, LabStreamingLayer  
* **Data & Visualization:** Pandas, NumPy, Matplotlib, Seaborn, Plotly  
* **Other:** Linux, Git
