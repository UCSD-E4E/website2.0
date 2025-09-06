---
date: 2025-08-20 00:00:00-08:00
description: null
featuredImage: TODO
author: Sean Perry, TODO
layout: blog-post
slug: /aid-knowledge-graphs-reu-2025
title: "Listening Without Labels: Unsupervised Exploratory Data Analysis for Bioacoustics"
categories:
- news-and-updates
tags:
- reu
- reu2025
- summer
- acoustic-species-id
- bioacoustics
---

Images are straightforward to interpret. They’re intuitive to human brains, and, owing to their prevalence, well-studied. Sound, by contrast, can only be experienced over time, requires undivided attention, and is often clouded by ambient complexity. While this complexity can make sound harder to analyze, it also carries ecological information that images miss. As such, bioacoustics have become an increasingly useful method to monitor ecosystem health in a cost-effective manner. AudioMoths, for example, are palm-sized recorders that can gather over 35 days of audio on a single charge.

{% include 
    img_caption.html
    src="assets/acoustic_species_id/2025-08-20_audiomoth.png"
    caption="AudioMoth device"
%}

In an ideal world, every ecosystem would come with its own complete set of labeled species recordings, enabling machine learning models to monitor populations and assess ecosystem health. But what do you do when labelled species data is sparse for your ecosystem of interest, as is often the case? Or what if you don’t even know what species reside in that ecosystem? To get around this, our focus this summer has been to use various deep learning and signal processing methods to characterize soundscapes, asking questions such as: how does the soundscape vary over the day, or even the year? What taxa are present within the soundscape, and what can we infer about the habitat quality based on this?

Our team this summer, consisting of Dhruv Tomar, Siya Kamboj, and Anu Jajodia, have been collaborating with two National Geographic Explorers: Muha Gomate and Professor Paola Rodríguez. Muha is a musician from Mozambique who aims to create an hour-long collage to represent the beauty and diversity of Gorongosa National Park’s soundscape throughout the year. Professor Rodríguez from the University of Guadalajara, on the other hand, aims to use bioacoustics to help identify sounds that can distinguish degraded and healthy coral reefs from the Mexican Tropical Pacific to aid reef restoration efforts.

These two projects may sound wildly different from each other, but the problems are really one in the same. Our overarching goal has been to build a general pipeline to reveal meaningful relationships and formulate testable ecological hypotheses from large bioacoustic datasets that lack labeled data, avoiding the need to spend countless hours manually labelling data. In the rest of this post, we will be detailing the various techniques we have been using to reach our goal, how we’ve put it all together using a knowledge graph, and our future steps.

# The Ecoacoustic Global Complexity Index (EGCI)

The first technique we began exploring, EGCI, was first documented in Colonna et. al. 2020 and uses information theory quantifiers to describe soundscapes. The paper first calculates Shannon’s Entropy, which describes the “randomness” of a distribution, in this case the amplitude of a soundwave. Then, this value is multiplied by the Jensen-Shannon divergence between the sample distribution and a uniform distribution (white noise in the context of audio) to obtain the Generalized Statistical Complexity Measure. Complexity, when plotted against entropy, is often enough to identify soundscapes, and unlike deeper approaches, is rooted in known real-world meaning. Though EGCI may take many forms depending on the population, a distribution of entropy with high variance will result in a characteristic concave shape, which results from the lag parameter formed during autocorrelation of the amplitude distribution.

As seen below, this characteristic curve results from a sample from coral reef audio, colored by the degradation of the reef. Notably, a decrease in entropy seems to increase the variance of complexity, though we have yet to derive the reason. To make sense of the curve, we cut out this variance by restricting entropy to the [0.9, 1] interval. In this domain, we see linearity emerge between different classes, providing a clear, explainable method to understand the environments that each of these sound samples comes from. However, this kind of statistical work requires a great deal of human input and could manifest itself in very different ways for different domains. It’s useful, but perhaps doesn’t give us the whole picture.

{% include 
    img_caption.html
    src="assets/acoustic_species_id/2025-08-20_egci_curve_1.png"
    src2="assets/acoustic_species_id/2025-08-20_egci_curve_enlarged.png"
%}

# Embeddings and Clustering

Embeddings have been around for a while at this point. It’s worth mentioning that in this case, embeddings refer to latent space vector representations of audio, images, or text. Their value has been on display to the general public since OpenAI made use of Vaswani et. al.’s Transformers to create their various GPT (gradient pretrained Transformers) models, including ChatGPT, a text-to-text attention-based model utilizing billions of parameters. Those models convert text into embeddings prior to doing all of their inference.

In our case, the embeddings are the star. We don’t know what we’re looking for precisely, so it’s difficult to implement a “decoder”, which makes sense of the embeddings to do some task. Instead, we found different ways to train an “encoder”, the component which converts audio into vectors. First, we had to convert the audio signal into an. It has been long established that one of the best ways to classify audio is to create a spectrogram, which is effectively a heatmap of amplitude on a grid where x is time and y is frequency. We take this as input and feed it into what is essentially a convolutional neural network (CNN), acting as an encoder. We squeeze the spectrograms down into a vector of predefined length and force a decoder to try and upsample the vector back to the original spectrogram, computing loss as the perceptual difference in the two spectrograms as calculated by mean square error using a Visual Geometry Group (VGG) model to reduce spectrograms to perceptual features.

{% include 
    img_caption.html
    src="assets/acoustic_species_id/2025-08-20_autoencoder.png"
    caption="Autoencoder schema"
%}

What do we do with these vectors? High dimension spaces are hard to visualize for humans, so we use the Uniform Manifold Approximation and Projection (UMAP) algorithm to reduce the vectors to 2D. We then tried various 2D clustering methods, with HBDSCAN and Gaussian Mixtures as the most successful methods. We test by comparing to known classifications, such as time of day, degraded/non-degraded status. We can then put these clusters into our dataset as labels for our network visualization.

{% include 
    img_caption.html
    src="assets/acoustic_species_id/2025-08-20_clusters.png"
    caption="Clusters colored by known labels (left) and HBDSCAN labels (right)"
%}

# Pattern Discovery

Another part of our process is to discover patterns within our data. One technique we have been using to accomplish this is template matching. For our purposes, template matching consists of taking the spectrogram of a particular sound of interest, then sliding this template across the dataset to find matches for that sound. Ultimately, it serves as an efficient method to find examples of particular sounds in data without the need for labels as would be needed for machine learning techniques.

An additional method we used specifically for our coral reef project is SurfPerch. SurfPerch is a model described in Williams et al., 2025 that was trained on ReefSet, the largest currently assembled dataset of coral reef sounds. This serves as a useful way to classify sounds found in our data from the Mexican Tropical Pacific. Using the results from these two methods, we can associate certain sounds with an array of variables such as time of day, habitat quality, and season to create something called a knowledge graph.

# Putting It All Together: Knowledge Graphs

Now that we have implemented many methods to extract information from audio files, how do we put it together to gather educated, testable hypotheses about the soundscape? We propose the use of knowledge graphs, an organized network that semantically connects real-world entities or nodes to each other. In our case, the entities or nodes include pieces of information such as audio file embeddings, the time and season that the audio was recorded, the location of recording, EGCI results, template matching results, and so on. The structure of a knowledge graph is flexible, allowing the user to enter any combination of nodes or edges as desired.

The graph structure is then inputted into the Heterogeneous Graph Transformer, a graph neural network architecture that generates embeddings for each node by taking into account what each node represents as well as its edges and neighbors. Next, in order to create links amongst nodes, the graph structure is inputted into a multilayer perceptron, which takes two node representations (the source node and destination node), concatenates them, and outputs a number indicating how likely those two nodes should be connected.

These predicted links serve as testable hypotheses that semantically connect two pieces of information. For example, some key hypotheses we were able to gather was that the presence of a biophonetic cascading sawtooth wave, taken from ReefSet, has a strong connection to non-degraded reefs. Using a chi-square test, we were able to verify that this correlation was indeed statistically significant. We also deduced that bat vocalizations are typically present at night in Gorongosa National Park, supported by the ecological literature and conversations with our collaborator.

In the future, we hope to experiment with knowledge graph inputs to determine what combination of information produces the best results. For the Gorongosa National Park data, we have explored splitting individual audio files into five-second chunks and temporally connecting them. Then, template matching results are connected to the particular chunk which contains the corresponding timestamp. This will better reflect the temporal and seasonal shifts in Gorongosa National Park. By contrast, for the coral reef data, we will explore removing audio files from the graph and delving deeper into how the relationships connect to each other, since we are more interested in evaluating relationships within the soundscape.

{% include 
    img_caption.html
    src="assets/acoustic_species_id/2025-08-20_knowledge_graph.png"
    caption="An example of a knowledge graph, applied to our data from Gorongosa National Park"
%}

# Pipeline

In order to make our work extensible to other unsupervised bioacoustic discovery projects, we developed a pipeline that runs our methods over unseen bioacoustic files. The user simply inserts metadata and/or annotations for bioacoustic audio files and checks off a toggle determining which methods should be run. Then, the data is chunked into intervals and the methods specified by the user are run over each chunk. The final results are stored in the knowledge graph, allowing the model to form connections between the soundscape, which can later be verified statistically.

# Future Work

Although knowledge graphs have been widely used in other fields (such as Google’s Knowledge Vault, announced in 2014), applying knowledge graphs in the field of bioacoustics is novel. In the future, we hope to extend our pipeline to run additional algorithms and insert their output into the knowledge graph. For instance, currently, our pipeline allows the user to choose whether they want to insert template matching or EGCI results into the knowledge graph; however, in the future, we hope to allow the user to insert the results of other algorithms into the knowledge graph. We also hope to run more experiments, such as incorporating the embeddings from the autoencoder in the knowledge graph or pruning the graph to only maintain relevant nodes and edges.