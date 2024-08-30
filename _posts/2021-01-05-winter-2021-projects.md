---
date: 2021-01-05 02:13:58+00:00
description: null
featuredImage: assets/maya/vr_screenshot_bowl_mask.png
layout: blog-post
slug: /winter-2021-projects
title: Winter 2021 Projects
author: Nathan
categories:
- news-and-updates
---
We are excited to start 2021 with a slew of active projects, continuing to explore and do research during the pandemic.  This quarter, we are looking for students to join projects ranging from creating 3D graphics visualizations of Mayan ruins to using machine learning to recognize animals from both images and their calls.  See our active recruitments [here]({{ "/open-opportunities" | absolute_url }})!

## [Maya VR]({{ "/maya-archaeology" | absolute_url }})
{% assign image = "assets/maya/vr_screenshot_bowl_mask.png" | resize: "250x250" | absolute_url %}
{% include img_caption.html
    src=image
    caption="Structure M7-1 in El Zotz, Guatemala visualized using Unreal Engine"
%}

Traditional methods of documenting findings in archaeology has been through illustrations and photographs, but archeologist now digitally archive these locations using LiDAR and Photogrammetry due to their increased accuracy. This method of creating environments has become more popular in recent years, thus we have a lot of raw data in the form of point clouds and photographs to experiment with in order to achieve the most accurate result. The goal of the project is to explore digital methods for documenting, visualizing, and sharing archeological finds to then prepare as an museum exhibition for Guatemala City.

## [Smartfin]({{ "/smartfin" | absolute_url }})
{% assign image = "assets/smartfin/internals_fullres.jpg" | resize: "250x250" | absolute_url %}
{% include img_caption.html
    src=image
    caption="Smartfin"
%}
Ocean sensing is challenging, particularly in the near shore surf zone where wave energy is at its peak.  Traditional sensing of oceanographic parameters such as wave energy and sea surface temperature are performed with a network of scientific buoys which are often miles apart.  Smartfin is a low cost surfboard mounted ocean monitoring sensor which aims to address this gap in sensing.  It consists of a microcontroller, various sensors, a battery, and a wireless radio, all housed within a custom manufactured surfboard fin.  Mounting on a surfboard provides an ideal platform for operating in the surf zone, and the density of surfers is much higher than traditional buoy sensing networks.  In addition, by distributing Smartfin units to surfing communities, we can directly engage the community with quantified data about how our coastal environments are changing.

We are working on data analysis for the sensing data to derive useful information from the raw sensor data.  First, we're looking at using the IMU to produce data, such as displacement and frequency content of waves, similar to those provided by scientific buoys. We are also looking to classify what the surfer is doing (paddling, surfing, bobbing, walking) and potentially provide statistics about the surf session.

## [Baboon Tracking]({{ "/baboons-on-the-move" | absolute_url }})
{% assign image = "assets/baboons_on_the_move/laikipia_plateau.png" | resize: "250x250" | absolute_url %}
{% include img_caption.html
    src=image
    caption="Laikipia Plateau in Kenya"
%}
Baboons are thought to live in the most complex society besides humans. They exquisitely track resources in their environment without maps, without verbal communication, without explicit collaborative objectives. One of the most complex negotiations that baboons have is deciding where to go and when to leave. Our collaborators have studied these animals for 46 years and know a great deal about most aspects of their behavior but just HOW they make troop movement decisions is still a mystery as it includes many individuals and exchanges back and forth can last up to an hour. We hope to get a peek into this mystery by applying aerial drone technology and automatically tracking the animals in the video footage. The goal of this project is to develop this tracking framework and we are looking for interested students. 

## [Acoustic Species]({{ "/acoustic-species-identification" | absolut_url }})
{% assign image = "assets/acoustic_species_id/white_winged_becard_vocalization.png" | resize: "250x250" | absolute_url %}
{% include img_caption.html
    src=image
    caption="White-Winged Becard"
%}
Biologists increasingly deploy autonomous audio recorders that are placed in natural habitats and record audio at fixed intervals (e.g. 1 minute every 5 minutes) for weeks or months. These recordings can be used to detect individual species that have unique vocalizations including birds, amphibians, bats and certain mammals such as primates. They can also detect human threats such as gunshots, chain saws, engines. For large surveys biologists can deploy 30-100 recorders simultaneously resulting in a huge volume of data. The goal of this project is to build a machine learning pipeline that can handle this kind of data and automatically detect and extract vocalizations of species of interest. The following points would need to be addressed: general data management; efficient labeling of vocalizations to be used for model training; development of models to classify sound recordings; and a pipeline to extract recordings and perform quality control. Our collaborators at the San Diego Zoo currently have data from about 80 recorders deployed in the Peruvian Amazon with close to 1 year of total recording time and we have species experts that can help with manual labeling. We are working to combine the powers of fields such as machine learning, digital signal processing, computer science, biology, and ecology to parse through and extract statistically significant indicators of ecological health from the world’s natural soundscapes that are begging to be heard.

## [Aye-Aye Sleep Monitoring](https://docs.google.com/document/d/1qhlcTJfNmHUiAad8An5oW5mIx0skUy5ZDjVEONaLAj0/edit?usp=sharing)
Aye-ayes (_Daubentonia madagascariensis_) are a species of lemur that the San Diego Zoo is working to protect and has in their care.  Aye-ayes fill a similar niche to woodpeckers - they have sharp teeth for chewing into tree trunks and branches to find their food (insect larvae, seeds, honey, etc).  Like humans, aye-ayes may have sleep problems that affect their quality of life.  However, unlike humans, aye-ayes won't willingly wear wearable sensors, so we need to find another way to measure their quality of sleep. This quarter, we are focusing on rapidly deploying a set of cameras, microphones, and vibration sensors to monitor the Aye-Ayes currently living at the San Diego Zoo in Balboa Park. We are looking for students who can contribute to the data management and analysis portion of this project.

## [Burrowing Owl Action Recognition]({{"/burrowing-owl-behavior-classification" | absolute_url}})
{% assign image = "assets/burrowing_owl/owl_thumb.png" | resize: "250x250" | absolute_url %}
{% include img_caption.html
    src=image
    caption="Burrowing Owl"
%}
The San Diego Zoo Institute for Conservation Research has a number of projects where the activities (behaviors) of animals are determined manually from videos and images captured in the field by camera traps or surveillance cameras.  For example, researchers studying burrowing owls not only keep track of the presence and number of owls and their predators in camera trap images but also record mating and predation events caught in those images. Behavior or action recognition using machine learning is a growing field with demonstrated success in a number of applications.  We are working to develop a comprehensive machine learning tool to recognize burrowing owls in their native habitats. This tool will assist scientists in understanding the burrowing owls' behavior in and around their nests. We are currently looking for students to help develop the machine learning models.

## [Radio Telemetry Tracking]({{"/radio-collar-tracker" | absolute_url}})
{% assign image = "assets/radio_collar_tracker/2020-08-20-rct_iso.jpg" | resize: "250x250" | absolute_url %}
{% include img_caption.html
    src=image
    caption="2019 Radio Tracking Drone"
%}
Current methods of radio telemetry tracking involve researchers hiking through potentially challenging terrain with a large antenna, which is a slow, difficult process to the point of not being useful in some field sites.  Over the past few years, we have built a drone and custom radio payload to tackle this challenge from the sky, avoiding all the slow bushwhacking on the ground.  We have deployed this system in the Dominican Republic and in the Cayman Islands tracking iguanas and their hatchlings, and are now looking to focus on developing this project's software components, and we are currently seeking someone to contribute to this project's system manager.
