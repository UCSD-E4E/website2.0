---
title: Onboarding Papers
layout: page
papers:
- bib_file: acoustic_species_id
  name: Acoustic Species ID
  url: /acoustic-species-identification
# - bib_file: Baboons_on_the_Move
#   name: Baboons on the Move
#   url: /baboons-on-the-move
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
# - bib_file: aye-aye
#   name: Aye-Aye Sleep Monitoring
#   url: /aye-aye-sleep-monitoring
- bib_file: support_group
  name: Research Support Group
  url: /research-support-group
---
{% for project in page.papers %}
# [{{ project.name }}]({{ project.url | absolute_url }})
{% capture bib_file %}onboarding_papers/{{project.bib_file}}{% endcapture %}
{% bibliography --file {{bib_file}} %}
{% endfor %}
