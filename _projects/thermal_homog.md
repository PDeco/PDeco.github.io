---
layout: page
title: Thermal Navigation
description: Visuals from the front end.
img: assets/img/Combination_raw_h264.gif
importance: 1
category: "Guidance, Navigation, and Control"
related_publications: false
---
In visual-inertial navigation, we use an inertial sensor to quickly predict the state of the system, and a camera to correct it periodically. Typically, the inertial measurements come from both an accelerometer and a gyroscope, but it is possible to reduce the reliance down to simply the gyroscope -- given that the trajectory adheres to certain profiles. 

The question is for my thesis thus became: can a probabilistic estimator (in this case an Iterated Extended Kalman Filter) be used to correct the assumption-constrained predicted state of a system and can it be done with a thermal camera to reduce reliance on GNSS and good lighting conditions (e.g. night time, or indoors)?

The answer is yes, and the results are shown in the videos below. 

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://www.youtube.com/embed/TvHgHuwdi4w?si=NjdYRF5tJgDnQN1I" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://www.youtube.com/embed/jgbRRfh_y6U?si=5LhXTMO_SlIVJ1iQ" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
</div>
<div class="caption">
    Thermal feature tracking results from my thermal-inertial navigation system subjected to conditions of thermal contrast varying from adequate (right) to poor (left).
</div>

What is seen in the videos is the projection of the bounding box from the reference image onto the current image. Alignment of the bounding box onto the tracked pattern indicates that the system is accurately tracking the state of the camera.