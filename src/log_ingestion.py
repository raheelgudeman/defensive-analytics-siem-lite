from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "logs" / "sample_auth_logs.csv"

def load_logs(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path)

def main() -> None:
    logs = load_logs(LOG_FILE)

    print("Log Ingestion Successful")
    print(f"Total events loaded: {len(logs)}")

    failed_logins = logs[logs["status"] == "failure"]
    print(f"Failed login attempts: {len(failed_logins)}")

if __name__ == "__main__":
    main()
