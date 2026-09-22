import pandas as pd

INPUT_FILE = "data/detection_results.csv"
OUTPUT_FILE = "data/detection_summary.txt"


def generate_summary():

    df = pd.read_csv(INPUT_FILE)

    total = len(df)
    normal = (df["status"] == "NORMAL").sum()
    anomalies = (df["status"] == "ANOMALY").sum()

    anomaly_percentage = (anomalies / total) * 100 if total > 0 else 0

    print("========================================")
    print("CAN DETECTION SUMMARY")
    print("========================================")
    print(f"Total Messages      : {total}")
    print(f"Normal Messages     : {normal}")
    print(f"Anomalous Messages  : {anomalies}")
    print(f"Anomaly Percentage  : {anomaly_percentage:.2f}%")
    print()

    print("Anomaly Reasons:")
    print(df.loc[df["status"] == "ANOMALY", "reason"].value_counts())

    with open(OUTPUT_FILE, "w") as file:
        file.write("CAN DETECTION SUMMARY\n")
        file.write("=====================\n")
        file.write(f"Total Messages: {total}\n")
        file.write(f"Normal Messages: {normal}\n")
        file.write(f"Anomalous Messages: {anomalies}\n")
        file.write(f"Anomaly Percentage: {anomaly_percentage:.2f}%\n\n")

        file.write("Anomaly Reasons:\n")
        file.write(
            df.loc[df["status"] == "ANOMALY", "reason"]
            .value_counts()
            .to_string()
        )

    print()
    print(f"Summary saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_summary()