class BrakeECU:
    def __init__(self):
        self.name = "Brake ECU"
        self.can_id = 0x200

    def generate_message(self):
        return {
            "ecu": self.name,
            "can_id": self.can_id,
            "data": [0, 80, 0, 0, 0, 0, 0, 0]
        }


brake = BrakeECU()

message = brake.generate_message()

print("Virtual ECU:", brake.name)
print("CAN ID:", hex(message["can_id"]))
print("Data:", message["data"])