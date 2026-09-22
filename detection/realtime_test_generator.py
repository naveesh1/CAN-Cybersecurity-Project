import can
import time

bus = can.Bus(
    interface="virtual",
    channel="CAN_Cybersecurity_Bus",
    receive_own_messages=True
)

print("========================================")
print("REAL-TIME CAN TEST GENERATOR")
print("========================================")

print("Sending normal traffic...")

# Send normal CAN messages
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

# Send controlled flooding traffic
for i in range(20):

    attack_message = can.Message(
        arbitration_id=0x555,
        data=[255, 255, 255, 255, 255, 255, 255, 255],
        is_extended_id=False
    )

    bus.send(attack_message)

    time.sleep(0.05)

print("Attack traffic complete.")

bus.shutdown()

print()
print("TEST COMPLETE")