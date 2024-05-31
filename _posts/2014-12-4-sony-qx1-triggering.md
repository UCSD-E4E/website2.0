---
date: 2014-12-04 03:46:49+00:00
description: null
featuredImage: /assets/2014-12-04-iris.jpg
layout: blog-post
slug: /sony-qx1-triggering
title: Sony QX1 Triggering
author: Eric Lo
categories:
- news-and-updates
---
We've grown quite fond of Sony's QX100 on our platforms for its superb image quality in a small form factor.  However, it has been difficult to remotely control the camera, and we're still using a [servo pushing a button to take pictures]({{'/quadcopter/sony-qx100-quadcopter-testing' | absolute_url}}).

<figure>
<a href="{{'/assets/2014-12-04-sony-qx.jpg' | absolute_url}}"><img src="{{'/assets/2014-12-04-sony-qx.jpg' | resize: '1024x768'}}" alt="QX1 (left), QX100 (right)"></a>
<figcaption>QX1 (left), QX100 (right)</figcaption>
</figure>

We recently acquired the Sony's newest lens cameras: the QX1. The larger APS-C sensor and interchangeable lens provide for higher image quality, though at the expense of increased weight. We've paired the QX1 with Sony's 20mm f/2.8 lens for a total weight of 269g, up from 180g with the QX100.

<figure>
<a href="{{'/assets/2014-12-04-qx1-trigger.jpg' | absolute_url}}"><img src="{{'/assets/2014-12-04-qx1-trigger.jpg' | resize: '1024x768'}}" alt="QX1 with trigger cable and battery dummy"></a>
<figcaption>QX1 with trigger cable and battery dummy</figcaption>
</figure>

Other than image quality improvements, we've found 2 features that make the QX1 attractive for installation in our platforms: a readily available battery dummy, and a nice wired trigger.

The AC-PW20 provides an easy way to externally power the QX1, and we've hooked it up to a DC/DC voltage regulator set at 8V to avoid the problem of the camera battery running out.

The QX1 supports the RM-VPR1 remote, which uses a proprietary plug to enable not only focus and shutter release, but also turning the camera on and off remotely. The wired shutter release is nice to have for our aerial platforms, but the ability to turn the camera on and off remotely is ideal for our underwater platforms which need to be sealed before submersion. However, we didn't want to take up space and weight with the remote, so we disassembled the remote and cut up the cable to get it hooked directly to our microcontrollers. As it turns out, the connector on both sides of the cable is the same, so after cutting off the plastic bits shrouding the connector, we get 2 connectors from the 1 cable.

<figure>
<a href="{{'/assets/2014-12-04-trigger-cable.jpg' | absolute_url}}"><img src="{{'/assets/2014-12-04-trigger-cable.jpg' | resize: '1024x768'}}" alt="The innards of Sony's Multi-Terminal cable"></a>
<figcaption>The innards of Sony's Multi-Terminal cable</figcaption>
</figure>

The cable from the remote to the camera has 7 wires and a shield. Here's the pinout:

| Color | Signal |
|-------|--------|
| Shield | GND |
| Black | GND |
| Blue | ON/OFF |
| Yellow | Focus |
| Green | Shutter Release |
| Red | ? |
| Orange| ? |
| Brown | ? |

By shorting ON/OFF to ground, we can turn the camera on or off, and both focus and shutter release work the same as other camera remotes. Hooking these up to optoisolators, we can easily control the camera as if we were pushing the physical buttons and achieve good performance. The rest of the camera controls can be handled over Wi-Fi with the Sony Camera API, but more on that later.
