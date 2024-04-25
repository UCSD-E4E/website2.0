---
date: 2021-04-30 02:03:39+00:00
description: null
featuredImage: /assets/2021-04-30-aid-median-map.png
layout: blog-post
slug: /measuring-bird-presence-in-the-peruvian-amazon-using-neural-network-predictions
title: Measuring Bird Presence in the Peruvian Amazon Using Neural Network Predictions
author: Nathan Hui
categories:
- news-and-updates
tags:
- acoustic-species-id
---
On April 13th, 2021, the Acoustic Species Identification project lead Jacob Ayers posted a dataset containing the predictions from a Recurrent Neural Network (RNN) trained to estimate the probability of bird presence (global scores) across close to 100,000 audio clips from the Peruvian Amazon. The dataset also contained information about the Audiomoth audio recording devices such as latitudinal and longitudinal coordinates and when each audio clip was created. The Acoustic Species Identification team and its collaborators took on the task of interpreting the dataset and producing different visualizations of their findings.

{% include
  img_caption.html
  src="assets/2021-04-30-aid-Matthew_Google_Map.png"
  src2="assets/2021-04-30-aid-all_audiomoths.png"
%}

The map on the left (produced by Matthew Mercurio) shows where in the Peruvian Amazon the Audiomoths were placed as well as having the yellow pins represent whether or not the audio recorded fits an expected trend (more discussion on this coming). The graph on the right demonstrates the challenge of trying to derive meaning from a dataset with so many data points. 

{% include
  img_caption.html
  src="assets/2021-04-30-aid-mathias_all_audiomoths.png"
%}

One of the main San Diego Zoo Wildlife Alliance collaborators, Mathias Tobler, averaged all of the clip global score predictions with respect to time and was able to demonstrate the capability of the Microfaune RNN to pick up on the expected trend of bird vocalization activity peaking during dawn and dusk.

{%
    include
    img_caption.html
    src="assets/2021-04-30-aid-AM1.png"
    src2="assets/2021-04-30-aid-AM3.png"
    src3="assets/2021-04-30-aid-AM6.png"
%}

The team did find an unexpected trend of four six hour interval peaks as seen in the "Strange Pattern" figure. Jacob decided to plot the only Audiomoth device that was listed as "Off-Road" and compared its closest neighbor "Nearby Road Audiomoth". These plots also demonstrated a contrast between the expected Dawn-Dusk Chorus and the unexpected six hour intervals.

In the future, the Acoustic Species Identification team will investigate into what is causing the odd six hour intervals. They also hope to produce more datasets derived from the various audio recordings and tools they work with, which can be used for future team data science challenges.

<iframe src="{{'assets/aid-median_bubble.html' | absolute_url}}" title="Interactive Map" width="100%" height="600"></iframe>
