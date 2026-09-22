import can
import time
import random
import csv


bus = can.Bus(
    interface="virtual",
    channel="CAN_Cybersecurity_Bus",
    receive_own_messages=True
)


log_file = "data/combined_traffic.csv"


normal_messages = [
    (0x100, "Engine ECU"),
    (0x200, "Brake ECU"),
    (0x300, "Steering ECU"),
    (0x400, "Instrument Cluster ECU")
]


print("===================================")
print("   NORMAL + ATTACK TRAFFIC")
print("===================================")


with open(log_file, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "can_id",
        "ecu",
        "data",
        "label"
    ])

    message_count = 0
    attack_count = 0

    for cycle in range(10):

        # Normal CAN traffic
        for can_id, ecu_name in normal_messages:

            if can_id == 0x100:
                data = [random.randint(80, 120), 0, 0, 0, 0, 0, 0, 0]

            elif can_id == 0x200:
                data = [0, random.randint(60, 100), 0, 0, 0, 0, 0, 0]

            elif can_id == 0x300:
                data = [random.randint(30, 60), 0, 0, 0, 0, 0, 0, 0]

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

            writer.writerow([
                time.time(),
                hex(can_id),
                ecu_name,
                data,
                "NORMAL"
            ])

            message_count += 1

            print(
                "NORMAL:",
                ecu_name,
                "| ID:", hex(can_id)
            )

            time.sleep(0.05)


        # Simulated CAN flooding attack
        if cycle in [4, 5, 6]:

            for _ in range(10):

                attack_id = 0x555
                attack_data = [255, 255, 255, 255, 255, 255, 255, 255]

                message = can.Message(
                    arbitration_id=attack_id,
                    data=attack_data,
                    is_extended_id=False
                )

                bus.send(message)

                writer.writerow([
                    time.time(),
                    hex(attack_id),
                    "Unknown",
                    attack_data,
                    "ATTACK"
                ])

                attack_count += 1

                print(
                    "ATTACK:",
                    "Unknown ECU",
                    "| ID:", hex(attack_id)
                )

                time.sleep(0.01)


print()
print("===================================")
print("COMBINED TRAFFIC COMPLETE")
print("Normal Messages:", message_count)
print("Attack Messages:", attack_count)
print("Total Messages:", message_count + attack_count)
print("Saved to:", log_file)
print("===================================")


bus.shutdown()