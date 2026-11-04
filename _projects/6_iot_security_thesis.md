---
layout: page
title: IoT security in smart agriculture
description: Undergraduate thesis analyzing attacks on, and defenses for, an agricultural IoT monitoring system
importance: 1
category: academic
---

_Undergraduate thesis, B.Sc. Systems and Computing Engineering, Universidad de los Andes, October 2024._
_Original title: "Análisis de Seguridad en Sistemas Agrícolas Inteligentes: Caso Práctico de Evaluación y Mejora en un Sistema IoT de Monitoreo"._

Farms are adopting IoT for irrigation, crop monitoring, product traceability and machinery management. Every connected sensor and gateway also widens the attack surface. This thesis asks what can go wrong in a typical agricultural IoT deployment, and how to defend it without hurting the system's performance.

## Case study

The analysis centers on a temperature-control system with a three-layer architecture:

1. **Sensors and actuators**: smart temperature sensors with local filtering and storage that report over Bluetooth Low Energy, plus a digitally controlled heater.
2. **Communication gateway**: collects sensor data over Bluetooth 5.0, aggregates it, and bridges it to MQTT, encrypted with AES-256 and with QoS for critical messages. It buffers data when the server is unreachable.
3. **Application server**: an MQTT broker, a time-series database, PID control with hysteresis for the heater, a web dashboard, a REST API, and alerting.

## Threat analysis

Using the **MITRE ATT&CK for ICS** matrix, I mapped adversary techniques to each component and grouped them by the property they break:

- **Integrity**: scripting on the gateway, modified PLC parameters, spoofed reporting messages, unauthorized command messages, and malicious firmware updates.
- **Confidentiality**: network sniffing and remote system discovery against the application server.
- **Non-repudiation**: modified alarm settings, connection proxies, and abuse of valid accounts.

## Proposed defenses

For each technique, the thesis proposes preventions and mitigations:

- Multi-factor authentication and role-based access control (OAuth 2.0 / OpenID Connect).
- Network segmentation.
- End-to-end encryption of device communications.
- Signed firmware updates.
- Continuous monitoring and auditing.

The goal is to balance security against the latency and power limits of field devices. The thesis concludes that IoT brings real efficiency gains to agribusiness, but only if security is designed in from the perception layer up.
