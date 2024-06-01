---
date: 2015-08-07 21:36:19+00:00
featuredImage: /assets/2015-08-07-aero-carlsbad.jpg
layout: blog-post
slug: /flight-testing-for-vaquita-aerial-surveys
title: Flight Testing for Vaquita Aerial Surveys
author: Antonella Wilby
categories:
- vaquita
gallery:
- /assets/2015-08-07-img01.jpg
- /assets/2015-08-07-img02.jpg
- /assets/2015-08-07-img03.jpg
- /assets/2015-08-07-img04.jpg
- /assets/2015-08-07-img05.jpg
- /assets/2015-08-07-img06.jpg
- /assets/2015-08-07-img07.jpg
- /assets/2015-08-07-img08.jpg
- /assets/2015-08-07-img09.jpg
- /assets/2015-08-07-img10.jpg
- /assets/2015-08-07-img11.jpg
- /assets/2015-08-07-img12.jpg
---
We recently completed initial flight testing of the fixed-wing aerial platform we will deploy in Mexico to survey [vaquita]({{'/vaquita' | absolute_url}}), a critically-endangered porpoise. Our platform consists of a modified 3D Robotics Aero plane outfitted with a Sony QX1 camera for taking high-resolution aerial imagery of the vaquita habitat. This approach will allow scientists and conservationists to perform aerial transects for population studies at a much lower cost than with manned aircraft.

<figure>
<a href="{{'/assets/2015-08-07-aero-black-mtn.jpg' | absolute_url}}"><img src="{{'/assets/2015-08-07-aero-black-mtn.jpg' | resize: '1024x768'}}" alt="Aero being tested in the field for flight-readiness"></a>
<figcaption>Aero being tested in the field for flight-readiness</figcaption>
</figure>

After a successful over-land flight-readiness test at Black Mountain in Poway, we flew the Aero platform over the ocean in Carlsbad, California to take aerial imagery of the ocean and coastline.

<figure>
<a href="{{'/assets/2015-08-07-aero-ocean.jpg' | absolute_url}}"><img src="{{'/assets/2015-08-07-aero-ocean.jpg' | resize: '1024x768'}}" alt="Aero flying over ocean taking aerial photos of surfers"></a>
<figcaption>Aero flying over ocean taking aerial photos of surfers</figcaption>
</figure>

Since this was an initial test, we did not set up specific imaging targets. However, there were surfers in the water below, which gave some idea of the size of objects that can be resolved in our aerial photographs. In upcoming local testing, we will place targets in the water which will represent vaquita and other marine life, to see how effective our platform is at photographing them during a fly-over. These targets will also allow us to evaluate how far below the water surface we can see with our cameras. We will also continue to investigate what flight conditions - e.g. weather, lighting, wind, and waves - allow us to generate the best imagery, in order to be most efficient with our flight deployments once we are in the field.

Our plane also captured a picture of our field team while in the air, as seen in the photo below. As a reference, the person in blue in the upper left-hand corner of the photo is roughly the same size as an adult vaquita, which grow to approximately five feet in length.

<figure>
<a href="{{'/assets/2015-08-07-aero-field-team.jpg' | absolute_url}}"><img src="{{'/assets/2015-08-07-aero-field-team.jpg' | resize: '1024x768'}}" alt="Field team as seen from Aero camera"></a>
<figcaption>Field team as seen from Aero camera</figcaption>
</figure>

Over the next few months, we will continue to refine our fixed-wing aerial imaging platforms, in order to deploy them in the Gulf of California after the monsoon season ends.

{% for image in page.gallery %}
<a href="{{ image | absolute_url }}">
<img alt="gallery" src="{{ image | resize: '150x150' }}" width="150px" height="150px">
</a>{% endfor %}