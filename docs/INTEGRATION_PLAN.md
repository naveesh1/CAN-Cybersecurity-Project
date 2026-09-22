\# Software + Hardware Integration Plan



\## 1. Project Integration



The project combines a software-based CAN cybersecurity monitoring system with a hardware CAN communication interface.



The software simulates, monitors, logs, and analyzes CAN traffic, while the hardware provides the physical interface for CAN communication.



\## 2. Software Architecture



The software system consists of:



\- Virtual ECU message generation

\- CAN traffic simulation

\- CAN traffic logging

\- Anomaly detection

\- Real-time CAN monitoring

\- Security alerts

\- Performance analysis

\- Streamlit security dashboard



\## 3. Hardware Architecture



The hardware consists of:



\- ESP32-WROOM-32

\- SN65HVD230 CAN Transceiver

\- AMS1117-3.3 Voltage Regulator

\- CAN termination resistor

\- CAN bus connector

\- Boot and Reset switches

\- Power input and decoupling capacitors



\## 4. Software-to-Hardware Communication



The ESP32 communicates with the SN65HVD230 through UART.



ESP32 TXD0 → SN65HVD230 TXD  

ESP32 RXD0 → SN65HVD230 RXD



The SN65HVD230 converts the ESP32 logic-level signals into differential CANH and CANL signals.



\## 5. CAN Bus Communication



The physical CAN interface uses:



\- CANH

\- CANL

\- GND



The CAN bus uses a 120R termination resistor between CANH and CANL.



\## 6. Planned Integration Flow



```text

ESP32

&#x20; ↓

SN65HVD230

&#x20; ↓

CANH / CANL

&#x20; ↓

CAN Traffic

&#x20; ↓

Software CAN Monitoring

&#x20; ↓

Anomaly Detection

&#x20; ↓

Security Alert

&#x20; ↓

Dashboard

7. Anomaly Detection Integration

The software analyzes CAN messages and identifies abnormal traffic using:

Unknown CAN IDs
Known simulated attack ID 0x555
High-frequency CAN traffic

Detected anomalies are reported as security alerts.

8. Testing Strategy

Integration testing will verify:

ESP32 CAN communication
CAN message transmission
CAN message reception
Normal CAN traffic monitoring
Abnormal CAN traffic detection
Real-time security alerts
Dashboard visualization
9. Current Prototype Status

The software prototype has been tested using controlled simulated CAN traffic.

The hardware schematic and PCB design have been completed and verified using KiCad.

Hardware-software integration is planned as the next stage of the prototype.

10. Important Limitation

The current anomaly-detection performance results are based on a controlled simulated dataset.

The measured 100% accuracy, precision, recall, and F1-score should not be interpreted as real-world vehicle CAN cybersecurity performance.


