---
title: Onboarding Papers
layout: page
papers:
- bib_file: acoustic_species_id
  name: Acoustic Species ID
  url: /acoustic-species-identification
- bib_file: fishsense
  name: FishSense
  url: /fishsense
- bib_file: mangrove_monitoring
  name: Mangrove Monitoring
  url: /mangrove-monitoring
- bib_file: radio_telemetry_tracking
  name: Radio Telemetry Tracking
  url: /radio-collar-tracker
- bib_file: smartfin
  name: Smartfin
  url: /smartfin
- bib_file: support_group
  name: Research Support Group
  url: /research-support-group
---
Below are some good papers for each project that will help you get a feel for what the project is about.

{% for project in page.papers %}
# [{{ project.name }}]({{ project.url | absolute_url }})
{% capture bib_file %}onboarding_papers/{{project.bib_file}}{% endcapture %}
{% bibliography --file {{bib_file}} %}
{% endfor %}
