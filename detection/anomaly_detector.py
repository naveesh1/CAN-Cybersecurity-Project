import pandas as pd
from collections import Counter

INPUT_FILE = "data/combined_traffic.csv"
OUTPUT_FILE = "data/detection_results.csv"

# Legitimate CAN IDs used by our virtual ECUs
KNOWN_CAN_IDS = {
    0x100: "Engine ECU",
    0x200: "Brake ECU",
    0x300: "Steering ECU",
    0x400: "Instrument Cluster ECU"
}

# Controlled simulated attack CAN ID
ATTACK_CAN_ID = 0x555

# Frequency threshold for this prototype
FREQUENCY_THRESHOLD = 15


def normalize_can_id(can_id):
    """Convert CAN ID into integer form."""
    if isinstance(can_id, str):
        can_id = can_id.strip()

        if can_id.lower().startswith("0x"):
            return int(can_id, 16)

        return int(can_id)

    return int(can_id)


def detect_anomalies():
    print("Loading CAN traffic...")
    
    df = pd.read_csv(INPUT_FILE)

    print(f"Total messages loaded: {len(df)}")

    # Detect the CAN ID column
    possible_id_columns = ["can_id", "CAN_ID", "id", "ID", "arbitration_id"]

    id_column = None

    for column in possible_id_columns:
        if column in df.columns:
            id_column = column
            break

    if id_column is None:
        raise ValueError(
            f"CAN ID column not found. Available columns: {list(df.columns)}"
        )

    print(f"Using CAN ID column: {id_column}")

    # Normalize CAN IDs
    df["CAN_ID_INT"] = df[id_column].apply(normalize_can_id)

    # Count frequency of each CAN ID
    id_counts = Counter(df["CAN_ID_INT"])

    # Detection columns
    df["status"] = "NORMAL"
    df["reason"] = ""

    for index, row in df.iterrows():

        can_id = row["CAN_ID_INT"]

        reasons = []

        # Rule 1: Unknown CAN ID
        if can_id not in KNOWN_CAN_IDS:
            reasons.append("Unknown CAN ID")

        # Rule 2: Known simulated attack ID
        if can_id == ATTACK_CAN_ID:
            reasons.append("Known simulated attack ID")

        # Rule 3: High-frequency traffic
        if id_counts[can_id] > FREQUENCY_THRESHOLD:
            reasons.append("High-frequency CAN traffic")

        if reasons:
            df.at[index, "status"] = "ANOMALY"
            df.at[index, "reason"] = "; ".join(reasons)

    # Remove helper column before saving
    df.drop(columns=["CAN_ID_INT"], inplace=True)

    # Save detection results
    df.to_csv(OUTPUT_FILE, index=False)

    # Statistics
    total_messages = len(df)
    anomaly_messages = (df["status"] == "ANOMALY").sum()
    normal_messages = (df["status"] == "NORMAL").sum()

    print()
    print("========================================")
    print("CAN ANOMALY DETECTION COMPLETE")
    print("========================================")
    print(f"Total Messages   : {total_messages}")
    print(f"Normal Messages  : {normal_messages}")
    print(f"Anomalies        : {anomaly_messages}")
    print(f"Detection File   : {OUTPUT_FILE}")
    print("========================================")


if __name__ == "__main__":
    detect_anomalies()