---
date: 2014-01-09 06:16:35+00:00
description: null
featuredImage: /assets/2014-01-09-copter-geisel.jpg
layout: blog-post
slug: /sony-qx100-quadcopter-testing
title: Sony QX100 Quadcopter Testing
author: Eric Lo
categories:
- quadcopter
gallery:
- /assets/2014-01-09-copter-geisel.jpg
- /assets/2014-01-09-calit2-night.jpg
- /assets/2014-01-09-ebu1-back-night.jpg
- /assets/2014-01-09-qx100-down.jpg
- /assets/2014-01-09-ebu1-1.jpg
- /assets/2014-01-09-ebu1-2.jpg
- /assets/2014-01-09-ebu1-3.jpg
- /assets/2014-01-09-ebu1-4.jpg
- /assets/2014-01-09-ebu2-1.jpg
- /assets/2014-01-09-cmrr-1.jpg
- /assets/2014-01-09-cmrr-2.jpg
- /assets/2014-01-09-wlh-1.jpg
- /assets/2014-01-09-pfe-1.jpg
- /assets/2014-01-09-cmrr-3.jpg
- /assets/2014-01-09-geisel-1.jpg
- /assets/2014-01-09-geisel-2.jpg
- /assets/2014-01-09-geisel-3.jpg
- /assets/2014-01-09-ebu1-5.jpg
- /assets/2014-01-09-cmrr-4.jpg
- /assets/2014-01-09-ebu2-2.jpg
- /assets/2014-01-09-pc-1.jpg
- /assets/2014-01-09-wlh-2.jpg
- /assets/2014-01-09-wlh-3.jpg
- /assets/2014-01-09-ebu1-6.jpg
- /assets/2014-01-09-ebu2-3.jpg
- /assets/2014-01-09-calit2-1.jpg
- /assets/2014-01-09-sme-1.jpg
- /assets/2014-01-09-ebu2-4.jpg
- /assets/2014-01-09-bear-1.jpg
- /assets/2014-01-09-bear-2.jpg
- /assets/2014-01-09-calit2-2.jpg
- /assets/2014-01-09-bioe-1.jpg
- /assets/2014-01-09-bioe-2.jpg
---
We've been hard at work bringing up a quadcopter platform for aerial imagery surveys, as well as preparation for the radio collar tracking effort. For our aerial imagery, we want the highest quality picture from the lightest package, and Sony's QX100 fits the bill, utilizing a 20.2MP 1" sensor and weighing only 182g. Here's our experience interfacing with the QX100, and a sample of the images we took from the copter.

[![]({{'/assets/2014-01-09-qx100-copter.jpg' | resize: '1024x682'}})]({{'/assets-2014-01-09-qx100-copter.jpg' | absolute_url}})

The QX100 features a Wi-Fi interface for control via a smartphone, so we thought we'd slap it on the copter and see how far it could go. Testing with a number of Android devices on hand, we quickly determined that that was not viable, with the liveview lagging and failing soon after the copter took off. In an attempt to scrounge up more signal strength without adding weight to the copter, we decided to experiment with a USB Wi-Fi dongle and a directional antenna connected to a laptop. To interface the camera to the laptop, we turned to Sony's Remote Camera API, and wrote a python script that would allow us to command image captures, as well as display a liveview so we can frame our shots. This was moderately successful, with some dropped frames but an otherwise stable link at 200ft, though it was not a very smooth experience. Both the software and hardware setups have room for improvement, so this is an encouraging first result.

We are releasing the interfacing script open source so others can experiment with it, and possibly apply it to other interesting projects. All of Sony's Wi-Fi enabled cameras use the same interface, so the script should work on other cameras such as the NEX-5T as well, though it will likely need to be modified for the appropriate IP address, as we did not implement the device discovery. Note that this is still under development, so it has issues and is not yet user friendly.

[https://github.com/UCSD-E4E/qx100-interfacing](https://github.com/UCSD-E4E/qx100-interfacing)

[![IMG_1408]({{'/assets/2014-01-09-IMG_1408.jpg' | resize: '1024x682'}})]({{'/assets/2014-01-09-IMG_1408.jpg' | absolute_url}})

We had much more success with the second approach we tried, mechanically triggering the shutter button with a servo driven from the Ardupilot. Using this method, we were able to quickly and reliably capture images, but without a liveview, framing the picture was difficult. This is relevant for aerial photography, but not for survey missions where the camera should be triggered regularly. Unfortunately, the QX100 has a habit of turning itself off when inactive, which seems to mean not being connected via Wi-Fi, so it cut out the last half of the attempted mapping mission.

The optimal approach we are now aiming for is to have a Wi-Fi liveview with a repeater on the copter to see what is going on while triggering captures with a servo to ensure consistent and reliable image capture.

In terms of achieved image quality, the QX100 is currently not well suited for aerial mapping missions. Due to lack of a shutter priority mode, program auto often chooses slower shutter speeds, which causes significant motion blur from the moving copter. The good news is that it works well while pointed forwards, as shown in the image gallery below. Sony is releasing a new firmware update for the camera at the end of January 2014 that provides a shutter priority mode, so we will try again then.

<figure>
<a href="{{'/assets/2014-01-09-ebu1-back-night.jpg' | absolute_url}}"><img src="{{'/assets/2014-01-09-ebu1-back-night.jpg' | resize: '640x480'}}" alt="The back of EBU1 at night"></a>
<figcaption>The back of EBU1 at night</figcaption>
</figure>

In addition to the imagery shown below, we also stitched some of it together to provide a 360 degree panoramic view from various locations on UCSD campus (requires silverlight plugin to view).

Hope you enjoy the pictures!

{% for image in page.gallery %}
<a href="{{ image | absolute_url }}">
<img alt="sony-gallery" src="{{ image | resize: '150x150' }}" width="150px" height="150px">
</a>{% endfor %}