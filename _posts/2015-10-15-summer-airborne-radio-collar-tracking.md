---
date: 2015-10-15 19:00:12+00:00
description: null
featuredImage: /assets/2015-10-15-stesha-copter-mojave.jpg
layout: blog-post
slug: /summer-2015-airborne-radio-collar-tracknig
title: 'Airborne Radio Collar Tracking: Summer 2015 REU'
author: Nathan Hui
categories:
- radio-collar-tracker
tags:
- conservation
- dominican-republic
- radio-collar
- robotics
---
(Above) 2015 Radio Collar Tracker during Desert Testing, Mojave Desert. Photo Credit: Engineers for Exploration

Many wildlife ecology studies look at population size, location, and density to understand animal behavior and population movement. One common method for locating individuals of a population is radio collar tracking, or radio telemetry. The traditional method for radio collar tracking involves going out in the field and, using a large directional antenna, following the pulses transmitted by the radio collar. This technique often involves walking directly through the brush and over heavy terrain, resulting in researchers taking as many as 5 hours to travel 2 kilometers.

<figure>
<a href="{{'/assets/2015-10-15-c-ricordi.jpg' | absolute_url}}"><img src="{{'/assets/2015-10-15-c-ricordi.jpg' | resize: '1024x768'}}"></a>
<figcaption><em>Cyclura ricordi</em> (Ricord's ground iguana) hatchling with radio collar attached, Dominican Republic, September 2015. Photo Credit: Dr. John Iverson, Earlham College</figcaption>
</figure>

For the past couple years, Engineers for Exploration has collaborated with researchers from the San Diego Zoo. In particular, we have been working with Dr. Stesha Pasachnik, who studies iguana populations in the Caribbean. We are currently developing a platform to track radio collars placed on iguana hatchlings in the Dominican Republic. Recently, a team of engineers from E4E deployed this platform into the field, once in early July, and again in mid September. These first field trials of the Radio Collar Tracker platform provided a proof-of-concept field demonstration that proved the feasibility of autonomously locating radio collars using low-cost aerial platforms.

<figure>
<a href="{{'/assets/2015-10-15-dom-rep-takeoff.jpg' | absolute_url}}"><img src="{{'/assets/2015-10-15-dom-rep-takeoff.jpg' | resize: '1024x768'}}"></a>
<figcaption>Radio Collar Tracker platform in flight in the Dominican Republic, July 2015. Photo Credit: Engineers for Exploration</figcaption>
</figure>

During our July trip to the Dominican Republic, we tried validating the Radio Collar Tracker platform. During this trip, we encountered significant issues due to increased radio noise in the Dominican Republic. We then made some changes to the software and hardware configuration to increase sensitivity and to improve our ability to extract and identify the collar pulses. However, during our September trip, we found that while the changes we made had some effect on how effectively we could hear and localize the collars, the changes ultimately were not enough to work effectively.

<figure>
<a href="{{'/assets/2015-10-15-result.png' | absolute_url}}"><img src="{{'/assets/2015-10-15-result.png' | resize: '1024x768'}}"></a>
<figcaption>Radio Collar Tracker run showing collar. Each axis is in meters. September 2015.</figcaption>
</figure>

Ultimately, we were able to design and deploy a system that is capable of finding collars, however, because of the low power of collars placed on the iguana hatchlings and the noise environment in the Dominican Republic, we were not able to use the system as effectively as hoped.
