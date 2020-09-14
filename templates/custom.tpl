{%- extends 'basic.tpl' -%}

{% block body %}
  {% for css in resources.inlining.css -%}
      <style type="text/css" scoped="true">
      {{ css }}
      </style>
  {% endfor %}
{{ super() }}
{%- endblock body %}

{% block output_area_prompt %}
<div class="prompt output_prompt">Out&nbsp;[{{cell.execution_count}}]:</div>
{% endblock output_area_prompt %}

{% block footer %}
{{ super() }}
{% endblock footer %}
