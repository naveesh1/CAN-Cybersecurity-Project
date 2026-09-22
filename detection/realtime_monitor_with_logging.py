import can
import time
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

print("========================================")
print("REAL-TIME CAN SECURITY MONITOR")
print("WITH SECURITY ALERT LOGGING")
print("========================================")
print("Monitoring virtual CAN bus...")
print("Press CTRL+C to stop.")
print()


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


try:

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

except KeyboardInterrupt:

    print()
    print("========================================")
    print("REAL-TIME MONITOR STOPPED")
    print("========================================")
    print(f"Security alerts saved to: {LOG_FILE}")

    bus.shutdown()