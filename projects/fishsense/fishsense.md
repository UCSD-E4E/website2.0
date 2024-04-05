---
layout: project
permalink: /fishsense
title: Fishsense
tag: fishsense
enable_nav: false
---
Monitoring fish species to keep track of their population growth and general health is vitally important. Current techniques for assessing fishes range from “capture and release” methods to manually conducting surveys within an area. In particular, our collaborators at the Scripps Institute of Oceanography and the Reef Environmental Education Foundation ([reef.org](reef.org)) are interested in studying the lengths within a fish population over time to allow fisheries to better manage their stocks. 

![]({{"assets/projects/fishsense/fishsense-lite-system.png" | absolute_url}})
Image of Fishsense Lite module.
Currently, such fish length data is gathered by employing human divers to manually survey and area and visually estimate and record the lengths of individual fish. This method is prone to inaccuracy, while also requiring each diver to be trained to visually estimate fish length. We intend to ease this data collection process by developing a prototype device that will perform length estimation automatically. 


![]({{"assets/projects/fishsense/P7170124-768x576.jpg" | absolute_url}})
Diver using Fishsense Lite camera for data collection.
The current prototype uses a standard dive camera with a rigidly attached waterproof laser pointer. The laser allows us to extrapolate an estimate of the fish’s distance away from the camera, from which fish length can be calculated.

![]({{"assets/projects/fishsense/P7170098-1-768x576.jpg" | absolute_url}})
Laser dot on a male California Sheephead.
To estimate fish length automatically, we require the use of computer vision techniques to detect the laser point, along with the fish head and tail points. These points are all assumed to be at the same distance from the camera as the laser dot, and that information can be used to calculate the distance between the two laser dots.

If you wish to learn more about this project, contact Christopher Crutchfield ([ccrutchf@ucsd.edu](ccrutchf@ucsd.edu)).