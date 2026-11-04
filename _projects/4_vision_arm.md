---
layout: page
title: Vision-guided robotic arm
description: An ESP32-CAM and OpenCV locate an object, and an ESP32-C3 arm solves inverse kinematics to grab it
img: assets/img/projects/robotic-arm/cv-poster.jpg
img_alt: "Live ESP32-CAM view of the robotic arm on a table, with the three plane markers and the tracked object highlighted, next to the vision script's log of polar coordinates"
importance: 1
category: robotics
---

You click an object in the camera feed. The system finds where it is on the table and sends a robotic arm to pick it up. Three programs talk to each other over Wi-Fi:

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img src="{{ '/assets/img/projects/robotic-arm/block-diagram.svg' | relative_url }}" alt="Block diagram: the ESP32-CAM streams video over HTTP to a laptop running plane.py with OpenCV, which sends POST /grab with r and theta to the ESP32-C3 arm controller driving four servos" class="img-fluid rounded z-depth-1" loading="lazy" />
    </div>
</div>

| Part           | Role                                            | Runs on            | Code                                  |
| -------------- | ----------------------------------------------- | ------------------ | ------------------------------------- |
| **Camera**     | Streams MJPEG video                             | ESP32-CAM          | PlatformIO, C++ (`CameraWebServer`)   |
| **Vision**     | Calibrates, finds the plane, tracks, decides    | Laptop             | Python + OpenCV (`plane.py`)          |
| **Controller** | Solves inverse kinematics and executes the grab | ESP32-C3, 4 servos | PlatformIO, C++ (`POST /grab` server) |

- **Camera**: a PlatformIO port of Espressif's `CameraWebServer`. It streams MJPEG over Wi-Fi and is tuned for steady frame pacing (80 MHz flash, logging compiled out).
- **Vision**: reads the stream, tracks the object by color and converts its pixel position into table coordinates. It is built on the algorithms in my [computer vision toolkit]({% link _projects/12_computer_vision.md %}).
- **Controller**: the arm firmware has three modes: joystick control, inverse-kinematics jogging, and an HTTP server mode that accepts `POST /grab` requests.

<div class="row">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/robotic-arm-tracking.mp4" class="img-fluid rounded z-depth-1" controls=true %}
        <div class="caption">
            The tracking view: three markers define the table plane, and the object's polar coordinates are sent to the arm.
        </div>
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/robotic-arm-grab.mp4" class="img-fluid rounded z-depth-1" controls=true %}
        <div class="caption">
            The arm grabbing the object.
        </div>
    </div>
</div>

## The vision pipeline

1. **Camera calibration.** I generated and printed a ChArUco board (a chessboard combined with ArUco markers), captured about 30 frames from the ESP32-CAM, and solved for the camera matrix and distortion coefficients. To check the calibration, I drew 3D axes and the measured distance on each detected tag in the live stream.
2. **A coordinate plane from markers.** Three ArUco markers on the table define the plane: two fix the x-axis (their midpoint is the origin) and the third fixes +y. These three known correspondences give an affine transform from pixels to plane coordinates.
3. **Tracking.** Clicking an object locks onto its hue. The program then follows the largest matching blob, with saturation, brightness and minimum-area filters to reject noise.
4. **Handoff.** The object's position is converted to polar coordinates `(r, θ)`, smoothed with a median over recent readings and latched for a few seconds. It is then sent to the arm as `POST /grab {"r": …, "theta": …}`.

## The arm

The firmware turns the polar target into an `(x, y)` reach at grab height, minus a standoff so the claw stops just short of the object. The arm has three joints plus a claw, four servos in all, and the inverse kinematics is decoupled: the base servo rotates to θ, which reduces the problem to a 2-link planar solve for the shoulder and elbow. Then it swings over, closes the claw and lifts to a carry pose. In manual mode, two joysticks drive the servos directly. The joystick input is smoothed with median-filtered ADC readings, a dead zone, speed tiers and dominant-axis locking. You can also record up to 20 poses and play them back.

**Stack:** Python, OpenCV (ArUco/ChArUco, camera calibration, HSV tracking), NumPy, C++/Arduino on ESP32 and ESP32-C3, PlatformIO, ESP32Servo.
