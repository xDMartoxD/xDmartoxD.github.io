---
layout: page
title: Robotsito
description: A 3D-printed robotic arm on an Arduino Uno, with joystick control and inverse kinematics
img: assets/img/projects/robotsito/ik-poster.jpg
importance: 2
category: robotics
---

Code: [github.com/xDMartoxD/robotsito](https://github.com/xDMartoxD/robotsito)

Robotsito is a four-servo robotic arm (hip, elbow, wrist and clamp) driven by an Arduino Uno. I 3D-printed it from the open-source [EEZYbotARM MK2](https://www.thingiverse.com/thing:1454048) design and wrote the control firmware myself. It was the starting point for the [vision-guided arm]({% link _projects/4_vision_arm.md %}).

<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/robotsito-ik.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
</div>
<div class="caption">
    Robotsito moving under inverse-kinematics control.
</div>

## What's inside

- **Joystick control**: an analog joystick drives the elbow and wrist. Larger deflection moves the servos faster, and a dead zone filters out drift. Two buttons rotate the hip in 10° steps, and the joystick button toggles the clamp.
- **Reference frames**: each servo has its own mounting offset and direction. Conversion functions map servo degrees to a shared reference frame, so the rest of the code can reason about real joint angles.
- **Safe wrist limits**: the wrist's allowed range depends on the elbow angle, which stops the arm from colliding with itself.
- **Inverse kinematics**: forward kinematics is built from 3×3 homogeneous transforms for the two planar links. Solving it in reverse gives the joint angles that reach a target `(x, y)` point, and unreachable targets are rejected.

**Stack:** C++/Arduino, PlatformIO, Servo library, Arduino Uno.
