import can
import csv
import time


bus = can.Bus(
    interface="virtual",
    channel="CAN_Cybersecurity_Bus",
    receive_own_messages=True
)


log_file = "../data/can_traffic.csv"


print("===== CAN TRAFFIC LOGGER =====")


with open(log_file, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "can_id",
        "dlc",
        "data"
    ])

    for cycle in range(5):

        messages = [
            (0x100, [100, 0, 0, 0, 0, 0, 0, 0]),
            (0x200, [0, 80, 0, 0, 0, 0, 0, 0]),
            (0x300, [45, 0, 0, 0, 0, 0, 0, 0]),
            (0x400, [60, 11, 184, 0, 0, 0, 0, 0])
        ]

        for can_id, data in messages:

            message = can.Message(
                arbitration_id=can_id,
                data=data,
                is_extended_id=False
            )

            bus.send(message)

            received = bus.recv(timeout=1)

            if received is not None:

                timestamp = time.time()

                writer.writerow([
                    timestamp,
                    hex(received.arbitration_id),
                    received.dlc,
                    list(received.data)
                ])

                print(
                    "Logged:",
                    hex(received.arbitration_id),
                    list(received.data)
                )

        time.sleep(0.5)


bus.shutdown()

print()
print("===== LOGGING COMPLETE =====")
print("Saved to:", log_file)