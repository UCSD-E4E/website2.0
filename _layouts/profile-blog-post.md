---
layout: blog-post
date: {{page.date}}
description: {{page.description}}
featuredImage: {{page.featuredImage}}
slug: {{page.slug}}
title: {{page.title}}
author: {{page.author}}
categories: {{page.categories}}
---

{{page.content}}

<h2> Student Researchers </h2>

{% for student in page.students %}
<div class="floatclearfix">
    {% if student.photo %}
    <p style="display: flex; justify-content: center;"><a href="{{ student.photo | absolute_url }}"><img alt="{{student.name}}" class="{{student.align}}" src="{{student.photo | resize: '180x240,webp,100'}}"></a></p>{% endif %}
    <p>{{student.bio}}</p>
</div>
{% endfor %}

{% if page.mentors %}
    <h2> Mentors </h2>
    {% for student in page.mentors %}
    <div class="floatclearfix">
        {% if student.photo %}
        <p style="display: flex; justify-content: center;"><a href="{{ student.photo | absolute_url }}"><img alt="{{student.name}}" class="{{student.align}}" src="{{student.photo | resize: '180x240,webp,100'}}"></a></p>{% endif %}
        <p>{{student.bio}}</p>
    </div>
    {% endfor %}
{% endif %}