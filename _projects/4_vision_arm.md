---
layout: page
title: Vision-guided robotic arm
description: An ESP32-CAM and OpenCV locate an object, and an ESP32 arm solves inverse kinematics to grab it
img: assets/img/projects/robotic-arm/cv-poster.jpg
importance: 1
category: robotics
---

You click an object in the camera feed. The system finds where it is on the table and sends a robotic arm to pick it up. Three programs talk to each other over Wi-Fi:

| Part           | Role                                            | Runs on                 | Code                                  |
| -------------- | ----------------------------------------------- | ----------------------- | ------------------------------------- |
| **Camera**     | Streams MJPEG video                             | ESP32-CAM               | PlatformIO, C++ (`CameraWebServer`)   |
| **Vision**     | Calibrates, finds the plane, tracks, decides    | Laptop                  | Python + OpenCV (`plane.py`)          |
| **Controller** | Solves inverse kinematics and executes the grab | ESP32-C3 on a 4-DOF arm | PlatformIO, C++ (`POST /grab` server) |

- **Camera**: a PlatformIO port of Espressif's `CameraWebServer`. It streams MJPEG over Wi-Fi and is tuned for steady frame pacing (80 MHz flash, logging compiled out).
- **Vision**: reads the stream, tracks the object by color and converts its pixel position into table coordinates. It is built on the algorithms in my [computer vision toolkit]({% link _projects/12_computer_vision.md %}).
- **Controller**: the arm firmware has three modes: joystick control, inverse-kinematics jogging, and an HTTP server mode that accepts `POST /grab` requests.

<div class="row">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/robotic-arm-tracking.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/robotic-arm-grab.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
</div>
<div class="caption">
    Left: the tracking view, with the three markers defining the plane and the object's polar coordinates being sent to the arm. Right: the arm grabbing the object.
</div>

## The vision pipeline

1. **Camera calibration.** I generated and printed a ChArUco board (a chessboard combined with ArUco markers), captured about 30 frames from the ESP32-CAM, and solved for the camera matrix and distortion coefficients. To check the calibration, I drew 3D axes and the measured distance on each detected tag in the live stream.
2. **A coordinate plane from markers.** Three markers on the table define the plane: two fix the x-axis (their midpoint is the origin) and the third fixes +y. These three known correspondences give an affine transform from pixels to plane coordinates.
3. **Tracking.** Clicking an object locks onto its hue. The program then follows the largest matching blob, with saturation, brightness and minimum-area filters to reject noise. I also integrated **YOLO** object detection with homography-based localization, so objects can be found by class instead of color and mapped straight into the arm's workspace.
4. **Handoff.** The object's position is converted to polar coordinates `(r, θ)`, smoothed with a median over recent readings and latched for a few seconds. It is then sent to the arm as `POST /grab {"r": …, "theta": …}`.

## The arm

The firmware turns the polar target into an `(x, y)` reach at grab height, minus a standoff so the claw stops just short of the object. It solves 2-link inverse kinematics for the shoulder and elbow servos and rotates the base to θ. Then it swings over, closes the claw and lifts to a carry pose. In manual mode, two joysticks drive the servos directly. The joystick input is smoothed with median-filtered ADC readings, a dead zone, speed tiers and dominant-axis locking. You can also record up to 20 poses and play them back.

**Stack:** Python, OpenCV (ArUco/ChArUco, camera calibration, HSV tracking), NumPy, C++/Arduino on ESP32 and ESP32-C3, PlatformIO, ESP32Servo.
