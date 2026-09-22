\# Real-Time Embedded Cybersecurity and Anomalous Message Detection for In-Vehicle CAN Networks



An embedded automotive cybersecurity prototype that combines CAN traffic simulation, real-time anomaly detection, security monitoring, and ESP32-based CAN hardware design.



\---



\## 🚗 Project Overview



Modern vehicles rely heavily on Controller Area Network (CAN) communication between electronic control units (ECUs).



Because traditional CAN communication does not inherently provide strong message authentication, abnormal or unauthorized messages can become a security concern.



This project demonstrates a prototype cybersecurity system that:



\- Simulates multiple vehicle ECUs

\- Generates normal CAN traffic

\- Generates controlled anomalous/attack traffic

\- Detects suspicious CAN messages

\- Performs real-time CAN traffic monitoring

\- Displays security alerts through a dashboard

\- Designs an ESP32 + CAN transceiver hardware interface

\- Produces a PCB design and manufacturing files



> \*\*Current status:\*\* Software prototype and PCB hardware design completed. Physical CAN hardware validation is planned as a future extension.



\---



\## 🎯 Project Objectives



1\. Simulate CAN communication between multiple virtual ECUs.

2\. Generate both normal and controlled anomalous CAN traffic.

3\. Detect suspicious CAN messages using rule-based anomaly detection.

4\. Monitor CAN traffic in real time.

5\. Visualize security status through a dashboard.

6\. Design an ESP32-based CAN hardware interface.

7\. Verify the PCB using DRC and Gerber inspection.



\---



\## 🏗️ System Architecture



```text

&#x20;                SOFTWARE PROTOTYPE



&#x20;    Virtual ECUs

&#x20;         │

&#x20;         ▼

&#x20;   CAN Message Generator

&#x20;         │

&#x20;         ▼

&#x20;    Virtual CAN Bus

&#x20;         │

&#x20;         ▼

&#x20;    CAN Traffic Logger

&#x20;         │

&#x20;         ▼

&#x20;   Anomaly Detection

&#x20;         │

&#x20;         ▼

&#x20;  Real-Time Monitoring

&#x20;         │

&#x20;         ▼

&#x20;  Security Dashboard



Hardware Architecture



&#x20;     ESP32-WROOM-32

&#x20;            │

&#x20;      UART TX / RX

&#x20;            │

&#x20;            ▼

&#x20;      SN65HVD230

&#x20;       CAN Transceiver

&#x20;            │

&#x20;       CANH / CANL

&#x20;            │

&#x20;            ▼

&#x20;        CAN BUS



Overall Concept 



ESP32

&#x20; │

&#x20; ▼

SN65HVD230

&#x20; │

&#x20; ▼

CAN Bus

&#x20; │

&#x20; ▼

CAN Traffic

&#x20; │

&#x20; ▼

Monitoring

&#x20; │

&#x20; ▼

Anomaly Detection

&#x20; │

&#x20; ▼

Security Alert

&#x20; │

&#x20; ▼

Dashboard 



💻 Software Features

Virtual ECU Simulation



The prototype contains four virtual ECUs:



ECU	CAN ID

Engine ECU	0x100

Brake ECU	0x200

Steering ECU	0x300

Instrument Cluster ECU	0x400

Controlled Attack Traffic



The prototype generates controlled anomalous traffic using:



CAN ID: 0x555

Data: FF FF FF FF FF FF FF FF



This traffic is used only for controlled testing of the detection pipeline.



Anomaly Detection



The detector currently identifies:



Unknown CAN IDs

Known simulated attack ID 0x555

High-frequency CAN traffic

Real-Time Monitoring



The system continuously monitors incoming CAN messages and generates security alerts when anomalous traffic is detected.



Security Dashboard



The Streamlit dashboard displays:



Total CAN messages

Normal messages

Anomalous messages

Anomaly rate

Security status

Traffic/anomaly visualization

📊 Controlled Prototype Results



The current controlled test dataset contains:



Metric	Result

Total Messages	70

Normal Messages	40

Anomalous Messages	30

True Positives	30

True Negatives	40

False Positives	0

False Negatives	0

Accuracy	100%

Precision	100%

Recall	100%

F1 Score	100%



Important: These performance values are from a controlled simulated dataset and should not be interpreted as real-world automotive CAN intrusion-detection performance.



🔧 Hardware Design



The hardware prototype was designed using KiCad.



Main Components

Component	Purpose

ESP32-WROOM-32	Main embedded controller

SN65HVD230	CAN transceiver

AMS1117-3.3	3.3V regulation

120Ω resistor	CAN termination

BOOT switch	ESP32 boot control

RESET switch	ESP32 reset control

Capacitors	Power decoupling

CAN connector	CANH / CANL interface

Power connector	External power input

ESP32 ↔ CAN Transceiver

ESP32 TXD0 / GPIO1

&#x20;       │

&#x20;       ▼

SN65HVD230 TXD



ESP32 RXD0 / GPIO3

&#x20;       ▲

&#x20;       │

SN65HVD230 RXD

CAN Interface

SN65HVD230 CANH ───── CANH

SN65HVD230 CANL ───── CANL

GND ────────────────── GND

🧩 PCB Design



The PCB was designed and routed in KiCad.



The design includes:



ESP32 module

CAN transceiver

Power regulation

CAN termination

BOOT and RESET controls

CAN connector

Power connector

Routed PCB traces

PCB Verification



The final PCB was verified using:



KiCad DRC

Gerber generation

Gerber visual inspection

KiCad 3D Viewer



Final DRC result:



Violations: 0

Unconnected Items: 0

Errors: 0

Warnings: 0

📸 Project Screenshots

Security Dashboard



Anomaly Detection



Real-Time Monitoring



CAN Schematic



PCB Layout



PCB 3D View



DRC Verification



Gerber Verification



🎥 PCB Design Demo



A short demonstration of the completed PCB layout and 3D design is available in:



videos/phase1-pcb-design-demo.mp4

🧪 Testing



The prototype was tested using two primary scenarios.



Normal Traffic

Messages: 20

Normal: 20

Anomalies: 0

Combined Traffic

Total: 70

Normal: 40

Anomalies: 30



The same detection pipeline was also tested through real-time monitoring and the security dashboard.



📁 Project Structure



CAN-Cybersecurity-Project/

│

├── dashboard/

│   └── security\_dashboard.py

│

├── detection/

│   ├── anomaly\_detector.py

│   ├── performance\_analyzer.py

│   └── realtime\_demo.py

│

├── simulation/

│   ├── engine\_ecu.py

│   ├── brake\_ecu.py

│   ├── steering\_ecu.py

│   ├── instrument\_cluster\_ecu.py

│   ├── can\_message\_generator.py

│   ├── generate\_ecu\_messages.py

│   ├── virtual\_can\_bus.py

│   ├── send\_can\_messages.py

│   ├── can\_monitor.py

│   ├── can\_network.py

│   ├── can\_logger.py

│   ├── normal\_traffic.py

│   ├── can\_attack.py

│   └── combined\_traffic.py

│

├── tests/

│   └── scenario\_test.py

│

├── data/

│   ├── can\_traffic.csv

│   └── normal\_traffic.txt

│

├── docs/

│   ├── HARDWARE\_DESIGN.md

│   └── INTEGRATION\_PLAN.md

│

├── screenshots/

│   ├── 01-security-dashboard.png

│   ├── 02-anomaly-detection.png

│   ├── 03-realtime-monitoring.png

│   ├── 04-can-schematic.png

│   ├── 05-pcb-layout.png

│   ├── 06-pcb-3d-view.png

│   ├── 07-drc-verification.png

│   └── 08-gerber-verification.png

│

├── videos/

│   └── phase1-pcb-design-demo.mp4

│

├── CAN-Cybersecurity-Hardware/

│   ├── CAN-Cybersecurity-Hardware.kicad\_sch

│   ├── CAN-Cybersecurity-Hardware.kicad\_pcb

│   ├── CAN-Cybersecurity-Hardware.kicad\_pro

│   └── Gerber / Drill files

│

└── README.md



⚠️ Current Limitations



This is currently a prototype and design-stage system.



The present implementation uses a simulated CAN environment for software testing.



Physical CAN hardware validation has not yet been completed because a physical USB-CAN interface is not currently available.



Therefore, the current results do not represent validated real-world automotive intrusion-detection performance.



🚀 Future Work



Planned future extensions include:



Physical ESP32 + SN65HVD230 integration

USB-CAN interface integration

Real CAN bus traffic capture

Hardware-in-the-loop testing

Expanded anomaly-detection techniques

CAN message frequency profiling

More realistic automotive attack scenarios

Extended security analytics



🛠️ Technologies Used



1.Python

2.python-can

3.Streamlit

4.ESP32

5.SN65HVD230

6.KiCad

7.CAN

8.UART

9.PCB Design

10.Gerber / Excellon

11.Rule-Based Anomaly Detection

