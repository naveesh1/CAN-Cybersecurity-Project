\# Hardware Design



\## Project

Real-Time Embedded Cybersecurity and Anomalous Message Detection for In-Vehicle CAN Networks



\## Hardware Architecture



The hardware prototype provides a CAN communication interface for the embedded cybersecurity system.



\### Main Components



| Reference | Component | Purpose |

|---|---|---|

| U1 | AMS1117-3.3 | 5V to 3.3V voltage regulation |

| U2 | ESP32-WROOM-32 | Main embedded controller |

| U3 | SN65HVD230 | CAN transceiver |

| R1 | 120R | CAN bus termination |

| R2 | 10kΩ | ESP32 EN pull-up |

| R3 | 10kΩ | ESP32 GPIO0 pull-up |

| C1 | 100nF | 3.3V supply decoupling |

| C2 | 10uF | 3.3V supply filtering |

| SW1 | BOOT | ESP32 boot control |

| SW2 | RESET | ESP32 reset control |

| J1 | POWER\_IN | 5V power input |

| J2 | CAN\_BUS | CANH, CANL and GND interface |



\## Power Connections



\- J1 Pin 1 → +5V

\- J1 Pin 2 → GND

\- +5V → U1 VI

\- U1 VO → +3V3

\- U1 GND → GND

\- C1 → +3V3 and GND

\- C2 → +3V3 and GND



\## ESP32 and CAN Transceiver



\- U2 Pin 35 (TXD0/IO1) → U3 Pin 1 (D/TXD)

\- U2 Pin 34 (RXD0/IO3) → U3 Pin 4 (R/RXD)

\- U3 Pin 3 (VCC) → +3V3

\- U3 Pin 2 (GND) → GND

\- U3 Pin 8 (RS) → GND

\- U3 Pin 5 (Vref) → No Connection



\## CAN Bus



\- U3 Pin 7 (CANH) → J2 Pin 1 (CANH)

\- U3 Pin 6 (CANL) → J2 Pin 2 (CANL)

\- J2 Pin 3 → GND

\- R1 120R → between CANH and CANL



\## ESP32 Boot and Reset



\### RESET



\- R2 → +3V3 and U2 Pin 3 (EN)

\- SW2 → U2 Pin 3 (EN) and GND



\### BOOT



\- R3 → +3V3 and U2 Pin 25 (GPIO0)

\- SW1 → U2 Pin 25 (GPIO0) and GND



\## PCB Verification



\- Design Rules Checker: 0 Errors

\- Warnings: 0

\- Unconnected Items: 0

\- Violations: 0

\- Gerber files generated

\- Drill files generated

\- Gerber layers visually verified

