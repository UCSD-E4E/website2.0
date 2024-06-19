---
date: 2021-09-16 05:45:25+00:00
description: null
featuredImage: assets/acoustic_species_id/2021-08-04_scripps_coastal_reserve_trail.jpg
layout: blog-post
slug: /scripps-coastal-reserve-deployment
title: Scripps Coastal Reserve Deployment
author: Nathan
categories:
- news-and-updates
tags:
- acoustic-species
- bioacoustics
- deployment
- scripps-coastal-reserve
---
The Scripps Coastal Reserve is part of California’s delicate coastal ecosystem lost to construction and property development. Despite the size, the reserve is home to about a hundred different bird species like the endangered California gnatcatcher (_P. californica_), whose homestead in the coastal sage scrub is being upended throughout the state. Thus, as humans step in, we must monitor these critical species to ensure their survival.

{% assign image1 = "assets/acoustic_species_id/2021-08-04_jacob_searching.jpg" | resize: "512x288" | absolute_url %}
{% assign image2 = "assets/acoustic_species_id/California-Gnatcatcher.jpg" | resize: "512x288" | absolute_url %}
{% include img_caption.html 
    src=image1
    src2=image2 %}

Since birds are difficult to identify by sight and the fact the reverse itself is a 5 minute walk from UCSD, the reserve became a natural choice for E4E's Acoustic Species Identification team's first field deployment. Before the deployment, the team focused on creating automated techniques for segmenting and identifying bird calls in audio data. The reserve provided the opportunity to test our team’s systems against anthropogenic noise and monitor local species.

The project lead on the Acoustic Species Identification team, Jacob Ayers, reached out to Isabelle Kay of the UC Nature Reserve system to learn more about the species on the reserve, and reserved times in August of 2021 to set up the deployment. Thanks to her help, a team of 3 undergrad E4E students came together to launch the deployment. On the team were Sean Perry, Mugen Blue, and Jacob Ayers.

{% include img_caption.html
    src="assets/acoustic_species_id/2021-08-10_audiomoth.jpg"
    caption="Audiomoth Device" %}

The plan for the deployment was to place 13 Audiomoths devices, microphones designed specifically for collecting ecological audio data at sampled intervals, across the reserve from August 10th to August 24th. For the two weeks, the Audiomoths would record 1 minute of audio every 10 minutes, thus getting a sample of audio data throughout the day.

Before the Audiomoth deployment, the team went out to the site to scout potential locations to evenly and securely set up Audiomoths.  Each time the team decided on a location, there would be a chorus of coordinates shouted across to the other members to record the location of each device as accurately as possible.

<iframe loading="lazy" width="560" height="315" src="https://www.youtube.com/embed/mT7LQ7s3GH8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe>

While preparing to get the coordinates of Audiomoth PHO1, the team also managed to spot and record a video of a California thrasher (_T. redivivum_), a known mimic bird in the region like a mockingbird.

{% include img_caption.html
    src="assets/acoustic_species_id/2021-08-10_mugen_blue_looking_at_audiomoth.jpg"
    caption="Mugen Blue configuring an Audiomoth" %}

On August 10th, the team drove up again to the reserve to place the Audiomoths. Together, the three undergraduate students nervously checked the devices to ensure everything was configured correctly. Had one of the Audiomoths been misconfigured or, worse, not turned on, then the team would lose out on hours of audio data. After a thorough round of double checks, the team set out, following the path they previously scouted out. At each site, an Audiomoth was removed from the backpack, branded with bright red electrical tape and labels like "OFF0", "PHO1", or "OTH1". Then, they were strapped or painter taped to sage scrub and lemonade berry bushes, around which birds frequently sat and sang.

{% include img_caption.html
    src="assets/acoustic_species_id/2021-08-10_jacob_placing_audiomoth.jpg"
    caption="Jacob Ayers deploying and Audiomoth" %}

And of course, they did a neat photoshoot with the ocean in the background. How could they be near the ocean and not take a cool picture like this?

{% include img_caption.html
    src="assets/acoustic_species_id/2021-08-10_expedition_team.jpg"
    caption="Summer 2021 Acoustic Species ID team. Left to right: Sean Perry (UC San Diego), Jacob Ayers (UC San Diego), Mugen Blue (CalPoly SLO)" %}

By early afternoon on August 10th, the team had successfully deployed ten Audiomoth devices to collect the Coastal Reserve Soundscape. Three Audiomoths didn't end up getting deployed.

On August 24th, the team returned to the site. In the mists of the dry season, the team retraced their steps for the 3rd and final time, picking up the Audiomoths from the brush, ever so carefully so as not to disturb the environment around them. There were some worries that the Audiomoths suffered water damage from late-night rainstorms during the deployment. Who knows if the devices fell off their branches to be swept by the rainwater or perhaps carried off by some animal or some other worst-case scenario where we would lose our brand new devices. Luckily, every Audiomoth was still on the same branch and twig they were originally attached to 2 weeks prior. The team successfully retrieved all of the Audiomoths and were additionally relieved to see they were still recording audio. The devices were taken back to Engineers for Exploration’s Sealab. The data was stored away on a server for simple access to run our segmentation algorithms on. In total, the team collected about 926 GB of data, roughly 336 hours of audio data.

Now, comes the hard part. The team is currently working to use and refine our automated techniques in the python package PyHa to identify species, calls, and filter out human noise. When that work is finished, we may have a system capable of detecting those critical species and judging their presence on the reserve. With that system, we can launch other deployments in reserves across the city where we can see if Gnatcatchers are reclaiming habitat in restored lagoons or if other bird species are loudly making their home. With time and future deployments, the team will have a system to help monitor the ecological soundscape of San Diego and help members of the animal kingdom be heard.

If you are interested in learning more about the project, check out our project page at [{{ "/acoustic-species-identification" | absolute_url }}]({{ "/acoustic-species-identification" | absolute_url }}) and our video documenting the deployment and the life of our project lead ([https://youtu.be/buHjodMuxvw](https://youtu.be/buHjodMuxvw)).
