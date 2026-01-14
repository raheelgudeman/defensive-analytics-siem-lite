from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "logs" / "sample_auth_logs.csv"
REPORT_OUTPUT = BASE_DIR / "output" / "report.txt"

def load_logs(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path)

def generate_report(df: pd.DataFrame) -> str:
    total_events = len(df)
    failed_events = len(df[df["status"] == "failure"])
    success_events = len(df[df["status"] == "success"])

    top_ips = (
        df.groupby("source_ip")
        .size()
        .sort_values(ascending=False)
        .head(5)
    )

    lines = []
    lines.append("Defensive Analytics SIEM-lite Report")
    lines.append("-----------------------------------")
    lines.append(f"Total events: {total_events}")
    lines.append(f"Successful events: {success_events}")
    lines.append(f"Failed events: {failed_events}")
    lines.append("")
    lines.append("Top Source IPs (by event volume):")

    for ip, count in top_ips.items():
        lines.append(f"- {ip}: {count} events")

    return "\n".join(lines)

def main() -> None:
    logs = load_logs(LOG_FILE)
    report_text = generate_report(logs)

    REPORT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_OUTPUT, "w", encoding="utf-8") as f:
        f.write(report_text)

    print(f"Report saved to: {REPORT_OUTPUT}")
    print("")
    print(report_text)

if __name__ == "__main__":
    main()
