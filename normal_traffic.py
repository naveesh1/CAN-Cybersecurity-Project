import can
import time
import random


bus = can.Bus(
    interface="virtual",
    channel="CAN_Cybersecurity_Bus",
    receive_own_messages=True
)


messages = [
    (0x100, "Engine ECU"),
    (0x200, "Brake ECU"),
    (0x300, "Steering ECU"),
    (0x400, "Instrument Cluster ECU")
]


print("===================================")
print("      NORMAL CAN TRAFFIC")
print("===================================")


message_count = 0

for cycle in range(10):

    for can_id, ecu_name in messages:

        if can_id == 0x100:
            data = [
                random.randint(80, 120),
                0, 0, 0, 0, 0, 0, 0
            ]

        elif can_id == 0x200:
            data = [
                0,
                random.randint(60, 100),
                0, 0, 0, 0, 0, 0
            ]

        elif can_id == 0x300:
            data = [
                random.randint(30, 60),
                0, 0, 0, 0, 0, 0, 0
            ]

        else:
            speed = random.randint(40, 100)
            rpm = random.randint(2000, 4000)

            data = [
                speed,
                (rpm >> 8) & 0xFF,
                rpm & 0xFF,
                0, 0, 0, 0, 0
            ]

        message = can.Message(
            arbitration_id=can_id,
            data=data,
            is_extended_id=False
        )

        bus.send(message)

        message_count += 1

        print(
            "Sent:",
            ecu_name,
            "| ID:", hex(can_id),
            "| Data:", data
        )

        time.sleep(0.1)


print()
print("===================================")
print("NORMAL TRAFFIC COMPLETE")
print("Total Messages:", message_count)
print("===================================")


bus.shutdown()