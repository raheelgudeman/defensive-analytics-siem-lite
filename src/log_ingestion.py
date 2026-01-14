import pandas as pd

LOG_FILE = "../logs/sample_auth_logs.csv"

def load_logs(file_path):
    """
    Load authentication logs from CSV file.
    """
    df = pd.read_csv(file_path)
    return df

def main():
    logs = load_logs(LOG_FILE)

    print("Log Ingestion Successful")
    print(f"Total events loaded: {len(logs)}")

    failed_logins = logs[logs["status"] == "failure"]
    print(f"Failed login attempts: {len(failed_logins)}")

if __name__ == "__main__":
    main()
