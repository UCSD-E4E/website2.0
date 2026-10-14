---
layout: project
permalink: /smartfin
title: Smartfin
category: smartfin
enable_nav: false
---
# Quick Summary
Smartfin brings surfers and scientists together to collect important oceanic data from coastlines by developing a surfboard fin that can passively collect information and seamlessly upload it to a cloud for use by scientists.

{% include 
    img_caption.html
    src="assets/smartfin/internals_fullres.jpg"
    src2="assets/smartfin/finScripps_fullres.jpg"
    caption='Images left to right from sciencemag.org and aquarium.ucsd.edu'
%}

<iframe width="800" height="475" src="https://www.youtube.com/embed/rY145HV-ReM" title="Smartfin: Surfing for Science" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

In the video above we show some of the progress made during the summer of 2020 and explain future goals.

# Introduction
As climate change becomes a growing crisis in our society, oceanography is a powerful tool to study its effects and their predicted impacts. Currently, satellites and off-shore buoys are used to study many parameters of the ocean including; sea surface temperature, salinity, ocean currents, and wave statistics. This data allows scientists to study ocean currents and nutrient flow which helps determine how ecosystems are coping with changes. However, these two methods are unable to collect this crucial data close to the shore in what’s known as the surf zone as the seafloor is too shallow and conditions are too rough to accommodate either system.

Searching for a solution to this problem, the Surfrider Foundation has partnered with the Scripps Institution of Oceanography to develop a solution called Smartfin that would allow surfers to passively collect this crucial data while they are in the water. The Smartfin hardware has been developed with many sensors designed to measure temperature, location, and wave characteristics, with more currently in development to study pH, dissolved oxygen, and chlorophyll. Preliminary testing of the Smartfin has shown its potential, as shown below temperature data from the board was compared to standard data collected from a near offshore buoy run by Scripps. As many beaches do not have this capability, providing this tool to surfers in select locations will give ordinary citizens the power to make powerful scientific observations, all while catching waves.


![]({{"assets/smartfin/waveData_fullres.jpg" | absolute_url}})

In the chart above, Smartfin user data is recorded in black on top verified temperature measurements from Scripps Pier in blue. The data points line up nicely, showing the impressive accuracy and reliability of the Smartfin to record this ocean parameter.
Image courtesy of Dr. Tyler Cyronak, Scripps Institute of Oceanography
Seen below is an early model of the Smartfin attached to a surfboard. This clear fin shows the battery, GPS, temperature sensor, and IMU (inertial measurement unit). The fin is still going through an iterative design process as more hardware is added to increase its capabilities. As seen on the photo to its right.

{% include 
    img_caption.html
    src="assets/smartfin/seeThrough_fullres.jpg"
    src2="assets/smartfin/handFin_fullres.jpg"
    caption="Images from surfrider.org"
%}


# Technical
Smartfin in its current state is very accurate at measuring sea surface temperature (SST) through its on board temperature sensor, as measured against a control of the Scripps Buoy. Recently, it has also shown that it can calculate certain wave statistics such as wave height very accurately as well.

The Smartfin calculates wave height through a Kalman Filter and spectral analysis. Spectral analysis will determine wave height from acceleration data, and a Kalman Filter will reduce noise generated while collecting data about the position of the fin.

There are a number of challenges to overcome before all of the wave statistics can be measured, as real ocean waves provide the sensors with very noisy data that can be difficult to interpret. In addition to this, the control buoy is far enough off-shore that there can be a discrepancy between its measured values and the Smartfins, making it difficult to determine if the Smartfin’s calculated values align with the buoy’s. An ongoing project to solve this issue is creating a filter that can remove data that is too far away from the expected results. These data points come up sometimes due to overly noisy data, or when there is too big of a discrepancy between the control values and the actual wave statistics for that day. Another possible way of solving this would be to build a program that can compare the results of individual Smartfin users within the same area against one another, therefore eliminating the need for an off-shore control buoy.

# Prospective Students
Currently, this project is focused on developing the next generation hardware, firmware, and supporting infrastructure.  In particular, we are looking for students with any of the following skills:
- Embedded C/C++ (particularly with Particle or STM32)
- PCB Design (particularly with Altium)
- Mechanical Design/Fabrication (particularly with SolidWorks and composites)

Specific positions can be found here: [Open Positions]({{ "open-opportunities" | absolute_url }}).

More Info:
<!-- [https://smartfin.org/](https://smartfin.org/) -->

<!-- [https://www.surfrider.org/programs/smartfin](https://www.surfrider.org/programs/smartfin) -->
[https://www.surfrider.org/media/press-releases/surfers-become-citizen-scientists-as-surfboard-fin-collects-critical-ocean](https://www.surfrider.org/media/press-releases/surfers-become-citizen-scientists-as-surfboard-fin-collects-critical-ocean) 


[https://youtu.be/CU-IX8tqP_4](https://youtu.be/CU-IX8tqP_4)
