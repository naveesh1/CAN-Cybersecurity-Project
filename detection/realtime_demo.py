import can
import time
import threading
from collections import Counter

KNOWN_CAN_IDS = {
    0x100: "Engine ECU",
    0x200: "Brake ECU",
    0x300: "Steering ECU",
    0x400: "Instrument Cluster ECU"
}

ATTACK_CAN_ID = 0x555
FREQUENCY_THRESHOLD = 15

message_counter = Counter()
LOG_FILE = "data/realtime_security_alerts.txt"

bus = can.Bus(
    interface="virtual",
    channel="CAN_Cybersecurity_Bus",
    receive_own_messages=True
)


def analyze_message(message):
    can_id = message.arbitration_id

    message_counter[can_id] += 1

    reasons = []

    if can_id not in KNOWN_CAN_IDS:
        reasons.append("Unknown CAN ID")

    if can_id == ATTACK_CAN_ID:
        reasons.append("Known simulated attack ID")

    if message_counter[can_id] > FREQUENCY_THRESHOLD:
        reasons.append("High-frequency CAN traffic")

    if reasons:
        return "ANOMALY", reasons

    return "NORMAL", []


def monitor():
    print("========================================")
    print("REAL-TIME CAN SECURITY MONITOR")
    print("========================================")
    print("Monitoring virtual CAN bus...")
    print()

    with open(LOG_FILE, "w") as log:
        log.write("REAL-TIME CAN SECURITY ALERT LOG\n")
        log.write("=================================\n")

    while True:
        message = bus.recv(timeout=1.0)

        if message is None:
            continue

        status, reasons = analyze_message(message)

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        if status == "ANOMALY":

            alert = (
                f"[{timestamp}] ANOMALY | "
                f"CAN ID: 0x{message.arbitration_id:03X} | "
                f"Data: {list(message.data)} | "
                f"Reason: {', '.join(reasons)}"
            )

            print("🚨 " + alert)

            with open(LOG_FILE, "a") as log:
                log.write(alert + "\n")

        else:

            ecu_name = KNOWN_CAN_IDS.get(
                message.arbitration_id,
                "Unknown ECU"
            )

            print(
                f"[{timestamp}] NORMAL | "
                f"{ecu_name} | "
                f"CAN ID: 0x{message.arbitration_id:03X} | "
                f"Data: {list(message.data)}"
            )


def generate_traffic():

    time.sleep(1)

    print("Sending normal traffic...")
    print()

    for cycle in range(5):

        messages = [
            can.Message(
                arbitration_id=0x100,
                data=[100 + cycle, 0, 0, 0, 0, 0, 0, 0],
                is_extended_id=False
            ),

            can.Message(
                arbitration_id=0x200,
                data=[0, 80 + cycle, 0, 0, 0, 0, 0, 0],
                is_extended_id=False
            ),

            can.Message(
                arbitration_id=0x300,
                data=[45 + cycle, 0, 0, 0, 0, 0, 0, 0],
                is_extended_id=False
            ),

            can.Message(
                arbitration_id=0x400,
                data=[60, 11, 184, 0, 0, 0, 0, 0],
                is_extended_id=False
            )
        ]

        for message in messages:
            bus.send(message)

        time.sleep(0.5)

    print("Normal traffic complete.")
    print()

    print("Sending controlled attack traffic...")
    print()

    for i in range(20):

        attack_message = can.Message(
            arbitration_id=0x555,
            data=[255, 255, 255, 255, 255, 255, 255, 255],
            is_extended_id=False
        )

        bus.send(attack_message)

        time.sleep(0.05)

    print("Attack traffic complete.")
    print()


monitor_thread = threading.Thread(
    target=monitor,
    daemon=True
)

generator_thread = threading.Thread(
    target=generate_traffic,
    daemon=True
)

monitor_thread.start()
generator_thread.start()

generator_thread.join()

time.sleep(2)

bus.shutdown()

print("========================================")
print("REAL-TIME TEST COMPLETE")
print("========================================")
print(f"Security alerts saved to: {LOG_FILE}")