import pandas as pd

LOG_FILE = "../logs/sample_auth_logs.csv"
ALERT_OUTPUT = "../output/alerts.csv"

FAILED_THRESHOLD = 5  # number of failed logins to trigger an alert


def load_logs(file_path):
    df = pd.read_csv(file_path)
    return df


def detect_bruteforce(df, threshold):
    """
    Detect brute-force attempts by counting failed logins per source_ip.
    Returns a DataFrame of suspicious IPs that meet or exceed the threshold.
    """
    failed = df[df["status"] == "failure"]

    counts = (
        failed.groupby("source_ip")
        .size()
        .reset_index(name="failed_count")
    )

    suspicious = counts[counts["failed_count"] >= threshold]
    return suspicious


def main():
    logs = load_logs(LOG_FILE)
    alerts = detect_bruteforce(logs, FAILED_THRESHOLD)

    if alerts.empty:
        print("No brute-force behavior detected.")
    else:
        print("Brute-force alerts generated:")
        print(alerts)

        alerts.to_csv(ALERT_OUTPUT, index=False)
        print(f"Saved alerts to: {ALERT_OUTPUT}")


if __name__ == "__main__":
    main()
