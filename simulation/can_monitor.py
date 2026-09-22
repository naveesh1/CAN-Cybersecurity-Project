import can


bus = can.Bus(
    interface="virtual",
    channel="CAN_Cybersecurity_Bus",
    receive_own_messages=True
)


messages = [
    can.Message(
        arbitration_id=0x100,
        data=[100, 0, 0, 0, 0, 0, 0, 0],
        is_extended_id=False
    ),
    can.Message(
        arbitration_id=0x200,
        data=[0, 80, 0, 0, 0, 0, 0, 0],
        is_extended_id=False
    ),
    can.Message(
        arbitration_id=0x300,
        data=[45, 0, 0, 0, 0, 0, 0, 0],
        is_extended_id=False
    ),
    can.Message(
        arbitration_id=0x400,
        data=[60, 11, 184, 0, 0, 0, 0, 0],
        is_extended_id=False
    )
]


print("===== CAN MONITOR =====")

for message in messages:
    bus.send(message)

    received = bus.recv(timeout=1)

    if received is not None:
        print(
            "Received:",
            "CAN ID:", hex(received.arbitration_id),
            "| Data:", list(received.data),
            "| DLC:", received.dlc
        )


print()
print("===== CAN MONITOR COMPLETE =====")

bus.shutdown()