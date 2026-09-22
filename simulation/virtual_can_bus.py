import can


bus = can.Bus(
    interface="virtual",
    channel="CAN_Cybersecurity_Bus",
    receive_own_messages=True
)


print("===== VIRTUAL CAN BUS =====")
print("Bus created successfully")
print("Channel: CAN_Cybersecurity_Bus")
print("Interface: virtual")


bus.shutdown()