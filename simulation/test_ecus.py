from engine_ecu import EngineECU
from brake_ecu import BrakeECU
from steering_ecu import SteeringECU
from instrument_cluster_ecu import InstrumentClusterECU


engine = EngineECU()
brake = BrakeECU()
steering = SteeringECU()
cluster = InstrumentClusterECU()


ecus = [
    engine,
    brake,
    steering,
    cluster
]


print("===== VIRTUAL ECU NETWORK =====")

for ecu in ecus:
    message = ecu.generate_message()

    print()
    print("ECU:", message["ecu"])
    print("CAN ID:", hex(message["can_id"]))
    print("Data:", message["data"])

print()
print("===== ALL ECUs WORKING =====")