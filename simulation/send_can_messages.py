import can

from engine_ecu import EngineECU
from brake_ecu import BrakeECU
from steering_ecu import SteeringECU
from instrument_cluster_ecu import InstrumentClusterECU


bus = can.Bus(
    interface="virtual",
    channel="CAN_Cybersecurity_Bus",
    receive_own_messages=True
)


ecus = [
    EngineECU(),
    BrakeECU(),
    SteeringECU(),
    InstrumentClusterECU()
]


print("===== SENDING CAN MESSAGES =====")

for ecu in ecus:
    ecu_data = ecu.generate_message()

    message = can.Message(
        arbitration_id=ecu_data["can_id"],
        data=ecu_data["data"],
        is_extended_id=False
    )

    bus.send(message)

    print(
        "Sent:",
        ecu_data["ecu"],
        "| CAN ID:",
        hex(message.arbitration_id),
        "| Data:",
        list(message.data)
    )


print()
print("===== ALL MESSAGES SENT =====")

bus.shutdown()