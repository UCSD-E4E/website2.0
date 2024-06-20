---
date: 2023-06-20 20:19:40+00:00
featuredImage: assets/fishsense/2023-06-20-segmented-garibaldi-with-laser.png
layout: blog-post
slug: /introducing-next-generation-of-fishsense
title: Introducing Next Generation of FishSense
author: Christopher Crutchfield
categories:
- news-and-updates
---
We'd like to introduce the next generation of our FishSense System. FishSense is a camera platform that aims to estimate the mass of fish visible in an image, using a combination of species identification and automatic length measurement. Now, to meet these goals, we present our FishSense-Lite and FishSense-Pro systems.

Our previous system leveraged an Intel RealSense D455 stereo camera to measure the length of fish, but the lack resolution in both the RGB and depth streams of this camera brought progress to a halt. Though our two new systems are still in active development, we are proud of the headway that has been made and would like to recognize the work being done.

## FishSense-Lite
FishSense-Lite is our citizen science platform to be used by untrained, citizen divers. This platform aims to provide an inexpensive, easy-to-build camera system that can be built by anyone in the world. We aim to use only components that are available off-the-shelf or 3D printable with ready-made CADs. We would like to thank Nathan Hui, Kyle Hu, and Christopher Crutchfield for their work designing this prototype and deriving the math that allows it to function.

In our prototype, the lens, enclosure, and camera are all commercially available components that many divers may already have. The laser is also commercially available and commonly used in dive training. Finally, the laser mount is a 3D printable component for which we intend to publish the CAD.

We intend to do all processing on an off-camera device to facilitate these design goals. This allows us to use an Olympus TG6 as our camera platform. We will leverage parallax between the camera and a laser rigidly affixed to it. Doing so allows us to estimate the depth of the object that the laser hits. With this information, we can calculate an approximation of the length of that object, which, in this case, is a fish.

{% include img_caption.html
    src="assets/fishsense/fishsense-lite-system.png"
    caption="Prototype of the FishSense-Lite system.  Based on a consumer camera, laser, and 3D printed components." %}

### Calibration
To perform the parallax calculations, it is necessary to know the camera’s intrinsic parameters. We then need to calculate the baseline between the laser and the camera as well as the angle of the laser with respect to the camera axis.

To perform calibration, we take multiple pictures of a known checkerboard pattern. These images then allow us to calculate the position of the checkerboard in three-dimensional space. We can then reproject them from the laser’s two-dimensional image to real-world three-dimensional coordinates using math and software provided by Kyle Hu and Christopher Crutchfield.

The calibration calculations happen off-device, and currently take tens of minutes per camera. We intend to leverage CUDA to improve the calculation performance, as the algorithm is parallelizable.

{% include img_caption.html
    src="assets/fishsense/2023-06-20-example-calibration-photo.png"
    caption="An example calibration photo used for our laser calibration." %}

Using multiple calibration images, as seen above, we can determine the location of the laser.  Then, because the checkerboard pattern is known ahead of time, it can be used to calculate the laser’s position using the observed parallax.

### Laser Detection
Thank you to Viva Suresh for his work designing the laser detection system.  Here, we have two main heuristics that can detect the laser within an image: 
 * The laser should be the brightest location in the image
 * The laser location is constrained based on the baseline and laser axis. Using these two heuristics, we are developing techniques to detect the lasers within images taken by our camera.

{% include img_caption.html
    src="assets/fishsense/2023-06-20-laser-detection.png"
    caption="Image representing a laser detected leveraging the first of the two heuristics listed above." %}

The above image represents a laser detected leveraging the first of the two heuristics listed above. As we continue to develop this portion of the project, we intend to leverage the second heuristic to generate a probabilistic map over all pixels in an image to determine which are most likely to be the laser.

### Fish Detection
Kyle Tran and Viva Suresh worked together to leverage the [Fishial](https://github.com/fishial) project ([https://github.com/fishial](https://github.com/fishial)) for Fish detection and segmentation. This project aims to be able to provide fish segmentation in images as well as species detection. To have better results on fish which we expect to see in our research, we intend to perform additional tuning to the species identification models provided. We intend to use our NVIDIA RTX A6000 GPU to enhance our training performance.

{% include img_caption.html
    src="assets/fishsense/2023-06-20-fishial-contour.jpg"
    caption="Fish whose contours were detected by the tools provided by the Fishial project." %}

### Length Detection
Once we have the contours detected by Fishial, we can perform a principal component analysis to determine the axis with the most variance. On most fish, and the on all the fish we are interested in, this axis closely lines up with the axis we wish to measure the length of.

{% include img_caption.html
    src="assets/fishsense/2023-06-20-fish-length.png"
    caption="This fish’s contours were determined using Fishial, which was used to calculate the axis of the largest variance. This axis strongly correlates with how we wish to measure the fish." %}

### Future Work
At the moment, much of this pipeline requires manual effort. To reduce this and allow us to scale, we intend to automate many steps, outputting a fish's mass directly from an image of it with a laser point. 

{% include img_caption.html
    src="assets/fishsense/2023-06-20-fishsense-pipeline.png"
    caption="Proposed pipeline" %}

Almost all these steps currently in the proposed pipeline require human assistance at some point in their performance. We are confident that we can implement many of these technologies into a coherent package such that it is usable on consumer-grade hardware. Many of these will benefit significantly from CUDA acceleration and are parallelizable or ML-based tasks.

## FishSense-Pro
In addition to our citizen science platform, we are building a higher-fidelity science platform. The aptly named FishSense-Pro system targets trained scientific divers, as opposed to the laser-based citizen science platform, allowing us to build a more accurate platform. 

Stereo cameras can measure depth at every point in an image, not just where the laser hits an object. Thus, we have evaluated many camera pairs to see which will best fit our system.

{% include img_caption.html
    src="assets/fishsense/2023-06-20-depth-resolving-power.png"
    caption="The image above compares the measured length resolution via mathematical modeling of multiple different cameras we evaluated. Below we will only discuss the cameras we are actively working on." %}

### Intel RealSense D455
Our prototype, based on the NVIDIA Jetson TX2, leverages the Intel RealSense D455 as its camera payload. Our first goal is to be able to evaluate this camera system. To do so, it is first necessary to calibrate the camera for use in water, as the cameras come from the factory calibrated for air. To facilitate this, we have created a more sturdy version of the OEM calibration board Intel provides to manufacturers. This was necessary as the provided board is unsafe to put into the water.

Allen Kan and Abhi Sachdeva worked together to calibrate the Intel RealSense underwater.  Unfortunately, their efforts to date have been unable to successfully achieve this due to the dynamics of a flat lens in an underwater enclosure. We intend to implement custom calibration beyond Intel’s calibration procedure to solve this.

In addition to the difficulty with calibrating this system, we have also observed that the light from the built-in, structured light projector is reflected back to the camera such that it washes out the image. Once calibration is complete, we will further test this platform with the structured light disabled.

### OAK-D
The OAK-D is the other off-the-shelf depth camera system we evaluated. This system has a similar feature set to the Intel RealSense D455, except it does not have a structured light projector. This system has a higher image and depth resolution than the Intel RealSense D455.

To use this system underwater, it also needs to be calibrated.  Harish Vasanth and Shaurya Raswan have taken point on this project.  They have successfully performed calibration in air but have not yet performed underwater calibration.

Like the Intel RealSense, this camera also observes issues with distortion caused by the lens in an underwater enclosure. As such, calibrating this system has been paused until we can determine the impacts of the flat lens distortion in the underwater enclosure.

### Ego Qoocam
The Ego Qoocam is an off-the-self commodity camera for virtual reality. As it has a small, fixed baseline, this system again has similar issues with distortion caused by enclosures. Thus, calibrating this system underwater is on pause.

In the air, we have used this platform for testing other stereo camera pairs. Though the Ego Qoocam may have a lower resolution than other potential camera pairs, such as the Lucid Tritons or GoPros, it is easier to achieve synchronization between cameras due to the Qoocam's comparatively less engineering, making it highly convenient. 

During our in-air testing, we were able to calculate the intrinsics of each of the cameras provided by the Qoocam as well as the extrinsics of the system. With these, Nicholas Chua and Vancheeswaran Vaidyanathan have evaluated methods of calculating disparity. The most success they have had calculating disparity has been using machine learning. Trained on our RTX A600 NVIDIA GPU.

{% assign image = "assets/fishsense/2023-06-20-qoocam-left.png" | resize: "400x225" | absolute_url %}
{% include img_caption.html
    src=image
    caption="Here is an example image from the left sensor of our Qoocam; we can merge this with an image from the right sensor using our model to calculate a disparity map." %}

{% assign image = "assets/fishsense/2023-06-20-qoocam-depth.png" | resize: "400x225" | absolute_url %}
{% include img_caption.html
    src=image
    caption="Above is an example of such a disparity map calculated with machine learning. Here blue objects are closer to the camera." %}

### Future Work
Our most immediate goal for this project is to solve our flat port distortions. This will allow us to resume our evaluation of these cameras in an underwater environment. Once we do so, we can completely calibrate the Intel RealSense, OAK-D, and Qoocam underwater. We can also begin working on a disparity model for the Qoocam underwater.

This project is partly funded by an NVIDIA Applied Research Accelerator Program project.
