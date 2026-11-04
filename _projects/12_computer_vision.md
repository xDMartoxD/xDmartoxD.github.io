---
layout: page
title: Computer vision toolkit
description: Classic OpenCV algorithms (matching, corners, edges, segmentation, detection, optical flow) built up for the vision-guided arm
img: assets/img/projects/computer-vision/sift-matching.jpg
img_alt: "SIFT feature matches drawn as lines between two images of the same object"
importance: 5
category: robotics
---

Before building the [vision-guided robotic arm]({% link _projects/4_vision_arm.md %}), I worked through the classic computer-vision toolbox in Python with OpenCV and NumPy, in a series of Jupyter notebooks. These are the results, run on the course's sample images and videos. The same building blocks ended up in the arm's pipeline: color spaces and thresholding for tracking, and marker detection plus camera geometry for locating objects.

## Image processing

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/computer-vision/hsv.jpg" title="HSV color space" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/computer-vision/blending.jpg" title="Masked blending" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/computer-vision/adaptive-threshold.jpg" title="Adaptive thresholding" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Color spaces (an image viewed in HSV), masked blending of a watermark with bitwise operations, and adaptive thresholding to clean up a scanned crossword.
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/computer-vision/morphology.jpg" title="Morphological opening" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/computer-vision/sobel.jpg" title="Image gradients" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/computer-vision/histogram-equalization.jpg" title="Histogram equalization" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Morphological opening to remove noise, Sobel/Laplacian gradients on a sudoku, and histogram equalization to recover contrast.
</div>

## Detection

<div class="row">
    <div class="col-sm-7 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/computer-vision/template-matching.jpg" title="Template matching" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm-5 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/computer-vision/harris-corners.jpg" title="Harris corners" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Template matching (response heatmap and best match, comparing all six OpenCV methods) and Harris corner detection on a real chessboard.
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/computer-vision/canny.jpg" title="Canny edges" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/computer-vision/grid-detection.jpg" title="Grid detection" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/computer-vision/watershed.jpg" title="Watershed segmentation" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Canny edges with a tuned median-based threshold, chessboard/circle-grid detection (the basis of camera calibration), and watershed segmentation separating touching coins.
</div>

<div class="row">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/computer-vision/sift-matching.jpg" title="SIFT feature matching" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/computer-vision/face-detection.jpg" title="Haar cascade face detection" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    SIFT descriptors with FLANN matching and Lowe's ratio test find a cereal box on a crowded shelf; Haar cascades detect every face in the 1927 Solvay Conference photo.
</div>

## Motion

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/computer-vision/lucas-kanade.jpg" title="Lucas-Kanade optical flow" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/computer-vision/dense-flow.jpg" title="Dense optical flow" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Sparse Lucas-Kanade optical flow tracking Shi-Tomasi corners on a moving hand, and dense Farneback flow (hue = direction, brightness = speed).
</div>

The notebooks also cover MeanShift/CAMShift face tracking, video capture and drawing on live video, and a webcam finger counter. The finger counter learns the background with a running average, segments the hand, and counts the fingers that cross a circle around the palm's convex hull. Finally, a set of neural-network notebooks covers Keras dense networks and CNNs (MNIST and CIFAR-10), plus a custom image classifier.

**Stack:** Python, OpenCV, NumPy, Matplotlib, scikit-learn, Keras, Jupyter.
