import can
import time

from engine_ecu import EngineECU
from brake_ecu import BrakeECU
from steering_ecu import SteeringECU
from instrument_cluster_ecu import InstrumentClusterECU


# Create virtual CAN bus
bus = can.Bus(
    interface="virtual",
    channel="CAN_Cybersecurity_Bus",
    receive_own_messages=True
)


# Create virtual ECUs
ecus = [
    EngineECU(),
    BrakeECU(),
    SteeringECU(),
    InstrumentClusterECU()
]


print("===================================")
print("   VIRTUAL CAN NETWORK STARTED")
print("===================================")


for cycle in range(3):

    print()
    print("----- CAN Cycle", cycle + 1, "-----")

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
            "| ID:",
            hex(message.arbitration_id),
            "| Data:",
            list(message.data)
        )

    time.sleep(1)


print()
print("===================================")
print("   CAN NETWORK TEST COMPLETE")
print("===================================")


bus.shutdown()