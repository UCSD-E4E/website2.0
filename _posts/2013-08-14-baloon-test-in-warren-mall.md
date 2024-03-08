---
date: 2013-08-14 17:17:16+00:00
description: null
featuredImage: http://e4e.ucsd.edu/wp-content/uploads/rigging-1024x685.jpg
layout: blog-post
slug: /balloon-test-in-warren-mall
title: Balloon Test in Warren Mall
author: Eric Lo
categories:
- stabilized-aerial-camera-platform
post_format:
- post-format-gallery
---
(Photography by Jennifer Batryn and Lauren Nishizaki)

This summer, we've been hard at work redesigning the stabilized aerial camera platform. In our past tests towing the balloon from a boat to survey marine wildlife, the gimbal was not able to move quickly enough to counteract strong gusting motions, and the rigging prevented the balloon's sail from deploying completely. To improve the stability of the balloon platform, we switched to a new gimbal that is lighter and better balanced, which reduces the work that the servos need to do. This means that the servos will be able to provide faster response than the previous gimbal and stabilize more effectively, which is critical to getting good imagery when tethered to the back of a bobbing boat. In addition, we rewrote the stabilization code from the ground up to allow more tuning options and new features, such as autofocus control or the addition of other sensors. Finally, we redid the rigging so the gimbal would now be held at a skewed angle, which would prevent the sail from deploying. The sail is crucial for maintaining stability in windy conditions, as it prevents the balloon from spinning out of control. With all these new improvements, we sent up the balloon to see how it'd fare.

<figure>
<a href="{{'/assets/2013-08-14-rigging.jpg' | absolute_url}}"><img src="{{'/assets/2013-08-14-rigging.jpg' | resize: '670x448>'}}"></a>
<figcaption>
Contemplating balloon gimbal rigging
</figcaption>
</figure>

<figure>
<a href="{{'/assets/2013-08-14-gimbal.jpg' | absolute_url}}"><img src="{{'/assets/2013-08-14-gimbal.jpg' | resize: '670x448>'}}"></a>
<figcaption>
The gimbal
</figcaption>
</figure>

<figure>
<a href="{{'/assets/2013-08-14-eric-nathan-balloon.jpg' | absolute_url}}"><img src="{{'/assets/2013-08-14-eric-nathan-balloon.jpg' | resize: '670x448>'}}"></a>
<figcaption>
Preparing to send up the balloon (note the properly deployed sail!)
</figcaption>
</figure>

<figure>
<a href="{{'/assets/2013-08-14-balloon-away.jpg' | absolute_url}}"><img src="{{'/assets/2013-08-14-balloon-away.jpg' | resize: '670x448>'}}"></a>
<figcaption>
Up, up, and away!
</figcaption>
</figure>

The weather was great, the equipment worked, and we were able to get some fantastic imagery from the balloon. While controlling the gimbal and camera through the live video feed, we noted that the video was quite stable, though occasionally there were small disturbances. However, this corresponded with the more powerful wind gusts, which resulted in extreme gimbal motion, so in that light, the stabilization worked very well.

[![]({{'/assets/2013-08-14-warren_mall.jpg' | resize: '150x150'}})]({{'/assets/2013-08-14-warren_mall.jpg' | absolute_url}})
[![]({{'/assets/2013-08-14-price-center-1.jpg' | resize: '150x150'}})]({{'/assets/2013-08-14-price-center-1.jpg' | absolute_url}})
[![]({{'/assets/2013-08-14-geisel.jpg' | resize: '150x150'}})]({{'/assets/2013-08-14-geisel.jpg' | absolute_url}})

[![]({{'/assets/2013-08-14-house.jpg' | resize: '150x150'}})]({{'/assets/2013-08-14-house.jpg' | absolute_url}})
[![]({{'/assets/2013-08-14-house-side.jpg' | resize: '150x150'}})]({{'/assets/2013-08-14-house-side.jpg' | absolute_url}})
[![]({{'/assets/2013-08-14-price-center-courtyard.jpg' | resize: '150x150'}})]({{'/assets/2013-08-14-price-center-courtyard.jpg' | absolute_url}})

As we've done previously, we created a high resolution panoramic by stitching together individual photos. This provides a very wide field of view as well as lots of detail when zooming in, which is ideal for analyzing aerial surveys.

![]({{'/assets/2013-07-30-gigapan.png'}})

In addition to the DSLR mounted on the gimbal, we attached a GoPro Hero 3 Black to the T-frame to see how the stabilization was working, as well as test the new GoPro's performance as payload for the balloon. Due to the wide field of view, the angular disturbances from the wind gusting is less apparent, which is ideal for an unstabilized camera.

GoPro video

<iframe width="560" height="315" src="https://www.youtube.com/embed/UqeC0Drys10?si=HmHAEzaLaNFMxKjn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Finally, we've begun experimenting with 3D structure from motion reconstructions, which takes photos from different perspectives, and generates a 3D model of the scene. We hope to use this in the future to create photorealistic 3D models of the areas we're surveying, which would allow a researcher to "walk" through the area and see the relative position of terrain or interesting features without going out in the field again. Here's a sample from our pictures of the house on top of EBU1.

<iframe width="560" height="315" src="https://www.youtube.com/embed/gDJPp5WQOFw?si=ze0z_5lvEhBaQP6_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

With these successful tests on land, we're looking forward to our next deployment at sea, where we will verify stability while tethered to a boat, as well as hopefully getting imagery of marine life in shallow water.
