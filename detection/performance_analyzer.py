import pandas as pd

INPUT_FILE = "data/detection_results.csv"
OUTPUT_FILE = "data/performance_results.txt"

ATTACK_CAN_ID = 0x555


def normalize_can_id(can_id):
    if isinstance(can_id, str):
        can_id = can_id.strip()

        if can_id.lower().startswith("0x"):
            return int(can_id, 16)

        return int(can_id)

    return int(can_id)


def main():
    print("Loading detection results...")

    df = pd.read_csv(INPUT_FILE)

    df["CAN_ID_INT"] = df["can_id"].apply(normalize_can_id)

    # Ground truth
    df["actual"] = df["CAN_ID_INT"].apply(
        lambda x: "ANOMALY" if x == ATTACK_CAN_ID else "NORMAL"
    )

    # Detector prediction
    df["predicted"] = df["status"]

    true_positive = (
        (df["actual"] == "ANOMALY") &
        (df["predicted"] == "ANOMALY")
    ).sum()

    true_negative = (
        (df["actual"] == "NORMAL") &
        (df["predicted"] == "NORMAL")
    ).sum()

    false_positive = (
        (df["actual"] == "NORMAL") &
        (df["predicted"] == "ANOMALY")
    ).sum()

    false_negative = (
        (df["actual"] == "ANOMALY") &
        (df["predicted"] == "NORMAL")
    ).sum()

    total = len(df)

    accuracy = (true_positive + true_negative) / total

    precision = (
        true_positive / (true_positive + false_positive)
        if (true_positive + false_positive) > 0
        else 0
    )

    recall = (
        true_positive / (true_positive + false_negative)
        if (true_positive + false_negative) > 0
        else 0
    )

    f1_score = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0
    )

    detection_rate = recall

    results = f"""
========================================
CAN DETECTION PERFORMANCE
========================================
Total Messages       : {total}
True Positives       : {true_positive}
True Negatives       : {true_negative}
False Positives      : {false_positive}
False Negatives      : {false_negative}

Accuracy             : {accuracy * 100:.2f}%
Precision            : {precision * 100:.2f}%
Recall               : {recall * 100:.2f}%
F1-Score             : {f1_score * 100:.2f}%
Detection Rate       : {detection_rate * 100:.2f}%
========================================
"""

    print(results)

    with open(OUTPUT_FILE, "w") as file:
        file.write(results)

    print(f"Performance results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()