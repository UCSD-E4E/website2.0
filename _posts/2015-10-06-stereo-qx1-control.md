---
date: 2015-10-06 18:31:54+00:00
description: null
featuredImage: /assets/2015-10-06-screenshot.png
layout: blog-post
slug: /stereo-qx1-control
title: Stereo QX1 Control
author: Eric Lo
categories:
- news-and-updates
---
In the past, we've interfaced with the Sony QX series of cameras with [custom software]({{'/quadcopter/sony-qx100-quadcopter-testing' | absolute_url}}) and [hardware]({{'/news-and-updates/sony-qx1-triggering' | absolute_url}}), but we were unable to control 2 cameras at once, as the QX camera hosts its own Wi-Fi access point. When we came across a reference to "Multi Camera Control", we had to take a look.

As it turns out, there is very little documentation on this. The suggested option from the PlayMemories Mobile application is to enter in the SSID and passkey on the camera, but the QX1 has no screen, nor any entry method. Digging a bit deeper, we found that Sony's Live View Remote claims to pair using WPS. Naturally, we grabbed a WPS pushbutton enabled router, and tried it out. Turns out it works! Here's what we did to pair 2 QX1s to 1 router:

<figure>
<a href="{{'/assets/2015-10-06-qx1-button.png' | absolute_url}}"><img src="{{'/assets/2015-10-06-qx1-button.png' | resize: '300x278'}}" alt="The Wi-Fi Button"></a>
<figcaption>The Wi-Fi Button</figcaption>
</figure><figure>
<a href="{{'/assets/2015-10-06-qx1-multi.png' | absolute_url}}"><img src="{{'/assets/2015-10-06-qx1-multi.png' | resize: '300x278'}}" alt="The Multi Camera Indicator"></a>
<figcaption>The Multi Camera Indicator</figcaption>
</figure>

1. Put the QX1s into multi camera mode. To do this, tap the Wi-Fi button under the battery cover until the LCD has a block next to the multi camera mode indicator.
2. Put the router into WPS pushbutton pairing mode.
3. To pair each camera, push and hold the Wi-Fi button until the camera beeps, or until you see an indication on the router that a device has connected. Repeat for each camera.
4. You should now have your cameras connected to the Wi-Fi router.

If you do this with your phone (we got it working on a Sony Xperia Z3 Compact), you can use the PlayMemories Mobile app to preview and control each camera, and ask them to take a picture "simultaneously". In practice, you're much better off triggering through the USB port if you want synchronization, but it's a nice feature to have if your cameras are far apart.

If you do this with a Wi-Fi router, you can look up the assigned IP addresses for each camera, and have your software to talk to that IP directly. Everything else works the same as with one camera.

Happy multi QX1 controlling!
