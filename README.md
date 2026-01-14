# defensive-analytics-siem-lite

## Defensive Cyber Analytics | Mini SIEM Project

**defensive-analytics-siem-lite** is a beginner-friendly cybersecurity project that demonstrates the core concepts behind a **Security Information and Event Management (SIEM)** system.  
The project focuses on **defensive cyber operations**, emphasizing log analysis, detection logic, alerting, and reporting.

This repository is designed to help learners and aspiring cyber professionals understand how security events are collected, analyzed, and transformed into actionable alerts in a SOC environment.

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
  - Most frequent source IPs
  - Targeted user accounts

---

## Planned Project Structure

