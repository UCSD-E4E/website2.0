---
date: 2015-10-06 01:30:01+00:00
description: null
featuredImage: /assets/2015-10-06-tigers-posing.jpg
layout: blog-post
slug: /summer-2015-reu-intelligent-camera-trap
title: 'Intelligent Camera Trap: Summer 2015 REU'
author: Ihab Salameh
categories:
- intelligent-camera-trap
tags:
- camera
- camera-trap
- computer-vision
- conservation
- exploration
- imaging
- nsf
- research
- reu
- robotics
- summer
- trap
- turret
---
A camera trap is a recording device that captures images or video of wildlife. Current camera trap technology is used by biologists and researchers to obtain population data about animals in a region of interest. However the scope of such data collection is limited by the fact that existing camera traps have a static field of view and often receive false positive triggers. This means that researchers often end up with hours of video containing no animals, or videos in which only part of the animal is visible. To solve these issues and to make camera traps more useful to behavioral researchers, our team is developing an intelligent camera trap that combines multiple high resolution cameras and computer vision tracking algorithms so that it can cleverly follow the movement of interesting animals.

Since camera traps are deployed for several months at a time, they must be able to conserve power. As a result, the intelligent trap must be based on an optimized tracking algorithm that can run on a small, efficient embedded board. This is an interesting problem because highly sophisticated tracking algorithms consume much more power, but are also more likely to minimize false positives; thus conserving power that would otherwise be used to record pointless data. The algorithm that our team developed this summer makes clever use of background subtraction and Kalman filters to effectively ignore background noise like moving branches and to track only the movement of relevant animals.

<figure>
<a href="{{'/assets/2015-10-06-cameratrap-tracking.png' | absolute_url}}"><img src="{{'/assets/2015-10-06-cameratrap-tracking.png' | resize: '300x278'}}" alt="Tracking objects as they move through a dynamic environment"></a>
<figcaption>Tracking objects as they move through a dynamic environment</figcaption>
</figure>

This summer REU team chose to explore the feasibility of a virtual turret design for the intelligent camera trap. The design incorporates up to eight high-resolution webcams that capture a 360 degree field of view. Our research involved choosing appropriate hardware and determining theoretical and empirical limits of a system that has to handle several live video feeds at once. This largely consisted of bandwidth and power testing.

<figure>
<a href="{{'/assets/2015-10-06-cameratrap-prototype.png' | absolute_url}}"><img src="{{'/assets/2015-10-06-cameratrap-prototype.png' | resize: '300x278'}}" alt="A CAD rendering of a potential mounting design"></a>
<figcaption>A CAD rendering of a potential mounting design</figcaption>
</figure>

It was demonstrated that a virtual turret is a viable design for the intelligent camera trap by building a prototype with USB webcams and working software for tracking and switching cameras. However, this design has yet to be field-tested. Ongoing and future work for this project includes finalizing the containment hardware, designing a process for video stitching during post-processing, and determining ways to draw high resolution videos at high frame rates from more than two cameras simultaneously.

We would like to extend our thanks to the wildlife videographer Nathan Williamson, and the researchers from the NOAA Southwest Fisheries Science Center, Jefferson Hinke and Mike Goebel, who met with us to provide advice and insight about improving upon existing camera trap designs. Additionally we would like to thank Matt Anderson and the San Diego Zoo for their support of this project.
