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



<img width="1906" height="868" alt="Screenshot 2025-10-23 115300" src="https://github.com/user-attachments/assets/42b012fa-765b-429c-8d4c-3ca82e830056" />

   <img width="1917" height="481" alt="Screenshot 2025-10-23 115108" src="https://github.com/user-attachments/assets/e8ebc5da-08a0-46fe-a18d-9841729d009d" />


<img width="1613" height="897" alt="Screenshot 2025-10-23 115728" src="https://github.com/user-attachments/assets/39ec3f99-8f5b-4dfc-a939-86514e386a1a" />


<img width="1905" height="865" alt="Screenshot 2025-10-23 115353" src="https://github.com/user-attachments/assets/51ddc0d1-deef-4733-99e6-ecabbda5c517" />


<img width="1611" height="817" alt="Screenshot 2025-10-23 121018" src="https://github.com/user-attachments/assets/99c223cd-5528-4b0f-9d4e-ea7c71c2304d" />

---

Built with: AWS Lambda • EC2 • CloudWatch • IAM • Python (boto3)
