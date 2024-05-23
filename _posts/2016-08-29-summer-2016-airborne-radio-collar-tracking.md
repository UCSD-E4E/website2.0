---
date: 2016-08-29 15:00:09+00:00
description: null
featuredImage: /assets/DSCN0687.jpg
layout: blog-post
slug: /summer-2016-airborne-radio-collar-tracking
title: 'Airborne Radio Collar Tracking: 2016 REU'
categories:
- autonomous-copters
- radio-collar-tracker
tags:
- conservation
- exploration
- iguanas
- nsf
- radio-collar
- research
- reu
- summer
---

The Radio Collar Tracker project is a collaboration between the San Diego Zoo€™s Beckman Institute for Conservation Research (ICR) and UC San Diego€™s Engineers For Exploration. We have been working with the ICR and its collaborators for the past four years to develop a drone to conduct radio collar tracking missions. Ultimately, the goal of this project is to develop a drone capable of autonomously tracking radio collared animals, particularly through environments that are difficult to access. To accomplish this, our system flies a search grid over a candidate area while recording a large swath of radio spectrum using a software defined radio. Once the drone returns from the flight, we use digital signal processing to extract the frequencies that the radio collars are transmitting on, and use a statistical model to determine where the collars we heard are. This data is then saved to a GIS (Geographical Information System) file, which ecologists and biologists can then use in their research.

For the past couple of years, the Radio Collar Tracker has been further developed. In the summer of 2015, a proof of concept was built and deployed in the Dominican Republic. While there were problems, it demonstrated the potential for the system to be effective. Since then, some of the post-processing and workflow have been improved to make the system more effective and help the researchers better visualize where the radio collar is located. In the spring of this year, the system was deployed in the Cayman Islands, but some of the same problems persisted. One key problem of the system is the detection range. Currently the system has a detection range of about 30 meters. While this is okay, to make the system really effective the range has to be improved. For the summer the goal was to improve the range from a hardware perspective.

[caption id="attachment_4164" align="aligncenter" width="640"]![Cayman Islands Flight Results](/assets/2016-08-29-summer-2016-airborne-radio-collar-tracking_LCI-1024x583.png) An example of improved data visualization from the Cayman Islands[/caption]

While there were considerations for the proof-of-concept system, it was decided that every aspect of the current system should be reevaluated as well as determining if new hardware should be introduced. Not only was the goal to improve the range, but also to keep the cost and weight down.

The new design consisted of the same components: antenna and a software defined radio. Computer simulation was used to design the antenna to make sure it is tuned to the frequency of the radio collars. Several SDRs were evaluated, weighing cost, sensitivity and ease of use. In addition to the antenna and SDR, we added an amplifier inline to make the signal stronger as it enters the receiver. As well as the receiver itself, we were able to determine that other radio systems on the UAS (unmanned aerial systems) and the motor controllers were causing some interference with the radio collar radio, which can decrease the effectiveness of the system.

[caption id="attachment_4165" align="aligncenter" width="640"]![New Radio Collar Tracker RF Equipment](/assets/2016-08-29-summer-2016-airborne-radio-collar-tracking_IMG_0786-1024x768.jpg) An example of the receiver with the SDR, amplifier, and antenna[/caption]

Although we didn€™t test the system on a field deployment like last summer, we still tried to not always test in the lab. Unfortunately due increasing restriction on flying UAS (Unmanned Aerial Systems) for research we were unable to test the system locally. To get the best idea of the improvement we tested our system on the ground. Although this test would not give us an absolute gauge of improvement, it can show it in a relative manner. From the initial results we have been able to demonstrate that we have almost doubled the detection range compared to the system that was on previous deployments.

Ultimately this summer we have designed the receiver to become more sensitive and we are excited to see the results on the next field deployment.

__€”_ by Daniel Webber and Nathan Hui_
