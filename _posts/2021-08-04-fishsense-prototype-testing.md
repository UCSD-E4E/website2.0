---
date: 2021-08-04 16:02:13+00:00
description: null
featuredImage: assets/fishsense/2021-08-04-fs-legacy.jpg
layout: blog-post
slug: /fishsense-prototype-testing
title: FishSense Prototype Testing
author: Peter Tueller
categories:
- news-and-updates
---
{% assign image = "assets/fishsense/2021-08-04-fs-legacy-birch.jpg" | resize: "1074x716" | absolute_url %}
{% include img_caption.html
    src=image
    caption="Birch Aquarium at Scripps Institution of Oceanography | aquarium.ucsd.edu"
%}

On July 22nd, 2021, Peter Tueller, Maddie Bland, and Ronan Wallace deployed a prototype of the FishSense platform in the Giant Kelp Forest Exhibit at Birch Aquarium at Scripps Institute of Oceanography at UC San Diego. The prototype, which uses the Intel RealSense D455 camera to capture RGBD images of fish for length and biomass measurements, had only been tested in an isolated tank with a toy fish as the target. This deployment collected more realistic data of multiple species of fish in slightly more realistic conditions, and is an important step towards deployment in real world applications. We plan to deploy the system next in aquaculture tanks as well as shallow waters surrounding mangrove forests in Mexico and Jamaica.

{% assign image1 = "assets/fishsense/2021-08-04-birch-fish-1.png" | resize: "512x288" | absolute_url %}
{% assign image2 = "assets/fishsense/2021-08-04-birch-fish-depthmap.jpg" | resize: "402x228" | absolute_url %}
{% include img_caption.html
    src=image1
    src2=image2
    caption="A color (left) and depth (right) image pair"
    %}

{$ assign image = "assets/fishsense/2021-08-04-grouper-yolov4.png" | resize: "512x288" | absolute_url %}
{% include img_caption.html
    src=image
    caption="Fish detection using YOLOv4"
    %}

The data we gathered at Birch Aquarium at Scripps also helped us finalize and submit the project's first accepted paper at the OCEANS'21 conference, which takes place right here in San Diego, September 20-23, 2021. You can read the full paper here: [https://kastner.ucsd.edu/wp-content/uploads/2021/08/admin/oceans21fishsense.pdf](https://kastner.ucsd.edu/wp-content/uploads/2021/08/admin/oceans21fishsense.pdf).
