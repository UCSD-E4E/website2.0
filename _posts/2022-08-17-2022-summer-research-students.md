---
date: 2022-08-17 03:55:35+00:00
description: null
featuredImage: assets/2022-08-17-reu-students.jpg
layout: blog-post
slug: /2022-summer-research-students
title: 2022 Summer Research Students
author: Nathan
categories:
- news-and-updates
students:
- bio: Emily Wong is a fourth year undergraduate student at Stanford University, majoring in Mechanical Engineering with a minor in Modern Languages. She is particularly interested in the intersection between robotics and oceanographic conservation. This summer, she is working with the FishSense team to find the best underwater calibration method for the team’s stereo depth cameras. She is also designing mechanisms and tactics for FishSense deployment on boats for the California Collaborative Fisheries Research Program (CCFRP), with the goal of simplifying the fish length measurement process and minimizing the amount of time that fish need to spend out of water. In her free time, you can find her exploring somewhere new, reading by the sea, or chasing other people’s dogs.
  photo: assets/people/e.wong.jpg
- bio: Scott Switzer is an undergraduate studying Electrical Engineering at the University of British Columbia in Canada (pronounced “kan”-“uh”-“duh”). For the FishSense team, Scott spent summer 2022 making various improvements to the existing hardware and firmware design. Scott’s interests include long walks on the beach, surfing, chicken spaghetti at Chickalinis, fish and boats.
  photo: assets/people/s.switzer.jpg
- bio: Bella Humphrey is a fourth year undergraduate at the University of Georgia, majoring in Computer Science and Mathematics. Her interests lie in the intersection of computer science, math, and environmental conservation. This summer she is excited to be working on machine learning as a part of the FishSense team, exploring improvements in object detection and segmentation on deck as well as underwater. In her free time, she enjoys making pasta, hiking, and going to the beach!
  photo: assets/people/i.humphrey.jpeg
- bio: Pranjal Chatterjee is a rising senior at Lynbrook High School, CA, with an interest in studying Applied Physics and Electrical/Computer Engineering in college. Previously, he has attended the COSMOS UCSD Robot Inventors summer program, where he worked to create robots with various capabilities and ended with designing and building a drawing robot that required differential modeling of a system using rotational kinematics and calculus. This summer, he is working with the E4E Acoustic Species Identification team, generating and implementing ideas for increasing precision using unsupervised clustering on BirdNET-Analyzer embeddings to filter out false positives from the model’s predictions. He has also finished generalizing the types of files that the models could analyze and optimizing the performance of annotation isolation functions. Outside of STEM activities, he enjoys playing the trombone, reading, and spending time with friends and family.
  photo: assets/people/p.chatterjee.jpeg
- bio: "Anshul is a second year Electrical Engineering student at UCSD. This summer, he worked on the Smartfin project; specifically on firmware validation, sensor calibration, and fin manufacturing. He thinks the best part about Smartfin is its potential for any surfer anywhere in the world to be able to acquire one and help fight climate change. Although sadly, despite spending months on Smartfin, he still can't surf. In his free time, Anshul enjoys playing tennis, biking, and backpacking. He wishes to go on adventures all around the world and see its beauty: all the more reason to engineer sustainable solutions to the environment's biggest challenges."
  photo: assets/people/a.garde.jpg
- bio: Sean Perry is a 3nd-year undergraduate at UCSD with a Math - Computer Science major and a Data Science minor. As a project lead on the Audio Acoustic Identification project, he is working towards reducing the cost of labor in creating high-quality training data for bird calls. Through developing user agreement metrics for a manual labeling platform called Pyrenote and expanding the range of tools that aim to automatically label data, the hope is that it becomes easy enough for people to produce large high quality datasets to create classifiers to monitor the biodiversity of the Peruvian Amazon. When not working on the project, Sean enjoys relaxing with video games, listening to music, and not working.
  photo: assets/people/s.perry.jpg
- bio: Frank Chaqueco is a rising junior at UC San Diego, majoring in electrical engineering with a focus on electronic circuits and systems. This summer he is working on the Radio Telemetry Tracking project. He is working on developing the sleep timer firmware and electronics for the stationary tracker towers that will monitor lizards in Arkansas. In his free time, Frank likes to work out, ride his bike, swim, and try new foods.
  photo: assets/people/f.chaqueco.jpg
- bio: Vanessa Salgado attends the University of California, Santa Barbara. She is a senior studying Computer Science and Chicano Studies. She is working with the Acoustics Species Identification team to generate strongly labeled data of bird calls in order to retrain machine learning pipelines to accurately identify bird species vocalizations. Her intentions are to use technology for environmental good, combat the effects of climate change and leave Earth better than how she found it. Her personal interests are reading memoirs, discussing films, making lists of her future goals, spending time with friends and family, and discovering new music.
  photo: assets/people/v.salgado.jpg
- bio: Prateek Rout is a rising sophomore are UIUC, majoring in Mechanical Engineering. He is working on the Radio Telemetry and developing a system of 10-foot towers to track collared lizards in Arkansas and designing a housing for electronics to be attached to a drone to track boas in the Turks and Caicos Islands. He is also helping develop the molds for new fins for the SmartFin project. During the school year, he works on carbon fiber molding and designs for super-efficient cars on the Eco Illini Supermileage team at UIUC.
  photo: assets/people/p.rout.jpg
- bio: Melina is a rising sophomore at University of California, San Diego, majoring in Computer Science. This summer, she is working on continuing software development on the radio telemetry tracking project. This involves making changes to the current use of TCP and threading to accommodate multiple tracking towers (instead of only one in previous iterations of the project). Additionally, she is implementing the communication protocol between tracking towers and the sleep timer to integrate the sleep timer into the software system. In her free time, Melina enjoys figure skating, exploring dessert shops, and playing board games with friends.
  photo: assets/people/m.dimitropoulou.jpg
- bio: Samantha Prestrelski is a second-year undergraduate student at UC San Diego majoring in Mathematics-Computer Science. She is working on the Acoustic Species Identification team, using machine learning to automatically segment and classify bird vocalizations in open-source audio datasets and field recordings. In her free time, Sam likes exploring campus, baking, and spending time with friends.
  photo: assets/people/s.prestrelski.jpg
- bio: Robert O'Brien is a rising junior at Princeton University studying electrical and computer engineering. This summer he mainly focused on improving firmware for the Smartfin team. Additionally, he made improvements in Smartfin's hardware and fin manufacturing techniques. Robert hopes to continue working with embedded systems and conservation after he graduates. Robert likes to surf and play rugby, however back in his hometown in Virginia there aren't many waves.
  photo: assets/people/r.obrien.jpg
---
This summer, we are hosting 12 students from around the US in our 2022 summer research program, finally back in person at UC San Diego.  We'll be working on measuring fish length, building SmartFins, labelling bird calls, and tracking animals.  Meet our students by reading their bios below:

## Student Researchers
{% for student in page.students %}
<div class="floatclearfix">
    {% if student.photo %}
    <p><a href="{{ student.photo | absolute_url }}"><img alt="{{student.name}}" class="{{student.align}}" src="{{student.photo | resize: '180x240'}}"></a></p>{% endif %}
    <p>{{student.bio}}</p>
</div>
{% endfor %}