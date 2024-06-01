---
date: 2016-09-03 22:24:59+00:00
description: null
featuredImage: /assets/humpback.jpg
layout: blog-post
slug: /machine-learning-for-humpback-whale-social-call-classification-2016-reu
title: 'Machine Learning for Humpback Whale Social Call Classification: 2016 REU'
categories:
- underwater-projects
tags:
- bioacoustics
- classification
- machine-learning
- nsf
- research
- reu
- whale
---

Bioacoustics lies in the intersection of biology and acoustics -- it is the study of wildlife and ecosystems through an analysis of the acoustic environment. On a broad scale, audio recordings can inform scientists about the species present in a region as well as about their abundance, which is very valuable for conservation efforts. On a closer look, it may allow scientists to study specific individuals, and even the different types of calls and sounds that individuals produce. This is a very general approach, which can be done noninvasively and on a low budget, and bioacoustic methods have been used to study a large variety of animals, ranging from insects, to songbirds, to elephants, to whales. Furthermore, since acoustics gives a window into environments that are otherwise difficult to examine -- such as the ocean -- marine mammal bioacoustics is especially prominent in current-day research.

Our project during the 2016 summer REU program focused on humpback whale social calls. Our collaborators at the [Thode Underwater Acoustics Lab](https://scripps.ucsd.edu/labs/athode/) at Scripps Institute of Oceanography have deployed hydrophones on humpback whales near Las Cabos, Mexico, to study the social structure and communication patterns of the whale population. To do so, they had to manually examine hours upon hours of data, and find and label all of the present whale calls. This is a difficult, time-intensive task. Through this collaboration with Scripps, our aim is to use this data to create an algorithm for automatic detection and classification of humpback whale calls, to allow ecologists to spend less time manually annotating audio recordings.

Our research this summer involved experimenting with various methods of data processing and machine learning techniques. We started by calculating spectrograms -- a visual representation of audio signals -- and applied several methods to segment the foreground calls and noises. Then, we experimented with different types of feature extraction. Once we had viable features, we fed the data into a supervised classification algorithm that uses Hidden Markov Models to obtain final classification. Further work will improve these methods for segmentation and classification.

[![whale_spectrogram_original](/assets/2016-09-03-machine-learning-for-humpback-whale-social-call-classification-2016-reu_whale_spectrogram_original-1024x280.png)](/assets/2016-09-03-machine-learning-for-humpback-whale-social-call-classification-2016-reu_whale_spectrogram_original.png)


Above are ten spectrograms - a visual representation of acoustic data that shows the intensity of sound across different frequencies through time. The whale calls are boxed and labeled.



[![whale_spectrogram_segmented](/assets/2016-09-03-machine-learning-for-humpback-whale-social-call-classification-2016-reu_whale_spectrogram_segmented-1024x280.png)](/assets/2016-09-03-machine-learning-for-humpback-whale-social-call-classification-2016-reu_whale_spectrogram_segmented.png)


These are the same ten spectrograms after processing. Much of the background noise has been removed, and the calls are clearer.





## Preliminary Results from Hidden Markov Model



The results from the HMM show that it is possible to separate calls like this using HMMs and that less features showed better performance. However, to get better results a more balanced training set is needed. Non whale calls made up about 99.1% of this data.

|9 Features|||30 Features|||
|--- |--- |--- |--- |--- |--- |
|Overall Accuracy|0.68||Overall Accuracy|0.84||
||Precision|Recall||Precision|Recall|
|No Call|0.9|0.73|No Call|0.89|0.91|
|Squeak|0.29|0.17|Squeak|0.2|0.19|
|Low Yap|0.14|0.07|Low Yap|0|0|    
{: .datatable}


**Table 1: **This table compares the overall accuracy of each data set given the number of features in a feature vector. It gives average precision and recall values for each class, derived from k-fold cross-validation where k=10. The HMMs involved used 2 states. The overall data distribution was 21049 no whale calls, 119 squeaks, and 62 low yaps.



Additionally, the noise across different data sets varied causing individual data sets to perform much better than the full combination. Non whale calls of this data set made up about 98.7% of this data.

|9 Features|||30 Features|||
|--- |--- |--- |--- |--- |--- |
|Overall Accuracy|0.72||Overall Accuracy|0.51||
||Precision|Recall||Precision|Recall|
|No Call|0.6|0.77|No Call|0.49|0.48|
|Squeak|0.46|0.5|Squeak|0.41|0.48|
|Low Yap|0.5|0.3|Low Yap|0.2|0.1|
{: .datatable}


**Table 2: **This table compares the overall accuracy of a particular data set a given the number of features in a feature vector. It gives average precision and recall values for each class, derived from k-fold cross-validation where k=10. The HMMs involved used 2 states. The data distribution for this data set was 3692 non whale calls, 29 squeaks, and 19 low yaps.



- _ by Lisa Bauer, Irina Tolkova, Hongyi Zhao, and Antonella Wilby_
