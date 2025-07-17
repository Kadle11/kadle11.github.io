<h2 id="publications" style="margin: 2px 0px -15px;">News</h2>

<div class="newsbar-vertical-scroll">
<ol class="new-items">

{% for item in site.data.news.main %}
<li>
  <div class="newsbar-row">
    <div class="col-sm-9" style="position: relative;padding-right: 15px;padding-left: 20px;">
      <div class="title"><strong>[{{ item.date }}]</strong> {{ item.desc }}</div>
    </div>
  </div>
</li>
<br>
{% endfor %}

</ol>
</div> 