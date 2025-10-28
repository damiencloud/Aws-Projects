
# 🚀 AWS EC2 Monitoring with CloudWatch Agent & Alarm Setup

This project demonstrates how to **create, configure, and monitor an EC2 instance** using the **Amazon CloudWatch Agent**, and set up a **CPU Utilization Alarm (CPU > 80%)** to simulate a production-style monitoring setup.

## 🧩 Project Overview

This guide covers:

1. Launching an EC2 Instance (Amazon Linux 2023)
2. Creating an IAM Role for CloudWatch Agent
3. Installing and configuring the CloudWatch Agent on EC2
4. Viewing metrics in CloudWatch
5. Creating a CPU Utilization Alarm (>80%)
6. Testing the alarm by stressing the instance

---

## 🛠️ Step 1: Create IAM Role for CloudWatch Agent

- Navigate to **IAM → Roles → Create Role**
- Choose **Trusted Entity: AWS Service → EC2**
- Attach the following policies:
  - `AmazonEC2RoleforSSM`
  - `CloudWatchAgentServerPolicy`
- Name the role: **`CwAgentRole`**

📄 **Trust Policy Example**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": ["ec2.amazonaws.com"]
      }
    }
  ]
}
```

---

## 🖥️ Step 2: Launch EC2 Instance

- Go to **EC2 → Launch Instance**
- AMI: `Amazon Linux 2023`
- Instance Type: `t3.micro`
- Key Pair: Use existing or create a new one
- Security Group: Allow SSH (port 22)
- Attach IAM Role: **`CwAgentRole`**

✅ Once launched, verify the instance details (Public IP, VPC ID, Subnet, etc.)  
💡 Example: Instance ID `i-046f5098ebc0720f9`, Role `CwAgentRole`

---

## ⚙️ Step 3: Connect & Install CloudWatch Agent

SSH into your instance:

```bash
ssh -i "your-key.pem" ec2-user@<public-ip>
```

Install the CloudWatch agent:

```bash
sudo yum install amazon-cloudwatch-agent -y
```

---

## ⚡ Step 4: Configure CloudWatch Agent

Run the agent configuration wizard:

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
```

Follow prompts:
- OS: `linux`
- Host Type: `EC2`
- User: `cwagent`
- StatsD Daemon: `no`
- Metrics: Select defaults for CPU, memory, disk, etc.

Start the CloudWatch Agent:

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json -s
```

✅ Validation success message confirms proper setup.

---

## 📊 Step 5: View Metrics in CloudWatch

- Navigate to **CloudWatch → Metrics → CWAgent**
- Observe metrics like:
  - `CPUUtilization`
  - `mem_used_percent`
  - `disk_used_percent`

📸 *Example Metric Graphs (CPUUtilization)*  
![CloudWatch Metrics Screenshot](./screenshots/metrics.png)

---

## 🚨 Step 6: Create CPU Utilization Alarm

- Go to **CloudWatch → Alarms → Create Alarm**
- Select metric: `CWAgent → CPUUtilization`
- Set condition:
  - Threshold: `Greater than 80%`
  - Period: `5 minutes`
- Actions:
  - Notification: Create SNS topic (email notification)
- Name the alarm: `HighCPUAlarm`

---

## 🧪 Step 7: Test the Alarm

SSH into the instance and simulate high CPU usage:

```bash
sudo amazon-linux-extras install stress -y
stress --cpu 4 --timeout 300
```

After a few minutes:
- CloudWatch will detect CPU > 80%
- Alarm state changes from **OK → ALARM**
- Email/SNS notification is triggered

---

## ✅ Step 8: Verification

- Go to **CloudWatch → Alarms**
- Confirm:
  - Alarm State = `ALARM`
  - Notifications received
- Stop the stress process:
  ```bash
  pkill stress
  ```
- Alarm returns to **OK** state.

---

## 🧾 Summary

| Component | Description |
|------------|--------------|
| **EC2 Instance** | Amazon Linux 2023 (t3.micro) |
| **IAM Role** | `CwAgentRole` with SSM + CloudWatch policies |
| **Monitoring** | CloudWatch Agent (CPU, Memory, Disk) |
| **Alarm** | CPU > 80% (SNS Email Alert) |
| **Region** | ap-south-1 (Mumbai) |

---

## 📂 Folder Structure

```
aws-ec2-monitoring/
├── README.md
├── screenshots/
│   ├── create-role.png
│   ├── ec2-details.png
│   ├── cloudwatch-agent-install.png
│   ├── cloudwatch-agent-config.png
│   ├── validation-success.png
│   ├── top-cpu-usage.png
│   └── metrics.png
```

---

## 🧠 Notes

- Ensure EC2 has correct IAM Role permissions.
- Verify that CloudWatch Agent service is running:
  ```bash
  sudo systemctl status amazon-cloudwatch-agent
  ```
- Use **AWS CLI** to list alarms:
  ```bash
  aws cloudwatch describe-alarms
  ```

---

## 📧 Author

**Eros Works**  
AWS Hands-on Projects | Cloud & DevOps Learning  
📍 AWS Region: Mumbai  
🕹️ GitHub: [Add your repo link here]

---
