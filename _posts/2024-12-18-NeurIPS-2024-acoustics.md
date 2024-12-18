---
date: 2024-12-18 9:00:00-7:00:00
description: null
featuredImage: assets/acoustic_species_id/2024_12_18_NeurIPS_Poster.jpg
author: Sean Perry and Ludwig von Schoenfeldt
layout: blog-post
slug: /acoustics-at-neurips-2024
title: Acoustic Species ID goes to NeurIPS 2024!
categories:
- news-and-updates
tags:
- acoustic-species-id
- bioacoustics
---

Our work, "A Deep Learning Approach to the Automated Segmentation of Bird Vocalizations from Weakly Labeled Crowd-sourced Audio" was accepted and presented at NeurIPS 2024 in the "Tackling Climate Change with Machine Learning" Workshop hosted by Climate Change AI! Congrats to the authors: Jacob Ayers, Sean Perry, Samantha Prestrelski, Tianqi Zhang, Ludwig von Schoenfeldt, Mugen Blue, Gabriel Steinberg, Mathias Tobler,Ian Ingram, Curt Schurgers and Ryan Kastner.

{% include 
    img_caption.html
    src="assets/acoustic_species_id/2024_12_18_NeurIPS_Canda_Place.jpg"
    caption="View of Canda Place, an iconic landmark of Vancover. View taken from the east side of the Vancover Convention Center. The confrence actually took place in both buildings with an underground tunnel connecting the two, as seen on the bottom right of the image. Taken by Sean Perry"
%}

This focused on the issue of weakly labeled datasets, often associated with large bioacoustic crowdsource dataset. Traditional methods frequently use digital signal processing approches to identify the species of interest. This work takes a look at testing these methods with deep learning models. [The paper can be found here](https://www.climatechange.ai/papers/neurips2024/8). Credits to **Mathias Tobler** for frist conceptualizing the idea. 

Key contributions to this work include [PyHa](https://github.com/UCSD-E4E/pyha), the python repository where the main techonologies used in the paper are stored. Credits primarly to **Jacob Ayers** for crediting the repo and vision for the project and **Samantha Prestrelski** for the work has done developing it and carrying out experiments. Further thanks to **Gabriel Steinberg** for his techical contributions with isolation techinques and chunking methods and **Mugen Blue** for his training TweetyNet, which was the most successful method used as seen in the paper. 

Shout out to [Pyrenote](https://github.com/UCSD-E4E/Pyrenote) by Sean Perry for providing the the labeling for the project. 

Last week, **Sean Perry** and **Ludwig von Schoenfeldt** attended NeurIPS 2024 and presented the work! The two traveled out of the country to Vancover, Canda to attend most of the confrence, getting to see hundreds of posters, amazing research in machine learning, and present thier own work! It was an inspiring moment getting to see where the future of the felid could be heading.

Acoustic Species is not done with this work. We will be continue to evalute how these methods may influnce the behavior of upstream models as we continue to work to improve bioacoustic machine learning techinques to identify species of interest. 

{% include 
    img_caption.html
    src="assets/acoustic_species_id/2024_12_18_NeurIPS_North_Vancover.jpg"
    caption="View of North Vancover, taken from the west side of Canda Plance looking northwest. The previous day was raining and the storm had started to move on north, appearing over the valleys of the moutains and the ski resorts. Taken by Sean Perry" 
%}