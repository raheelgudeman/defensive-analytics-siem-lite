# defensive-analytics-siem-lite

## Defensive Cyber Analytics | Mini SIEM Project

**defensive-analytics-siem-lite** is a beginner-friendly cybersecurity project that demonstrates the core concepts behind a **Security Information and Event Management (SIEM)** system.  
The project focuses on **defensive cyber operations**, emphasizing log analysis, detection logic, alerting, and reporting.

This repository helps learners and aspiring cyber professionals understand how security events are collected, analyzed, and transformed into actionable alerts in a SOC environment.

---

## Project Goals
- Understand how SIEM systems work at a foundational level
- Practice defensive cyber analytics using Python
- Build hands-on experience with logs, detection rules, and alerts
- Develop skills relevant to SOC Analyst and Cyber Defense roles

---

## Core Cybersecurity Concepts
- Log ingestion and parsing
- Event normalization
- Rule-based detection logic
- Alert generation
- Incident reporting
- Basic anomaly detection

---

## Features

### Log Ingestion
- Ingests authentication and security logs
- Supports structured formats such as CSV
- Simulates real-world security telemetry

### Event Normalization
- Converts raw logs into structured events
- Extracted fields include:
  - Timestamp
  - Username
  - Source IP
  - Event type
  - Status (success or failure)

### Detection Logic (SIEM-lite)
Implements basic but realistic detection rules:
- Multiple failed login attempts
- Potential brute-force behavior
- Repeated authentication failures from the same IP
- Abnormal login activity patterns

### Alerting
- Generates security alerts when thresholds are exceeded
- Alerts include severity, timestamp, and description
- Output stored in structured formats for review

### Reporting
- Produces summary reports including:
  - Total events processed
  - Alerts generated
  - Successful vs failed login counts
  - Top source IPs by event volume

---

## Technologies Used
- Python 3
- Pandas
- CSV and JSON data handling
- Command-line execution (macOS Terminal)  
- Git & GitHub (SSH authentication)  

---
## Project Structure

## How the SIEM-lite Workflow Works

1. **Log Ingestion**  
   Authentication logs are loaded from a CSV file and parsed into structured events.

2. **Event Analysis**  
   Login attempts are analyzed to distinguish successful and failed authentications.

3. **Detection Logic**  
   Repeated failed login attempts from the same source IP are evaluated to detect potential brute-force behavior.

4. **Alert Generation**  
   Suspicious activity is written to `alerts.csv` for analyst review.

5. **Reporting**  
   A SOC-style summary report is generated in `report.txt`, providing visibility into activity trends and suspicious sources.

---

## How to Run (Local)

### 1. Clone the repository (SSH)
```bash
git clone git@github.com:raheelgudeman/defensive-analytics-siem-lite.git
cd defensive-analytics-siem-lite


