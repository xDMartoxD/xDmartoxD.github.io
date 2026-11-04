---
layout: page
title: Interactive solar system
description: A to-scale 3D model of the solar system in three.js, with real textures and orbital periods
img: assets/img/projects/solar-system/sun.jpg
img_alt: "Rendered Sun against a starfield, with the simulation's speed and rotation controls in the corner"
importance: 3
category: academic
---

This interactive 3D model of the solar system was my final project for _Mundos Lejanos_, an astronomy course at Universidad de los Andes (2023). It's built with three.js and TypeScript. The course report pairs each body's science (size, composition, atmosphere, orbit) with the steps used to recreate it in WebGL.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/solar-system/sun.jpg" title="The Sun in the simulation" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    The Sun, rendered with an emissive 8K texture against a Milky Way skybox. The dat.gui panel in the corner controls the simulation.
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://www.youtube.com/embed/58KWOWkuCxU" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://www.youtube.com/embed/VN88t_O2RlQ" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://www.youtube.com/embed/ffe68p-uEDI" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Walkthroughs of the simulation (parts 1–3).
</div>

## How it works

- **Real proportions**: planet diameters and orbital distances come from real values relative to Earth and to the astronomical unit, all scaled by a single divider.
- **Real motion**: each planet orbits the Sun at a rate based on its actual orbital period, and spins on its axis based on its rotation period. The Moon orbits Earth, and Earth has a separate, slowly rotating cloud layer.
- **Textures**: 8K maps for the Sun, the planets and the star field, a bump map for Earth's terrain, and an alpha-mapped ring for Saturn. The Sun is the scene's single point light, so each planet has a proper day side and night side.
- **Controls**: a dat.gui panel controls time speed, toggles orbital motion and compresses distances, since at true scale the planets are tiny specks. Number keys `1` to `9` re-target the camera on each planet, and OrbitControls with damping handle navigation.

**Stack:** TypeScript, three.js, dat.gui, Vite.
