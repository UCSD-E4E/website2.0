---
date: 2014-02-06 08:02:34+00:00
description: null
featuredImage: /assets/2014-02-06-stingray.jpg
layout: blog-post
slug: /stingray-joystick-control
title: Stingray Joystick Control
author: Justin Chen
categories:
- underwater-projects
tags:
- auv
- imaging
- robotics
- stingray-2
- underwater
- underwater-robot
---
Themost recent developments for the Stingray include having a way to control the vehicle remotely using a Playstation 3 controller. Although the goal for the Stingray is to have complete autonomy, we wanted a way to be able to control the robot in situations where remote control is necessary (ie. difficult obstacles, retrieving the robot). We focused on using a Playstation 3 controller because it would be intuitive and easy to use for the operator.

<iframe width="560" height="315" src="https://www.youtube.com/embed/v8D40E6Ah8M?si=3jNDmzbfJau5mF4r" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This past month, we had the chance to test the joystick function at the pool. Although we didn't have problems with connecting the controller to the robot, we were having issues with the motors responding the commands being sent from the controller. We noticed that when the Stingray was in the water, there would be moments where the motor continued to run, although the input from the controller has ceased. This is seen throughout the video above. Though we aren't 100% sure what is causing the problem, we have simplified the code to be able to move in multiple degrees of freedom at once. This will allow the user to be able to perform movements such as forward-left simultaneously.
