---
layout: page
title: Useless machine
description: A six-switch "useless machine" with a belt-driven carriage and an inverse-kinematics servo arm, designed in SolidWorks
img: assets/img/projects/useless-machine/exploded.jpg
img_alt: "Exploded SolidWorks view of the useless machine: lid plate with six switches, servos and arm links, stepper motor, belt and linear rail with its carriage"
importance: 3
category: robotics
---

Code and CAD: [github.com/xDMartoxD/useless-machine](https://github.com/xDMartoxD/useless-machine)

A useless machine has one job: when you flip its switch, it reaches out and flips the switch back off. This version has **six** switches on the lid:

- A **push-rod servo** opens the lid.
- A **NEMA 17 stepper** drives a carriage along an **MGN12H linear rail** with a GT2 belt, so it can reach whichever switch was flipped.
- A **two-link servo arm** on the carriage, built like [Robotsito]({% link _projects/5_robotsito.md %}), reaches up and flips the switch back.

I designed the complete mechanism in **SolidWorks**: the box, hinged lid, switch plate, push-rod lid mechanism, belt pulleys and clamps, motor and servo mounts, the carriage and the arm linkages. Off-the-shelf parts (NEMA 17, MG90S servos, MGN12H rail, bearings) were placed from supplier CAD models.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/useless-machine-explode.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/useless-machine-collapse.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
    </div>
</div>
<div class="caption">
    Exploded view of the assembly, and the parts collapsing back into the box.
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/useless-machine-pulley.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
        <div class="caption">Motion study of the drive assembly.</div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/useless-machine-motion.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
        <div class="caption">Motion study of the box mechanism.</div>
    </div>
</div>

## Firmware

The firmware runs on an Arduino Uno and is built with PlatformIO.

- **State machine**: idle → open lid → move → press → close lid. The carriage starts driving while the lid is still opening, and AccelStepper keeps the motion non-blocking so the switches are read the whole time. With several switches ON, it handles the nearest one next. If you flip a switch while the lid is closing, it opens straight back up.
- **Carriage**: a 20-tooth GT2 pulley gives 40 mm per revolution, which is 80 steps/mm at 16 microsteps. The carriage homes against an endstop at boot, and the stepper is released when idle so it stays cool.
- **Arm**: closed-form two-link inverse kinematics (elbow-up) turns a finger-tip target into shoulder and elbow angles. As in Robotsito, each servo has a mounting offset and direction that map servo degrees to real joint angles. Moves are interpolated along a straight line with IK solved at every step, and any pose outside the reachable workspace or the joint limits is refused.
- **Robustness**: switches are debounced in software, and a stuck switch is retried three times and then skipped, so the box never gets stuck in a loop. All dimensions live in one `config.h` for calibration.

**Tools:** SolidWorks (part modeling, assemblies, exploded views, motion studies), C++/Arduino, PlatformIO, AccelStepper, Servo.
