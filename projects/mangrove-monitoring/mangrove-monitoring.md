---
layout: project
permalink: /mangrove-monitoring
title: Mangrove Monitoring
tag: mangrove-monitoring
enable_nav: false
---

![]({{"assets/projects/mangrove/aburto_lab_photos.jpg" | absolute_url}})
Mangroves are a very valuable and understudied plant species.  They provide $100,000 per hectare per year in services that are critical to the overall health of coastal ecosystems.  Mangroves act as fishery habitats, they sequester carbon, filter runoff, and protect coastlines from hurricanes.

![]({{"assets/projects/mangrove/services_and_loss.jpg" | absolute_url}})

We are collaborating with the Aburto Lab and the Gulf of California Marine Program at the Scripps Institution of Oceanography to use drone and satellite imagery to quantify mangrove species and extent in Baja California.

# REU Summer 2017

During the summer of 2017, Eric Lo, Brynn Hall, and Nikko (Nicholas) Bouck traveled to Baja California with our SIO collaborators to capture drone imagery and ground truth data on the mangroves.  After capturing aerial imagery in Baja California we began to explore machine learning techniques to automate analysis of the data collected. Julien Bloch, from UC Berkeley, and Felix Parker, Johns Hopkins University explored various machine learning algorithms as Nikko Bouck and Brynn Hall built up training data for these algorithms. The image below illustrates the results of the automation efforts over the summer of 2017.

![]({{"assets/projects/mangrove/species_classification.jpg" | absolute_url}})

# Spring 2018 Update

Mangrove Monitoring in Puerto San Carlos

![]({{"assets/projects/mangrove/Day1_full-Team-768x465.jpg" | absolute_url}})

Engineers for Exploration leaders Nikko Dutra Bouck and Eric Lo went to Baja Sur California with [Scripps Institution of Oceanography](https://scripps.ucsd.edu/) (SIO) researchers Astrid Hsu and Joy Kumagai and Beni Martinez from the [Gulf of California Marine Program](http://gulfprogram.ucsd.edu/) from May 9th to May 15th, where the team collected new data to help support the conservation of coastal mangrove ecosystems in Puerto San Carlos, Baja Sur California, México.

The overall goal for expedition was to test data collection methodologies that can provide accurate information about the distribution and extent of Baja’s mangroves. By utilizing remote sensing techniques and on-the-ground methods, this project aims to calculate mangrove biomass by species and region in a quick and efficient manner.  In particular, we developed new methodologies to support and improve our machine learning techniques. Parallel to this, the Aburto Lab spent a substantial amount of time collecting biomass data within the mangroves, information that the Engineers for Exploration team will use to compose a statistical model on species density.

The first day on site, in Mexico, Nikko developed a new methodology for ground truthing aerial surveys that will greatly improve the teams confidence in machine learning classification and crowdsourced labeling.  The methodology is called a perimeter survey which implements a low altitude drone flight that provides imagery so sharp that mangrove species can be classified by leaf shape. At the edge of the mangrove forest, the pilot drops a large species marker on the ground to reference the starting point for drawing polygons around the individual plant species, and then flies at roughly 15 meters above. This new approach is preferred over our [previous approach](http://gulfprogram.ucsd.edu/general/mangroves-from-above-and-below/) because the perimeter survey enables a drone pilot to validate the identity of each plant species while in the field.  The addition of this dataset can dramatically improve the ability to train machine learning algorithms, and provides an excellent reference for analyzing the accuracy of the team’s machine learning efforts.

![]({{"assets/projects/mangrove/labeled_survey-768x474.jpg" | absolute_url}})

Throughout the remainder of the trip, Eric trained the Beni Martinez and Astrid to collect aerial drone imagery for biomass and species analysis at altitudes of 120m and 15m. The long-term vision is that members of the GCMP such as Beni Martinez will train local park rangers in Baja California Sur and scale up these efforts, resulting in a greatly improved workflow that will enable the three organizations involved to identify changes in the environment within a year.  The rangers will be able send the data collected to the GCMP, the Aburto Lab, and Engineers for Exploration where each team will then utilize the machine learning platform to automatically identify changes in mangrove species distribution and provide insight into illegal dumping activities. This Machine Learning platform is currently being developed by John Dorian, Tammy Mok, and Nikko Dutra Bouck and will continue this summer during our NSF REU program.

![]({{"assets/projects/mangrove/IMG_9850-768x512.jpg" | absolute_url}})

Check back soon for results and our updated crowdsourced tool with high resolution imagery.

Beta release:

[https://davidjasperforman.github.io/MLPaintWeb/](https://davidjasperforman.github.io/MLPaintWeb/)

If you are interested in learning more about labeling events or becoming involved in this project contact us. [e4e@eng.ucsd.edu](e4e@eng.ucsd.edu)

SIO collaborators:
Octavio Aburto, Astrid Hsu, Mathew Costa, Joy Kumagai, Alex Makic

<iframe width="800" height="475" src="https://www.youtube.com/embed/obCpmMlv9pw" title="E4E Mangrove Monitoring: Summer 2020" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
