---
layout: page
title: Data visualization dashboards
description: Speed cameras vs. traffic accidents in Bogotá (Power BI), and a century of the US movie market (Vega-Lite)
img: assets/img/projects/dataviz/accidents.jpg
img_alt: "Dashboard of Bogotá traffic accidents: a heat map of the city, accidents over time, accidents by road, and the cameras with the most accidents"
importance: 2
category: academic
---

Two visual-analytics projects from the Visual Analytics course at Universidad de los Andes.

## Do speed cameras reduce accidents in Bogotá?

I combined Bogotá's open data on traffic accidents with the locations of the city's "Cámaras Salvavidas" (speed enforcement cameras). A pandas pipeline computed the haversine distance from every accident to every camera, which let me filter accidents by how close they happened to a camera. The Power BI dashboard can then compare crash counts before and after each camera was installed.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/dataviz/accidents.jpg" title="Bogotá accidents dashboard" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    The dashboard can be filtered by camera, date range, distance to the camera, severity and accident type. It shows an accident heatmap, before/after gauges, a timeline, and the worst road corridors and cameras.
</div>

## The US movie market over 100 years

This is an [Observable notebook](https://observablehq.com/d/f1d2e4aee93571eb) built with Vega-Lite. It explores releases per month and year, sales by genre, and how critics and audiences compare. The chart below plots IMDb rating against Rotten Tomatoes rating, with each point sized by worldwide gross.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/dataviz/movies.jpg" title="Movies dashboard" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>

**Stack:** Python (pandas, Jupyter), Power BI, Vega-Lite, Observable, D3.
