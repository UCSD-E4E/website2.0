---
date: 2013-07-23 04:47:53+00:00
description: null
featuredImage: /assets/2013-07-23-tiger-danger.jpg
layout: blog-post
slug: /the-tiger-tracker-begins
title: The Tiger Tracker Begins
author: Riley Yeakle, Eric Lo, David Muller
categories:
- intelligent-camera-trap
---
(Photography by [Jennifer Batryn](https://www.flickr.com/photos/kokosnu55/))

A while back, a few researchers had set up a camera rig in the lion enclosure at the zoo, Dr. Lance Miller had told us. He had cautioned them the cameras were too close to the ground, and like most cats, lions tend to be very curious about new things in their environments. It turns out, Lance was right. The next morning all but a few scraps of the cameras were left. As we set up our own camera system in the tiger's enclosure, we hoped our system would not befall the same fate.

The July 3rd deployment was the first step in realizing the [Tiger Tracker]({{'intelligent-camera-trap' | absolute_url}}) behavior monitoring system.

[![tiger2]({{'/assets/2013-07-23-tiger2.jpg' | resize: '600x402>'}})]({{'/assets/2013-07-23-tiger2.jpg' | absolute_url}})

The goal of our first test run at the zoo was to gather training footage of the tiger to 'teach' the main processor of the system how to tell the difference between the tiger and other warm objects. As humans with an incredibly well developed visual system, we can easily distinguish animals from non-animals. Computers however, require lots of training footage and clever algorithms to do the same. For the basic tiger detector, the computer needs hundreds, if not thousands of annotated images to reliably recognize it.

[![riley]({{'/assets/2013-07-23-riley-setup.jpg' | resize: '600x402>'}})]({{'/assets/2013-07-23-riley-setup.jpg' | absolute_url}})

To capture the data needed to build these tiger-finding algorithms, we constructed a fixed camera turret with a webcam, high resolution thermal camera, and an experimental ultra low resolution infrared sensor. With the webcam we would capture human-friendly footage, while the thermal camera and low resolution heat sensor would capture computer-friendly footage. By cross-referencing the thermal and color videos, we will be able to extract the training data needed to construct and test the effectiveness of our tiger detection algorithms.

![gabrielle-riley-setup]({{'/assets/2013-07-23-gabrielle-riley-setup.jpg' | resize: '175x261>'}}) ![david-catwalk]({{'/assets/2013-07-23-david-catwalk.jpg' | resize: '175x261>'}}) ![]({{'/assets/2013-07-23-setup.jpg' | resize: '175x261>'}})

With help from Greg Vicino and San Diego Zoo staff, we set up the camera rig in the tiger enclosure. The cameras aimed towards an area near the back of the enclosure, one of the tiger's favorite places to hang out. We mounted the turret up high on the fence near the back of the enclosure. Though getting good footage of the tiger was important, we also wanted the camera rig to come back out in one piece the next day.

![final-check]({{'/assets/2013-07-23-final-check.jpg' | resize: '600x402>'}})

The camera rig now in place, we did one last check and launched the video capture program. After a quick head count, we took off and the keeper let the tiger into its enclosure. The tiger walked right into the field of view of the camera.

![exit]({{'/assets/2013-07-23-exit.jpg' | resize: '600x402>'}})

The next day we retrieved the camera rig after letting it capture data for almost 24 hours. Each of the cameras on the turret captured some great shots of the tiger.

<figure>
    <img alt="tiger-thermal-highres" src="{{'/assets/2013-07-23-tiger-thermal-highres.jpg' | resize: '600x402>'}}">
    <figcaption>A side by side comparison of thermal (left) and visible (right) spectrum imaging</figcaption>
</figure>

The low resolution IR sensor was largely experimental because we weren't sure that the sensor would be able to resolve the tiger, but it turns out in some cases we could. We're currently testing the effectiveness of different segmentation algorithms using both the high and ultra low resolution thermal footage we captured.

<figure>
    <img alt="tiger-lowres-web" src="{{'/assets/2013-07-23-tiger-lowres-web.png' | resize: '600x402>'}}">
    <figcaption>Experimental ultra-low resolution thermal imaging (right) may provide a viable tiger detection method</figcaption>
</figure>

Once we use this data to demonstrate our ability to localize the tiger, we'll move on to the next test: recording and classifying tiger behavior as active or inactive. This simple characterization in itself will streamline behavioral data collection and analysis for researchers at the zoo. With the feedback this system provides, caretakers and researchers will be able to improve the quality of care and better study species in captivity.

[More and Full-Size Images](https://www.flickr.com/photos/kokosnu55/sets/72157634476869034/with/9204190781/)
