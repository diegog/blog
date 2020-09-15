{%- extends 'basic.tpl' -%}

{% block output_area_prompt %}
<div class="prompt output_prompt">Out&nbsp;[{{cell.execution_count}}]:</div>
{% endblock output_area_prompt %}

{% block footer %}
{{ super() }}
{% endblock footer %}
