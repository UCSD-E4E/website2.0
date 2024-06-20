---
date: 2015-09-29 00:41:46+00:00
description: null
featuredImage: /assets/2015-09-29-lidar-octocopter-2.jpg
layout: blog-post
slug: /summer-2015-reu-aerial-lidar
title: 'Aerial LiDAR: Summer 2015 REU'
author: Ihab Salameh
categories:
- aerial-lidar
tags:
- aerial-imaging
- archaeology
- conservation
- exploration
- imaging
- nsf
- research
- reu
- robotics
- structure-from-motion
- summer
---
LiDAR (Light Detection and Ranging) is a technology that generates a point cloud by using an array of lasers to measure distance. For archaeologists, a LiDAR scan can be extremely useful for surveying and mapping an unexplored area. Though LiDAR scanning services are available, hiring a pilot and renting the equipment necessary to generate one data set will generally cost a year's worth of funding for an archaeologist.

<figure>
<a href="{{'/assets/2015-09-29-lidar-system.png' | absolute_url}}"><img src="{{'/assets/2015-09-29-lidar-system.png' | resize: '300x188'}}" alt="LiDAR System"></a>
<figcaption>LiDAR System</figcaption>
</figure>

A more reasonable alternative is the Velodyne Puck LiDAR. At 300,000 points per second, a detailed point cloud can be generated without siphoning an archaeologist's funding. Traversing dense underbrush with a machete in the heat can take weeks and does not guarantee results. A LiDAR system attached to a drone can provide archaeologists with an easy way to collect millions of data points in a matter of hours, saving both time and resources. As an aerial platform, it can quickly and accurately survey large areas of land for the potential identification of ancient sites. The system pictured above was flown over the jungles of Guatemala in the hopes of detecting the Mayan temples buried within.

<figure>
<a href="{{'/assets/2015-09-29-lidar-poing-cloud.png' | absolute_url}}"><img src="{{'/assets/2015-09-29-lidar-point-cloud.png' | resize: '300x192'}}" alt="Point Cloud data of the campsite in Guatemala"></a>
<figcaption>Point Cloud data of the campsite in Guatemala</figcaption>
</figure>

The aim of this summer project was to successfully post-process the data collected from the Guatemala expedition and to reconfigure the hardware to include an external INS and GPS. Because the LiDAR was received only a few days before the trip, not all of the components were integrated completely. Correcting the scans first involves realignment. To achieve this, the GPS and IMU data were applied to the point cloud scans to create a transformed file. The transformed point clouds were then compared with consecutive scans using an iterative closest point algorithm. This process calibrates point cloud scans that are potentially skewed due to unforeseen errors, such as sudden wind causing the drone to bank. Once roughly realigned, the point clouds were combined to create a final point cloud scan of the area of interest. From this, the canopy can be subtracted and the ground can be analyzed for possible archaeological sites, in our case Mayan temples.

Further information on this project can be found at the E4E github wiki page [here](https://github.com/UCSD-E4E/aerial_lidar/wiki)
