<h2 id="publications" style="margin: -5px 0px 2px;">Service/Teaching</h2>

<h4 style="margin:0 10px 0;">Artificat Evaluation Committees</h4>
<ul style="margin:0 0 5px;">
  {% for reviewer in site.data.services.main.artifact_evaluation_committees %}
    <li><autocolor>{{ reviewer.name }} {{ reviewer.years }}</autocolor></li>
  {% endfor %}
</ul>

<h4 style="margin:0 10px 0;">Teaching Assistantships</h4>
<ul style="margin:0 0 20px;">
  {% for reviewer in site.data.services.main.teaching %}
    <li><autocolor>{{ reviewer.name }} {{ reviewer.years }}</autocolor></li>
  {% endfor %}
</ul>