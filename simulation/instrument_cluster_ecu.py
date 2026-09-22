class InstrumentClusterECU:
    def __init__(self):
        self.name = "Instrument Cluster ECU"
        self.can_id = 0x400

    def generate_message(self):
        return {
            "ecu": self.name,
            "can_id": self.can_id,
            "data": [60, 11, 184, 0, 0, 0, 0, 0]
        }


cluster = InstrumentClusterECU()

message = cluster.generate_message()

print("Virtual ECU:", cluster.name)
print("CAN ID:", hex(message["can_id"]))
print("Data:", message["data"])