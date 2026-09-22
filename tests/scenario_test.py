import pandas as pd

INPUT_FILE = "data/detection_results.csv"


def test_normal_messages(df):
    normal_df = df[df["status"] == "NORMAL"]

    print("\n==============================")
    print("NORMAL TRAFFIC TEST")
    print("==============================")

    print(f"Normal messages found : {len(normal_df)}")

    if len(normal_df) > 0:
        print("PASS: Normal CAN messages detected correctly.")
    else:
        print("FAIL: No normal CAN messages found.")


def test_anomalous_messages(df):
    anomaly_df = df[df["status"] == "ANOMALY"]

    print("\n==============================")
    print("ATTACK TRAFFIC TEST")
    print("==============================")

    print(f"Anomalous messages found : {len(anomaly_df)}")

    if len(anomaly_df) > 0:
        print("PASS: Anomalous CAN messages detected.")
    else:
        print("FAIL: Attack traffic was not detected.")


def test_attack_id(df):
    attack_df = df[df["can_id"].astype(str).str.lower() == "0x555"]

    print("\n==============================")
    print("ATTACK CAN ID TEST")
    print("==============================")

    print(f"Attack ID messages found : {len(attack_df)}")

    if len(attack_df) > 0:
        print("PASS: Simulated attack ID 0x555 detected.")
    else:
        print("FAIL: Attack ID 0x555 not found.")


def main():

    print("========================================")
    print("CAN SECURITY SCENARIO TEST")
    print("========================================")

    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print("ERROR: detection_results.csv not found.")
        return

    print(f"Total messages loaded : {len(df)}")

    test_normal_messages(df)
    test_anomalous_messages(df)
    test_attack_id(df)

    print("\n========================================")
    print("SCENARIO TEST COMPLETE")
    print("========================================")


if __name__ == "__main__":
    main()