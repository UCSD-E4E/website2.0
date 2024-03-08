---
date: 2014-06-26 18:33:08+00:00
description: null
featuredImage: /assets/2014-06-26-tahoe-1.jpg
layout: blog-post
slug: /expedition-lake-tahoe
title: Expedition Lake Tahoe
author: Antonella Wilby
categories:
- nautical-archaeology
- stereo-diving-rig
- underwater-projects
tags:
- 3d-reconstruction
- archaeology
- computer-vision
- exploration
- imaging
- nautical-archaeology
- shipwrecks
- structure-from-motion
- underwater
---
Engineers for Exploration members have just returned from an expedition to Emerald Bay, Lake Tahoe, California, where they were imaging a pair of sunken Gold Rush-era barges in collaboration with archaeologists from the [Atlantic World Marine Archaeology Research Institute](https://www.amari-archaeology.org/).

This project aims to provide digital tools for documentation of underwater archaeological sites. Conventional nautical archaeology techniques rely on recording the geometric structure of a shipwreck or other site with a tape measure, which is laborious and time-consuming. We aim to augment this process by providing digital tools for accurately capturing the 3D structure of a site, in addition to providing information-rich 3D visual data which archaeologists can use to analyze a site remotely. The video below shows an example of a wreck being recorded using conventional methods.

<figure>
<iframe width="560" height="315" src="https://www.youtube.com/embed/L7TJK6qwxc8?si=mQpbzGNhTXJ4rVzb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<figcaption>Mike Bianco from Scripps Institute of Oceanography and Piotr Bojakowski from AMARI Archaeology recording one of the underwater barges using conventional nautical archaeology techniques. Video © [Robert Zuill](https://www.robertzuill.com)</figcaption>
</figure>

A digital imaging technique that has gained momentum in terrestrial archaeology is called Structure from Motion, which is an algorithm for turning multiple 2D images of a scene into a 3D model. However, Structure from Motion is not yet a fully-viable technique for recording underwater archaeological sites because the complexities of the underwater environment tend to make the software perform poorly, resulting in sparse, inaccurate, or poorly-reconstructed 3D models.

Among the technologies we deployed at Lake Tahoe was our [Stereo Diving Rig]({{'/stereo-diving-rig' | absolute_url}}). In addition to optical sensors, this rig incorporates a variety of position sensors which help the rig align the cameras more accurately during the process of Structure from Motion. 

<figure>
<iframe width="560" height="315" src="https://www.youtube.com/embed/4tQb9h5dbE8?si=Rqfs8zNSNNfh1I1N" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<figcaption>Perry Naughton from Center of Interdisciplinary Science for Art, Architecture, and Archaeology (CISA3) digitally recording a barge for post-processing into a 3D model. Video © [Robert Zuill](https://www.robertzuill.com)</figcaption>
</figure>

The video below shows a 3D reconstruction of one of the Emerald Bay barges, created using commercial Structure from Motion software.

<figure>
<iframe width="560" height="315" src="https://www.youtube.com/embed/mUuxQBkg4ws?si=zA-xEfD_fElBvEkb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<figcaption>3D reconstruction using Structure from Motion of an underwater barge in Lake Tahoe</figcaption>
</figure>

As you can see in the above video, the overall structure of the barge has been captured in the 3D reconstruction, but much of the detail is missing due to the poor underwater performance of many computer vision algorithms. Our future work will focus on refining both our imaging platforms and the Structure from Motion algorithm to improve performance in the underwater environment. We anticipate that this work will vastly increase the viability of Structure from Motion as a tool for underwater archaeology research.
