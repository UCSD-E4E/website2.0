---
layout: project
permalink: /stereo-diving-rig
title: Stereo Diving Rig
category: stereo-diving-rig
enable_nav: false
---
![]({{ "/assets/nautical_archaeology/2014-06-26_stereo_rig.jpg" | resize: "640x230^,webp,80" }})

The stereo diving rig is a modular, diver-propelled data collection platform designed to make high-accuracy models of underwater environments using Structure from Motion and other 3D reconstruction algorithms. It can hold a variety of sensors and onboard computers, allowing for rapid collection of underwater data and facilitating investigations into the performance of different sensors in the underwater environment. The original configuration contained two IDS machine vision cameras in stereo, two Sony QX100 cameras with APS-C sensors in stereo, an inertial measurement unit (IMU), a digital compass, a pressure sensor, and a Doppler Velocity Logger (DVL). Combining measurements from all of these sensors allows the rig to gain more accurate pose estimates and generate more accurate 3D models.

The Stereo Rig has the capability to integrate many other sensors and computing platforms and facilitate experimentation into real-time mapping algorithms and underwater sensor performance. Current work on the rig involves integrating a GPU and/or and FPGA, stereo plenoptic cameras, and a hydrophone which can be combined with an Ultra-Short Baseline Acoustic Positioning System to geolocate underwater images. 

The data collected using this platform is used to investigate performance of Structure from Motion, SLAM, visual odometry, and other algorithms in the underwater environment.