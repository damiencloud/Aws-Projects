# 🚀 AWS Lambda EC2 Automation (Start/Stop Instances)

This project automates the **starting and stopping of EC2 instances** using **AWS Lambda** and **CloudWatch Events (EventBridge)**.

---

## 🧠 Overview

AWS Lambda is triggered automatically by a **CloudWatch schedule rule**.  
Depending on the rule, it executes either the **start** or **stop** function to manage EC2 instances — helping reduce costs by turning off non-production servers after hours.

---

## 🧰 AWS Services Used

| Service | Purpose |
|----------|----------|
| AWS Lambda | Runs the automation code |
| CloudWatch Events | Triggers Lambda on a schedule |
| EC2 | Target instances |
| IAM | Permissions for Lambda to control EC2 |

---

**Architecture Flow:**

CloudWatch Event (Scheduled Trigger)
│
▼
AWS Lambda (Python Script)
│
▼
Amazon EC2
(Start / Stop API)

---
<img width="1906" height="868" alt="Screenshot 2025-10-23 115300" src="https://github.com/user-attachments/assets/e92bb1e0-ad6a-4fe3-a6f6-e2c4e3e43b26" />

<img width="1917" height="481" alt="Screenshot 2025-10-23 115108" src="https://github.com/user-attachments/assets/ce35d5fb-9fa5-43d4-a042-cb32064ec929" />

<img width="1611" height="817" alt="Screenshot 2025-10-23 121018" src="https://github.com/user-attachments/assets/19598f51-066d-4b4d-a930-bda9abbfced0" />

<img width="1613" height="897" alt="Screenshot 2025-10-23 115728" src="https://github.com/user-attachments/assets/cd7d03cf-5aec-4b6e-bb8b-da735eeb7f3a" />

<img width="1905" height="865" alt="Screenshot 2025-10-23 115353" src="https://github.com/user-attachments/assets/d2c6ed30-f1d0-42e8-9887-4f0816025c65" />




---

Built with: AWS Lambda • EC2 • CloudWatch • IAM • Python (boto3)
