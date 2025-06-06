# 🔐 Smart Intruder and Weapon Detection System
![Intruder Alert](images/intruder.png)


A real-time security system that detects unauthorized individuals and identifies weapons using computer vision, with instant alerts via mobile.

> ⚠️ Built using Python, OpenCV, Haar Cascade, LBPH, YOLOv8, Raspberry Pi, Arduino, and Blynk.

---

## 📸 Project Overview

This system enhances physical security by integrating:
- **PIR motion detection**
- **Face recognition** (known vs unknown)
- **Weapon detection** using YOLOv8 object detection
- **Real-time alerts** via Blynk to a mobile phone

It captures video input, detects motion, identifies the person and the presence of any weapon, and sends an immediate alert if a threat is detected.

---

## 🚀 Features

- 👁️ Motion detection via PIR sensor
- 🧠 Face detection + recognition (LBPH with Haar Cascade)
- 🔫 YOLOv8-based weapon detection
- 📱 Instant alerts using Blynk app
- 🎛️ GUI with Tkinter for easy use
- 💬 Serial communication with Arduino

---

## 🛠 Tech Stack

| Technology | Use |
|------------|-----|
| Python 3 | Core scripting |
| OpenCV | Image/video processing |
| Haar Cascade | Face detection |
| LBPH | Face recognition |
| YOLOv8 | Weapon detection |
| Raspberry Pi | Main processor |
| Arduino | Hardware interfacing |
| Blynk | Real-time alerting |
| Tkinter | GUI application |

---

## 🧪 Installation

1. Clone the repository
   ```bash
   git clone https://github.com/shreyasanjeev/smart-intruder-weapon-detection.git
   cd smart-intruder-weapon-detection
