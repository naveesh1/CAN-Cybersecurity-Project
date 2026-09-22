class SteeringECU:
    def __init__(self):
        self.name = "Steering ECU"
        self.can_id = 0x300

    def generate_message(self):
        return {
            "ecu": self.name,
            "can_id": self.can_id,
            "data": [45, 0, 0, 0, 0, 0, 0, 0]
        }


steering = SteeringECU()

message = steering.generate_message()

print("Virtual ECU:", steering.name)
print("CAN ID:", hex(message["can_id"]))
print("Data:", message["data"])