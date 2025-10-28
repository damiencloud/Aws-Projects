# Amazon CloudWatch Agent Configuration Guide

This guide provides configuration examples for enabling the **Amazon CloudWatch Agent** on an EC2 instance.  
It includes two setups:
1. **Metrics-Only Configuration**
2. **Metrics + Logs Configuration**

---

## 🧩 Overview

The CloudWatch Agent helps you collect and publish **system metrics** (like CPU, memory, and disk usage) and **log files** (like `/var/log/messages`) from your EC2 instance to **Amazon CloudWatch**.

---

# ⚙️ 1️⃣ Metrics-Only Configuration

This configuration collects detailed system metrics and publishes them to CloudWatch under the `CWAgent` namespace.

### **JSON Config**
```json
{
  "agent": {
    "metrics_collection_interval": 60,
    "run_as_user": "root"
  },
  "metrics": {
    "aggregation_dimensions": [
      ["InstanceId"]
    ],
    "append_dimensions": {
      "AutoScalingGroupName": "${aws:AutoScalingGroupName}",
      "ImageId": "${aws:ImageId}",
      "InstanceId": "${aws:InstanceId}",
      "InstanceType": "${aws:InstanceType}"
    },
    "metrics_collected": {
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
      },
      "disk": {
        "measurement": ["used_percent", "inodes_free"],
        "metrics_collection_interval": 60,
        "resources": ["*"]
      },
      "diskio": {
        "measurement": ["io_time"],
        "metrics_collection_interval": 60,
        "resources": ["*"]
      },
      "mem": {
        "measurement": ["mem_used_percent"],
        "metrics_collection_interval": 60
      },
      "statsd": {
        "metrics_aggregation_interval": 60,
        "metrics_collection_interval": 10,
        "service_address": ":8125"
      },
      "swap": {
        "measurement": ["swap_used_percent"],
        "metrics_collection_interval": 60
      }
    }
  }
}
```

---

## 📊 Metrics Collected

| Category | Metrics | Description |
|-----------|----------|--------------|
| CPU | `cpu_usage_idle`, `cpu_usage_user`, `cpu_usage_system`, `cpu_usage_iowait` | CPU performance metrics |
| Disk | `used_percent`, `inodes_free` | Disk usage and inode availability |
| Disk I/O | `io_time` | Disk I/O operations |
| Memory | `mem_used_percent` | Memory usage |
| Swap | `swap_used_percent` | Swap utilization |
| StatsD | Custom metrics via UDP port `8125` | Application-level metrics |

---

# ⚙️ 2️⃣ Metrics + Logs Configuration

This configuration includes **everything from the metrics-only setup**, and additionally collects logs from `/var/log/messages`.

### **Full JSON Config**
```json
{
  "agent": {
    "metrics_collection_interval": 60,
    "run_as_user": "root"
  },
  "logs": {
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "file_path": "/var/log/messages",
            "log_group_class": "STANDARD",
            "log_group_name": "ec2logsforcwagentinstance",
            "log_stream_name": "ec2logstream",
            "retention_in_days": 1
          }
        ]
      }
    }
  },
  "metrics": {
    "aggregation_dimensions": [
      ["InstanceId"]
    ],
    "append_dimensions": {
      "AutoScalingGroupName": "${aws:AutoScalingGroupName}",
      "ImageId": "${aws:ImageId}",
      "InstanceId": "${aws:InstanceId}",
      "InstanceType": "${aws:InstanceType}"
    },
    "metrics_collected": {
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
      },
      "disk": {
        "measurement": ["used_percent", "inodes_free"],
        "metrics_collection_interval": 60,
        "resources": ["*"]
      },
      "diskio": {
        "measurement": ["io_time"],
        "metrics_collection_interval": 60,
        "resources": ["*"]
      },
      "mem": {
        "measurement": ["mem_used_percent"],
        "metrics_collection_interval": 60
      },
      "statsd": {
        "metrics_aggregation_interval": 60,
        "metrics_collection_interval": 10,
        "service_address": ":8125"
      },
      "swap": {
        "measurement": ["swap_used_percent"],
        "metrics_collection_interval": 60
      }
    }
  }
}
```

---

## 📜 Logs Collected

| Field | Value |
|--------|--------|
| **File path** | `/var/log/messages` |
| **Log group name** | `ec2logsforcwagentinstance` |
| **Log stream name** | `ec2logstream` |
| **Retention** | 1 day |
| **Class** | STANDARD |

💡 This sends system messages from `/var/log/messages` to **CloudWatch Logs**.

---

## 🚀 Deployment Steps

1. **Save configuration file:**
   ```bash
   sudo mkdir -p /opt/aws/amazon-cloudwatch-agent/etc
   sudo nano /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
   ```
   Paste one of the above JSON configs and save the file.

2. **Start or reload the agent:**
   ```bash
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl      -a fetch-config      -m ec2      -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json      -s
   ```

3. **Verify agent status:**
   ```bash
   sudo systemctl status amazon-cloudwatch-agent
   ```

4. **View in CloudWatch:**
   - **Metrics:** CloudWatch → *Metrics → CWAgent*  
   - **Logs:** CloudWatch → *Logs → Log groups → ec2logsforcwagentinstance*

---

## 📈 Example Metrics Table

| Metric Name | Description | Unit |
|--------------|-------------|------|
| `cpu_usage_user` | CPU time spent in user space | Percent |
| `mem_used_percent` | Memory used percentage | Percent |
| `disk_used_percent` | Disk utilization | Percent |
| `swap_used_percent` | Swap usage | Percent |
| `io_time` | Disk I/O time | Milliseconds |

---

✅ **Summary**
| Config Type | Includes Logs? | Includes Metrics? |
|--------------|----------------|------------------|
| Metrics Only | ❌ No | ✅ Yes |
| Metrics + Logs | ✅ Yes | ✅ Yes |
