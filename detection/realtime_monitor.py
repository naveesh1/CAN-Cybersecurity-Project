import can
import time
from collections import Counter

# Legitimate CAN IDs used by our virtual ECUs
KNOWN_CAN_IDS = {
    0x100: "Engine ECU",
    0x200: "Brake ECU",
    0x300: "Steering ECU",
    0x400: "Instrument Cluster ECU"
}

# Controlled simulated attack ID
ATTACK_CAN_ID = 0x555

# Frequency threshold
FREQUENCY_THRESHOLD = 15

# Message counter
message_counter = Counter()

# Virtual CAN bus
bus = can.Bus(
    interface="virtual",
    channel="CAN_Cybersecurity_Bus",
    receive_own_messages=True
)

print("========================================")
print("REAL-TIME CAN SECURITY MONITOR")
print("========================================")
print("Monitoring virtual CAN bus...")
print("Press CTRL+C to stop.")
print()


def analyze_message(message):

    can_id = message.arbitration_id

    message_counter[can_id] += 1

    reasons = []

    # Rule 1: Unknown CAN ID
    if can_id not in KNOWN_CAN_IDS:
        reasons.append("Unknown CAN ID")

    # Rule 2: Known simulated attack ID
    if can_id == ATTACK_CAN_ID:
        reasons.append("Known simulated attack ID")

    # Rule 3: High-frequency traffic
    if message_counter[can_id] > FREQUENCY_THRESHOLD:
        reasons.append("High-frequency CAN traffic")

    if reasons:
        status = "ANOMALY"
    else:
        status = "NORMAL"

    return status, reasons


try:

    while True:

        message = bus.recv(timeout=1.0)

        if message is None:
            continue

        status, reasons = analyze_message(message)

        timestamp = time.strftime("%H:%M:%S")

        if status == "ANOMALY":

            print(
                f"[{timestamp}] 🚨 ANOMALY | "
                f"CAN ID: 0x{message.arbitration_id:03X} | "
                f"Data: {list(message.data)} | "
                f"Reason: {', '.join(reasons)}"
            )

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

    bus.shutdown()