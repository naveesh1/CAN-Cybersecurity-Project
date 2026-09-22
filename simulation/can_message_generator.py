import can


def create_can_message(can_id, data):
    message = can.Message(
        arbitration_id=can_id,
        data=data,
        is_extended_id=False
    )

    return message


message = create_can_message(
    0x100,
    [100, 0, 0, 0, 0, 0, 0, 0]
)


print("===== CAN MESSAGE =====")
print("CAN ID:", hex(message.arbitration_id))
print("Data:", list(message.data))
print("DLC:", message.dlc)