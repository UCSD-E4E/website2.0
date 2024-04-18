---
date: 2015-03-15 00:16:23+00:00
description: null
featuredImage: /assets/2015-03-15-uw-tablet.jpg
layout: blog-post
slug: /underwater-tablet-interface-for-stereo-diving-rig
title: Underwater Tablet Interface for Stereo Diving Rig
author: Antonella Wilby
categories:
- underwater-projects
---
For the last quarter we've been working on developing a tablet-based diver interface for our Stereo Diving Rig. The goal of this interface is to allow a diver to see images and sensor data streaming from the rig in real-time, as well as allow them to control the parameters and settings of the onboard cameras to adapt to changes in underwater lighting conditions. 

Most tablets use a capacitive touch-screen interface, which doesn't work underwater because water is conductive and thus changes the capacitance over the entire screen, essentially causing the tablet to register a "touch" at every point on the screen. Instead, we are using a tablet that uses a stylus to interface with the screen. The screen of the tablet contains a grid of coils that generate an electromagnetic field in front of the tablet, and the stylus pen contains a coil that transfers the power from the screen to the internal electronics of the stylus. When the stylus pen gets close enough to the tablet's electromagnetic field, the stylus receives power and the tablet registers a touch on the touchscreen. 

Water attenuates electromagnetic waves outside of the range of visible light very quickly. We tested the tablet (in a waterproof bag) and the stylus underwater to see if the electromagnetic field from the screen was able to transmit far enough underwater to register a touch from the stylus. Our test was successful, indicating that a pen-based interface is a viable alternative to using a capacitive touchscreen to control our camera rig.  

<figure>
<a href="{{'/assets/2015-03-15-stylus-enclosure-11.jpg' | absolute_url}}"><img src="{{'/assets/2015-03-15-stylus-enclosure-11.jpg' | resize: '1024x768'}}"></a>
<figcaption>Design of waterproof stylus enclosure in CAD software</figcaption>
</figure>

We are currently designing an underwater enclosure for the stylus (pictured above), which a diver can use to interface with the stereo diving rig via the tablet. In the coming months, we will also design a more robust underwater tablet enclosure than the waterproof bag we are currently using, to allow the tablet interface to be used at depths down to 120 ft. 
