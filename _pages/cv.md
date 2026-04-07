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

<style>
.first-author-pub .archive__item-title a::before {
  content: "★ ";
  color: #d62728;
}
html[data-theme="dark"] .first-author-pub .archive__item-title a::before {
  color: #ff6b6b;
}
.first-author-pub {
  border-left: 3px solid #d62728;
  padding-left: 10px;
  margin-bottom: 8px;
}
html[data-theme="dark"] .first-author-pub {
  border-left-color: #ff6b6b;
}
</style>

**First-Author**

<ul>
{% for post in site.publications reversed %}
  {% if post.first_author == true %}
  <div class="first-author-pub">
    {% include archive-single-cv.html %}
  </div>
  {% endif %}
{% endfor %}
</ul>

**Other Publications**

<ul>
{% for post in site.publications reversed %}
  {% if post.first_author != true %}
    {% include archive-single-cv.html %}
  {% endif %}
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

<style>
.skill-category {
  margin-bottom: 18px;
}
.skill-category-title {
  font-weight: 600;
  margin-bottom: 8px;
  color: #333;
}

html[data-theme="dark"] .skill-category-title {
  color: #eaeaea;
}

.skill-badge {
  display: inline-block;
  background: #1f77b4;
  color: white;
  padding: 6px 12px;
  margin: 4px 6px 4px 0;
  border-radius: 20px;
  font-size: 0.9em;
  font-weight: 500;
  transition: all 0.2s ease;
}

.skill-badge:hover {
  opacity: 0.85;
  transform: translateY(-2px);
}

.skill-badge.ml {
  background: #ff7f0e;
}

.skill-badge.viz {
  background: #2ca02c;
}

.skill-badge.other {
  background: #9467bd;
}

html[data-theme="dark"] .skill-badge        { background: #1e6fb8; }
html[data-theme="dark"] .skill-badge.ml    { background: #e67e22; }
html[data-theme="dark"] .skill-badge.viz   { background: #27ae60; }
html[data-theme="dark"] .skill-badge.other { background: #8e44ad; }
</style>

<div class="skill-category">
  <div class="skill-category-title">Languages</div>
  <span class="skill-badge">Python</span>
  <span class="skill-badge">SQL</span>
  <span class="skill-badge">C++</span>
  <span class="skill-badge">MATLAB</span>
</div>

<div class="skill-category">
  <div class="skill-category-title">Machine Learning & Deep Learning</div>
  <span class="skill-badge ml">PyTorch</span>
  <span class="skill-badge ml">TensorFlow</span>
  <span class="skill-badge ml">Scikit-Learn</span>
  <span class="skill-badge ml">XGBoost</span>
  <span class="skill-badge ml">Keras</span>
  <span class="skill-badge ml">Hugging Face</span>
  <span class="skill-badge ml">MistralAI</span>
</div>

<div class="skill-category">
  <div class="skill-category-title">Data Processing & Analysis</div>
  <span class="skill-badge">Pandas</span>
  <span class="skill-badge">NumPy</span>
  <span class="skill-badge">SciPy</span>
  <span class="skill-badge">OpenCV</span>
  <span class="skill-badge">SimpleITK</span>
  <span class="skill-badge">nibabel</span>
  <span class="skill-badge">NLTK</span>
</div>

<div class="skill-category">
  <div class="skill-category-title">Visualization</div>
  <span class="skill-badge viz">Matplotlib</span>
  <span class="skill-badge viz">Seaborn</span>
  <span class="skill-badge viz">Plotly</span>
  <span class="skill-badge viz">Ggplot</span>
</div>

<div class="skill-category">
  <div class="skill-category-title">Specialized Tools</div>
  <span class="skill-badge other">LabStreamingLayer</span>
  <span class="skill-badge other">BCI2000</span>
  <span class="skill-badge other">Linux</span>
  <span class="skill-badge other">Git</span>
  <span class="skill-badge other">MLFlow</span>
  <span class="skill-badge other">SLURM</span>
</div>
