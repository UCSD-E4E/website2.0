---
date: 2014-10-07 22:26:00+00:00
description: null
featuredImage: /assets/2014-10-07-s800.jpg
layout: blog-post
slug: /summer-2014-automated-wildlife-radio-collar-tracking
title: 'Automated Wildlife Radio Collar Tracking: Summer 2014 REU'
author: Eric Lo
categories:
- radio-collar-tracker
---
Although wildlife radio collar tracking is common practice in wildlife research, VHF tracking has not changed much in the past half century. It requires the researchers to go to the field on foot carrying a bulky directional antenna and listening to the received signals. The process of tracking down the collared animals can take anywhere from minutes to hours, depending on the environment. In some cases, it may even be prohibitive to attempt collar tracking, as the number of animals that can be tracked will be limited to the few which are easily accessible. We're working with the San Diego Zoo Institute for Conservation Research to test a technological solution to address this problem.

<figure>
<a href="{{'/assets/2014-10-07-s800-1.jpg' | absolute_url}}"><img src="{{'/assets/2014-10-07-s800-1.jpg' | resize: '1024x768'}}"></a>
<figcaption>Our hexacopter aerial platform, equipped with the custom radio collar tracking payload</figcaption>
</figure>

Our solution consists of an aerial platform that carries a custom radio receiver payload which can detect the radio collar signal. By flying, we can avoid the challenges presented from navigating impassible terrain and cover a significantly larger area than would be possible on foot. In addition, the receiver payload can scan for multiple radio collars at once, streamlining the process of tracking multiple animals.

<figure>
<a href="{{'/assets/2014-10-07-s800-prep.jpg' | absolute_url}}"><img src="{{'/assets/2014-10-07-s800-prep.jpg' | resize: '1024x768'}}"></a>
<figcaption>Flight testing at Warren Field</figcaption>
</figure>

<figure>
<a href="{{'/assets/2014-10-07-s800-landing.jpg' | absolute_url}}"><img src="{{'/assets/2014-10-07-s800-landing.jpg' | resize: '1024x768'}}"></a>
<figcaption>Flight testing at Lake Hodges</figcaption>
</figure>

In order to develop our prototype and validate our implementation, we conducted extensive testing of our system, flight testing in both a sports field as well as a more natural setting. The figure below shows the results of one of our tests. In this test, we placed 3 radio collars in different configurations to determine the effect on our tracking system. One was placed in a tree, another was buried under a pile of rocks, and the last one was up on a hill. Ground truth data was taken with a smartphone GPS to record the actual location of the collar, represented by the large circles. The positions measured by our system are represented by the smaller circles, and show the results of 3 runs to demonstrate repeatability. From our testing, we have determined the error bound of our localization to be within 30 meters.

<figure>
<a href="{{'/assets/2014-10-07-lake-hodges.png' | absolute_url}}"><img src="{{'/assets/2014-10-07-lake-hodges.png' | resize: '1024x768'}}"></a>
</figure>

From the testing done in the summer on our prototype, we have demonstrated the feasibility of our approach for localizing wildlife radio collars. Looking forward, we strive to improve accuracy and expand to longer ranges by moving our payload from a copter to a fixed wing craft.

We would like to thank our collaborators at the Dr. Stesha Pasachnik and Dr. Mathias Tobler for their support, insight, and advice, which was crucial to keep the project on track, as well as Ranger Bryan from the San Dieguito River Valley Conservancy for letting us test at Lake Hodges.
