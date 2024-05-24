---
date: 2015-09-15 06:51:43+00:00
description: null
featuredImage: /assets/2015-09-15-birdnest-deployment.png
layout: blog-post
slug: /summer-2015-reu-bird-nest-tracker
title: 'Bird Nest Tracker: Summer 2015 REU'
author: Ihab Salameh
categories:
- bird-nest-tracker
tags:
- aerial-imaging
- camera
- conservation
- exploration
- imaging
- nsf
- research
- reu
- robotics
- summer
---
The scientific research and study of birds often requires ornithologists to spend days at a time observing their behavior. These efforts are made with the goal of obtaining population data critical to the preservation of nesting animals, and to improve our understanding of the many species of birds that inhabit an area. Engineers for Exploration is currently devising a solution that would allow scientists to use their time more efficiently and concentrate on research rather than data gathering.

The "Bird Nest Tracker" is a set of visual sensors capable of acquiring video data that can be used to localize nesting birds. The tracker can be coupled to a variety of aerial platforms, allowing us to gather data from large nesting sites without deploying a team of scientists to the field for long periods of time.

[![birdnest-payload]({{'/assets/2015-09-15-birdnest-payload.png' | resize: '375x278'}})]({{'/assets/2015-09-15-birdnest-payload.png' | absolute_url}})

The system is composed of two cameras used to record video data gathered by a SBC MinnowBoard running Ubuntu 14.04. One camera provides thermal imaging using Long-Wave Infrared (LWIR) at a resolution of 320x240 pixels, and the other is a regular visible light camera recording at a resolution of 4224x3156 pixels.


[![birdnest-images]({{'/assets/2015-09-15-birdnest-images.png' | resize: '573x231'}})]({{'/assets/2015-09-15-birdnest-images.png' | absolute_url}})

The two cameras have very different resolutions and fields of view, and their positions on the aerial platform will be offset slightly. This means that at the same instance in time, each camera will capture a similar but different recording of what is happening.Â  Sensor fusion and image processing can be used to skew, crop and rotate one of the videos so that we obtain the same image from both cameras, giving us useful data to analyze.

**Goals:**

Research has begun in the implementation of the image processing algorithms required to merge the videos and filter out everything that is considered signal noise in our case, which would be anything other than a bird's nest. The initial goal is to make these algorithms robust and accurate enough to provide a good representation of possible nesting sites. As a long-term goal, these techniques will be adapted to conduct on-board video processing, allowing for the detection of bird nests in mid-flight.

[![birdnest-aerial-test]({{'/assets/2015-09-15-birdnest-aerial-test.jpg' | resize: '426x409'}})]({{'/assets/2015-09-15-birdnest-aerial-test.jpg' | absolute_url}})
