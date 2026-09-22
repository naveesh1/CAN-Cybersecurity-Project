import can

from engine_ecu import EngineECU
from brake_ecu import BrakeECU
from steering_ecu import SteeringECU
from instrument_cluster_ecu import InstrumentClusterECU


def create_can_message(can_id, data):
    return can.Message(
        arbitration_id=can_id,
        data=data,
        is_extended_id=False
    )


ecus = [
    EngineECU(),
    BrakeECU(),
    SteeringECU(),
    InstrumentClusterECU()
]


print("===== CAN MESSAGES FROM ALL ECUs =====")

for ecu in ecus:
    ecu_data = ecu.generate_message()

    message = create_can_message(
        ecu_data["can_id"],
        ecu_data["data"]
    )

    print()
    print("ECU:", ecu_data["ecu"])
    print("CAN ID:", hex(message.arbitration_id))
    print("Data:", list(message.data))
    print("DLC:", message.dlc)

print()
print("===== MESSAGE GENERATION COMPLETE =====")