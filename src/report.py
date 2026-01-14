import pandas as pd

LOG_FILE = "../logs/sample_auth_logs.csv"
REPORT_OUTPUT = "../output/report.txt"


def load_logs(file_path):
    df = pd.read_csv(file_path)
    return df


def generate_report(df):
    total_events = len(df)
    failed_events = len(df[df["status"] == "failure"])
    success_events = len(df[df["status"] == "success"])

    top_ips = (
        df.groupby("source_ip")
        .size()
        .sort_values(ascending=False)
        .head(5)
    )

    report_lines = []
    report_lines.append("Defensive Analytics SIEM-lite Report")
    report_lines.append("-----------------------------------")
    report_lines.append(f"Total events: {total_events}")
    report_lines.append(f"Successful events: {success_events}")
    report_lines.append(f"Failed events: {failed_events}")
    report_lines.append("")
    report_lines.append("Top Source IPs (by event volume):")

    for ip, count in top_ips.items():
        report_lines.append(f"- {ip}: {count} events")

    return "\n".join(report_lines)


def main():
    logs = load_logs(LOG_FILE)
    report_text = generate_report(logs)

    with open(REPORT_OUTPUT, "w", encoding="utf-8") as f:
        f.write(report_text)

    print(f"Report saved to: {REPORT_OUTPUT}")
    print("")
    print(report_text)


if __name__ == "__main__":
    main()
