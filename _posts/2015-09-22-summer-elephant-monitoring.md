---
date: 2015-09-22 01:16:59+00:00
description: null
featuredImage: /assets/2015-09-22-elephant.png
layout: blog-post
slug: /summer-2015-reu-elephant-monitoring
title: 'Elephant Monitoring: Summer 2015 REU'
author: Ihab Salameh
categories:
- elephant-monitoring
tags:
- conservation
- exploration
- research
- reu
- robotics
- summer
---
Though there is already a range of commercially available deployable autonomous recording units, many are expensive, or consume too much power to be deployed for desirable periods of time. Their cost and need for heavy battery units make deploying them in remote locations difficult. We're working with the San Diego Zoo Institute for Conservation Research to develop a more cost-effective unit that can be sent on similarly long deployments.

<figure>
<a href="{{'/assets/2015-09-22-elephant-mic.png' | absolute_url}}"><img src="{{'/assets/2015-09-22-elephant-mic.png' | resize: '300x113'}}" allt="A similar unit developed by the Cornell Lab of Ornithology"></a>
<figcaption>A similar unit developed by the Cornell Lab of Ornithology</figcaption>
</figure>

The system, known as an autonomous recording unit, must be able to endure hostile environments, while capturing audio frequencies from 5 Hz to several thousand Hz, for periods of 6 months or longer at a time. These devices are often placed in remote locations, requiring several days of trekking through dense jungle to reach, so minimizing weight is very important. As a result, the system must be extremely low power to minimize the batteries required.

As the system will be unattended for months at a time, it must also be capable of storing large amounts of data. Due to the low frequencies measured, relatively low sample rates can be used, allowing for somewhat smaller disk storage.

<figure>
<a href="{{'/assets/2015-09-22-elephant-circuitry.png' | absolute_url}}"><img src="{{'/assets/2015-09-22-elephant-circuitry.png' | resize: '300x225'}}" alt="elephant-circuitry"></a>
</figure>

After early testing with different types of microphones, the electret condenser microphone was selected for its low cost, wide availability, and flat frequency response. Some electrets have flat responses down to just a few Hz, making them ideal for our purposes.

The MSP432 microcontroller was selected for its decent processing power, RAM space and low power consumption. It comes with a built in ADC and is works with multiple communication protocols such as SPI, making it compatible with SD cards.

Our team will work over the next few weeks on solving few issues related to power supply of the system, complete the code port to the MSP432 from a different controller, and begin testing the units isolated from outside connections (PC data, external power supply, etc.)
