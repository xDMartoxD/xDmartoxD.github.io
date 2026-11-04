---
layout: page
title: IoT poultry farm monitoring
description: Sensor network, edge gateway and cloud dashboard for a small chicken farm in Quetame, Colombia
img: assets/img/projects/iot-chicken-farm/architecture.png
importance: 4
category: academic
---

_Team project for ISIS4223 Internet of Everything, a master's-level course at Universidad de los Andes (2023)._
Code and reports: [github.com/xDMartoxD/iot-chicken-farm](https://github.com/xDMartoxD/iot-chicken-farm)

Small poultry farms in Quetame, Cundinamarca, operate with little real-time visibility. One of the biggest causes of losses is chickens piling on top of each other when they are cold or stressed, which can suffocate them. Poor control of water quality, feed and egg collection adds to the losses. Our team designed an IoT system to monitor the farm and react automatically, then built a working prototype of its sensing layer.

## Design

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/iot-chicken-farm/architecture.png" title="System architecture" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Device-layer architecture. Sensor nodes talk Zigbee to an NVIDIA Jetson Nano gateway, which sends data to the cloud over LTE-M and MQTT and drives the actuators.
</div>

We turned each farm problem into a measurement and a response:

| Problem                      | Sensing                                      | Response                             |
| ---------------------------- | -------------------------------------------- | ------------------------------------ |
| Chickens piling up from cold | DS18B20 temperature, MLX90640 thermal camera | Close curtains, turn on the heater   |
| Chickens piling up from fear | Thermal and infrared (Pi NoIR) cameras       | SMS alert to the barn manager        |
| Water pH affecting the flock | SEN0169 pH probe                             | Acid/base doser with a stepper valve |
| Untracked feed consumption   | Accelerometer on the feed dispenser          | Logging only                         |
| Eggs miscounted or broken    | Weight, RGB camera, infrared                 | Stop signal to the collector         |

For the network, sensor nodes form a low-power **Zigbee** mesh using **6LoWPAN** encapsulation and **RPL** routing. Image processing runs at the edge (Raspberry Pi Zero 2 W and the Jetson Nano) so raw video never leaves the farm. Only events and readings go up over **LTE-M** and **MQTT**. The design also covers stakeholder analysis and quality requirements (availability, fault tolerance, energy efficiency) for the farm's conditions of 10–30 °C and 89% humidity.

## Prototype

- **Temperature node**: an ESP32 reads a DHT sensor and switches heating or cooling outputs (LEDs in the prototype) to hold the barn at 30–35 °C.
- **pH node**: a second ESP32 with acid and base outputs to keep the water at pH 6–8.
- **Gateway**: a Python service polls both nodes over Bluetooth Classic (RFCOMM), parses their readings, and posts timestamped values to an **Ubidots** dashboard.
- **MQTT**: an ESP8266 publish/subscribe client was used to test the cloud link.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://www.youtube.com/embed/sft1YtgVUfk" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://www.youtube.com/embed/ZKdEqnlpLtI" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Project demos, parts 1 and 2.
</div>

**Stack:** ESP32, ESP8266, Arduino C++, Python (PyBluez), Ubidots, MQTT. The design also specifies Zigbee, 6LoWPAN, RPL, LTE-M and an NVIDIA Jetson Nano.
