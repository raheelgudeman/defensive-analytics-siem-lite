from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "logs" / "sample_auth_logs.csv"
ALERT_OUTPUT = BASE_DIR / "output" / "alerts.csv"

FAILED_THRESHOLD = 5

def load_logs(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path)

def detect_bruteforce(df: pd.DataFrame, threshold: int) -> pd.DataFrame:
    failed = df[df["status"] == "failure"]

    counts = (
        failed.groupby("source_ip")
        .size()
        .reset_index(name="failed_count")
    )

    suspicious = counts[counts["failed_count"] >= threshold]
    return suspicious

def main() -> None:
    logs = load_logs(LOG_FILE)
    alerts = detect_bruteforce(logs, FAILED_THRESHOLD)

    if alerts.empty:
        print("No brute-force behavior detected.")
    else:
        print("Brute-force alerts generated:")
        print(alerts)

        ALERT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        alerts.to_csv(ALERT_OUTPUT, index=False)
        print(f"Saved alerts to: {ALERT_OUTPUT}")

if __name__ == "__main__":
    main()
