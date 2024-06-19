---
date: 2018-08-30 21:44:28+00:00
description: null
featuredImage: /assets/IMG_20180726_112524.jpg
layout: blog-post
slug: /maya-archaeology-summer-work
title: Maya Archaeology Summer Work
categories:
- tunnel-mapping
---

Archaeologists in Guatemala are studying the Maya and discovering more about their history and culture. One way they do this is by digging tunnels into their temples, allowing them to unearth masks, carvings, graves, and more. We have been working on creating an easy-to-use hand-held 3D mapping system using SLAM algorithms so these archaeologists can easily map the tunnels and document their findings. We already have a working self-contained rig that has been tested with several different algorithms - but this has been done with only one camera. This summer we focused on implementing and testing a multi-camera 3D Scanning setup so that we can compare it with our current single-camera system. We decided to create a rig with two Kinect cameras that are rigidly connected together, which is vital as their relative positions between one another should be static. Our construction of this rig definitely looks like a prototype, but it works well.

{% include 
    img_caption.html
    src="/assets/IMG_20180531_152139-1074x806.jpg"
%}

To perform the testing, we took expeditions to the mud caves in Anza Borrego Desert. These caves are a great testing environment, as they offer very similar conditions to those that the equipment will face in the tunnels of Guatemala - heat, dust, and cramped spaces. This is extremely beneficial, as our first trip showed that we did not test our equipment as thoroughly as we should have: two regulators failed, a Kinect was surged with power causing it to break, and our LED light panel began flickering. Luckily we were able to rewire some of the rig in the field so we could still collect some data, but we needed to go back. 

{% include 
    img_caption.html
    src="/assets/20180805_113104_HDR-1074x604.jpg"
%}



Our next expedition proved to be more successful, and we were able to collect the data we needed. We took scans of the cave with several different algorithms, different cameras, and different camera-setups. We also scanned the cave with a LiDAR, which will be treated as the ground truth.

{% include 
    img_caption.html
    src="/assets/20180819_123230-1074x604.jpg"
%}

Moving forward into the school year, we will now be comparing all of the point clouds we collected to the LiDAR scan. This will allow us to quantify the accuracy of the point clouds, and we expect the multi-camera setup to show clear advantages.

 

 
