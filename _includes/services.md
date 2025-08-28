# Service/Teaching

<div class="services">
  <h4 style="margin:0 10px 0;">Artifcat Evaluation Committees</h4>
  <ol class="svc-item">

    {% for reviewer in site.data.services.main.artifact_evaluation_committees %}
      <li><autocolor>{{ reviewer.name }} {{ reviewer.years }}</autocolor></li>
    {% endfor %}
  </ol>

  <h4 style="margin:0 10px 0;">Teaching Assistantships</h4>
  <ol class="svc-item">
    {% for reviewer in site.data.services.main.teaching %}
      <li><autocolor>{{ reviewer.name }} {{ reviewer.years }}</autocolor></li>
    {% endfor %}
  </ol>
</div>