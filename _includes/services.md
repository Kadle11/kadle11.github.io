<h2 id="publications" style="margin: 2px 0px -15px;">Service/Teaching</h2>

<h4 style="margin:0 10px 0;">Artificat Evaluation Committees</h4>
<ol class="bibliography">

  {% for reviewer in site.data.services.main.artifact_evaluation_committees %}
    <li><autocolor>{{ reviewer.name }} {{ reviewer.years }}</autocolor></li>
  {% endfor %}
</ol>

<h4 style="margin:0 10px 0;">Teaching Assistantships</h4>
<ol class="bibliography">
  {% for reviewer in site.data.services.main.teaching %}
    <li><autocolor>{{ reviewer.name }} {{ reviewer.years }}</autocolor></li>
  {% endfor %}
</ol>
