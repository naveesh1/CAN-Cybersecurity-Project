class EngineECU:
    def __init__(self):
        self.name = "Engine ECU"
        self.can_id = 0x100

    def generate_message(self):
        return {
            "ecu": self.name,
            "can_id": self.can_id,
            "data": [100, 0, 0, 0, 0, 0, 0, 0]
        }


engine = EngineECU()

message = engine.generate_message()

print("Virtual ECU:", engine.name)
print("CAN ID:", hex(message["can_id"]))
print("Data:", message["data"])