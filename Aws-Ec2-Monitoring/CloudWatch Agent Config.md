# CloudWatch Agent Configuration

This configuration enables the **Amazon CloudWatch Agent** on an EC2 instance to collect and publish key system metrics for monitoring CPU, memory, disk, and network I/O performance.

## 🧩 Overview

The configuration file defines:
- Metrics collection intervals  
- User permissions for running the agent  
- System-level metrics to collect (CPU, Disk, Memory, Swap, etc.)  
- Dimensions and metadata to attach to each metric (like Instance ID, Image ID, etc.)

---

## ⚙️ Configuration Details

### **Agent Section**
```json
"agent": {
  "metrics_collection_interval": 60,
  "run_as_user": "root"
}
```
- **metrics_collection_interval:** Collects metrics every 60 seconds.  
- **run_as_user:** Runs the agent as the `root` user for full system access.

---

### **Metrics Section**
```json
"metrics": {
  "aggregation_dimensions": [["InstanceId"]],
  "append_dimensions": {
    "AutoScalingGroupName": "${aws:AutoScalingGroupName}",
    "ImageId": "${aws:ImageId}",
    "InstanceId": "${aws:InstanceId}",
    "InstanceType": "${aws:InstanceType}"
  }
}
```
- **aggregation_dimensions:** Groups metrics by EC2 Instance ID.  
- **append_dimensions:** Adds identifying metadata for easier filtering in CloudWatch.

---

### **Metrics Collected**

#### 🖥️ CPU
```json
"cpu": {
  "measurement": [
    "cpu_usage_idle",
    "cpu_usage_iowait",
    "cpu_usage_user",
    "cpu_usage_system"
  ],
  "metrics_collection_interval": 60,
  "resources": ["*"],
  "totalcpu": false
}
```
Collects detailed CPU usage metrics (idle, system, user, I/O wait).

---

#### 💾 Disk
```json
"disk": {
  "measurement": ["used_percent", "inodes_free"],
  "metrics_collection_interval": 60,
  "resources": ["*"]
}
```
Tracks disk space usage and available inodes.

---

#### 📊 Disk I/O
```json
"diskio": {
  "measurement": ["io_time"],
  "metrics_collection_interval": 60,
  "resources": ["*"]
}
```
Measures I/O time for disk operations.

---

#### 🧠 Memory
```json
"mem": {
  "measurement": ["mem_used_percent"],
  "metrics_collection_interval": 60
}
```
Monitors percentage of used memory.

---

#### 🔄 Swap
```json
"swap": {
  "measurement": ["swap_used_percent"],
  "metrics_collection_interval": 60
}
```
Tracks swap space utilization.

---

#### 📡 StatsD
```json
"statsd": {
  "metrics_aggregation_interval": 60,
  "metrics_collection_interval": 10,
  "service_address": ":8125"
}
```
Enables custom StatsD metrics collection from applications listening on port **8125**.

---

## 🚀 Deployment Steps

1. Save this configuration as `/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json`.
2. Start or restart the CloudWatch Agent:
   ```bash
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl      -a fetch-config      -m ec2      -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json      -s
   ```
3. Verify the agent is running:
   ```bash
   sudo systemctl status amazon-cloudwatch-agent
   ```
4. View metrics in the **CloudWatch → Metrics → CWAgent** namespace.

---

## 📈 Example Metrics in CloudWatch

| Metric Name | Description | Unit |
|--------------|-------------|------|
| `cpu_usage_user` | CPU time spent in user space | Percent |
| `mem_used_percent` | Memory used percentage | Percent |
| `disk_used_percent` | Disk utilization | Percent |
| `swap_used_percent` | Swap usage | Percent |
| `io_time` | Disk I/O time | Milliseconds |
