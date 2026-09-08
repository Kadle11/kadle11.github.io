---
layout: homepage
---

<div class="intro-section">
  <div class="intro-photo">
    <img class="profile-picture" src="{{ site.avatar }}" alt="Profile photo of {{ site.title }}" />
  </div>
  <div class="intro-text">
    <div class="intro-unit">
      I am a fourth-year Ph.D. student in Computer Science at the
      <a href="https://www.gatech.edu/">Georgia Institute of Technology</a>, advised by
      <a href="https://sites.cc.gatech.edu/home/ada/">Prof. Ada Gavrilovska</a>.
    </div>

    <div class="intro-unit">
      I work on memory disaggregation, vector databases, and systems for AI and
      emerging hardware. My current work explores memory disaggregation and
      near-data processing for datacenter and graph analytics workloads.
    </div>

    <div class="intro-unit">
      During my Ph.D. I have interned at SoLab,
      <a href="https://www.skhynix.com/">SK Hynix America</a> (Fall 2026), and at the
      Systems Architecture Lab, <a href="https://www.hpe.com/us/en/hewlett-packard-labs.html">HPE Labs</a> (2025).
    </div>

    <div class="intro-unit">
      Earlier, I was on the GeForce Now team at
      <a href="https://www.nvidia.com/">Nvidia</a> and in the Server Performance Group at
      <a href="https://www.amd.com/">AMD</a>.
    </div>

    <div class="intro-unit intro-links">
      <span class="email">{{ site.email }}</span> ·
      {% if site.cv_link %}<a href="{{ site.cv_link }}" target="_blank" rel="noopener">CV</a> · {% endif %}
      <a href="{{ site.google_scholar }}">Scholar</a> ·
      <a href="{{ site.github_link }}">GitHub</a> ·
      <a href="{{ site.linkedin }}">LinkedIn</a>
    </div>
  </div>
</div>

{% include news.html %}

{% include publications.html %}

{% include awards.html %}

{% include service.html %}

{% include teaching.html %}

{% include talks.html %}
