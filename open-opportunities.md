---

title: Open Opportunities - Academic Year
layout: page
---
For these academic year opportunities, please apply at [{{'/join' | absolute_url}}]({{'/join' | absolute_url}}) and specify the opportunity you are interested in. Our next round of applications will be processed at the start of the academic quarter. Keep in mind that projects do recruit outside of these opportunities as well.

{% assign opportunities = site.data.opportunities | sort: "project" %}
{% for position in opportunities %}
## {% if position.link %}[{% endif %}{{ position.project }} - {{ position.title }}{% if position.link %}]({{position.link}}){% endif %}
{{ position.description }}

{% if position.required %}
**Required Skills**
{% for skill in position.required %}
- {{ skill }}
{% endfor %}
{% endif %}

{% if position.desired %}
**Desired Skills**
{% for skill in position.desired %}
- {{ skill }}
{% endfor %}
{% endif %}

{% endfor %}

