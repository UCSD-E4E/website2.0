---
layout: project
permalink: /fishsense-lite
title: FishSense Lite – Citizen Science for Smarter Fisheries
category: fishsense, fishsense-lite
enable_nav: false
---

Monitoring fish populations is essential for understanding ecosystem health and supporting effective fisheries management. Many existing assessment techniques rely on **capture-and-release methods** or **manual diver surveys**, which can be time-intensive and introduce uncertainty. Collaborators at the **Scripps Institution of Oceanography** and the **Reef Environmental Education Foundation (REEF)** are particularly interested in tracking **fish length distributions over time**, an important indicator of population structure and long-term trends.

At REEF, FishSense Lite forms the technical basis of the **SMILE Project** ([reef.org/SMILE](https://www.reef.org/SMILE)), a citizen science initiative focused on improving fish length data collection during diver-based surveys. To date, **ten FishSense Lite units have been deployed with REEF** to support ongoing field use and evaluation.

{% include 
    img_caption.html
    src="assets/fishsense/fishsense-lite-system.png"
    caption="FishSense Lite prototype module."
%}

In many current survey workflows, fish length data are collected by trained divers who visually estimate and record the size of individual fish. While this approach is widely used, it depends heavily on observer experience and can vary across individuals and survey sites. FishSense Lite explores whether a **lightweight, diver-deployable imaging system** can help support and augment these surveys by enabling more consistent length estimates.

{% include 
    img_caption.html
    src="assets/fishsense/2023-07-17_nathan_fishsense_lite.jpg"
    caption="Diver using the FishSense Lite camera during a survey."
%}

The current FishSense Lite prototype consists of a standard dive camera with a rigidly mounted, waterproof laser pointer. The laser provides a known geometric reference in each image, which can be used to estimate the distance between the camera and the fish and support downstream length calculations.

{% include 
    img_caption.html
    src="assets/fishsense/2023-07-17_sheephead_laser_dot.jpg"
    caption="Laser dot visible on a male California Sheephead."
%}

Automated length estimation relies on computer vision techniques to identify the laser point as well as the fish’s head and tail within each image. By assuming these points lie approximately on the same depth plane as the laser dot, image measurements and known camera geometry can be combined to estimate fish length.

FishSense Lite has been field tested in collaboration with REEF and has been featured in outreach efforts highlighting the role of **citizen science in marine conservation**, including coverage in *Alert Diver* magazine by DAN:  
[Advancing Conservation Through Citizen Science](https://dan.org/alert-diver/article/advancing-conservation-through-citizen-science/).

A short video demonstrating the system in use, courtesy of REEF, is available here:  
<iframe width="465" height="827" src="https://www.youtube.com/embed/wjY5di6nBZY" title="SMILE Project 2024   1080Square" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

FishSense Lite remains an active research and development project, with ongoing refinement informed by diver feedback and field deployments.

If you would like to learn more about FishSense Lite, please contact **Christopher Crutchfield** at  
[ccrutchf@ucsd.edu](mailto:ccrutchf@ucsd.edu).
