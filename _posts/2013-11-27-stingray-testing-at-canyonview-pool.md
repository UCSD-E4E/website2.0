---
date: 2013-11-27 00:22:33+00:00
description: null
featuredImage: /assets/2013-11-27-stingray-underwater.jpg
layout: blog-post
slug: /stingray-testing-at-canyonview-pool
title: Stingray Testing at Canyonview Pool
author: Antonella Wilby
categories:
- underwater-projects
post_format:
- post-format-gallery
---
Stingray Team has been hard at work testing and refining the controls system of our underwater vehicle. We've been working on getting the Stingray to auto-stabilize at a given depth and swim in a dead-reckoned lawnmower pattern. Current testing has been done in UCSD's Canyonview pool, but we are close to moving the Stingray to the ocean to test in a realistic environment.

The video below shows the Stingray descending to a user-specified depth while auto-stabilizing.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Q9eLGGNRPgs?si=-Eo0rC35_y9a49lU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In addition to developing visual pose estimation and SLAM software, the vision team has been working on getting the Stingray to track and follow a colored target in order to further test the control system. This target-tracking system will allow us to refine the controls and navigation system as an intermediate step to complete autonomous navigation. The video below shows the Stingray tracking a green target.

<iframe width="560" height="315" src="https://www.youtube.com/embed/kmZBftBRP1w?si=wyxZYjVFHdT6RFuN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In the video above, color segmentation is performed to extract the green target from the background. The threshold window shows in white the objects in the image that meet the threshold, and the desired target is outlined in white in the RGB image window. The Stingray tracks the target by continuously staying the same distance from the target.

**Pictures from Stingray Test**

[![]({{'/assets/2013-11-27-stingray-underwater.jpg' | resize: '150x150'}})]({{'/assets/2013-11-27-stingray-underwater.jpg' | absolute_url}})
[![]({{'/assets/2013-11-27-IMG_0002.jpg' | resize: '150x150'}})]({{'/assets/2013-11-27-IMG_0002.jpg' | absolute_url}})
[![]({{'/assets/2013-11-27-IMG_0006.jpg' | resize: '150x150'}})]({{'/assets/2013-11-27-IMG_0006.jpg' | absolute_url}})

[![]({{'/assets/2013-11-27-IMG_0014.jpg' | resize: '150x150'}})]({{'/assets/2013-11-27-IMG_0014.jpg' | absolute_url}})
[![]({{'/assets/2013-11-27-IMG_3981.jpg' | resize: '150x150'}})]({{'/assets/2013-11-27-IMG_3981.jpg' | absolute_url}})
[![]({{'/assets/2013-11-27-underwater.png' | resize: '150x150'}})]({{'/assets/2013-11-27-underwater.png' | absolute_url}})
