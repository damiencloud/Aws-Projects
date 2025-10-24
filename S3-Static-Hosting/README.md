# 🌐 Host a Static Website on Amazon S3

This project demonstrates how to host a **static website** using **Amazon S3**.  
It was completed as part of my cloud learning journey to understand AWS storage and hosting services.

---

## 🚀 Project Overview
The goal of this project was to learn how **Amazon S3** can be used to store and serve static website content directly from the cloud.  
By configuring S3 bucket settings and permissions, we can make a simple HTML website publicly accessible to anyone on the internet.

---

## 🧰 Tools & Concepts Used
- **AWS S3 (Simple Storage Service)**
- **Static Website Hosting**
- **Bucket Policy & ACL (Access Control List)**
- **Index Document (index.html)**
- **Bucket Endpoints**
- **Public Access Configuration**

---

## 🛠️ Steps Implemented

### 1. **Create an S3 Bucket**
- Chose **Mumbai (ap-south-1)** as the region to minimize latency.
- Configured the bucket name (S3 bucket names must be **globally unique**).
- Disabled **Block Public Access** to allow website visibility.

### 2. **Upload Website Files**
- Uploaded:
  - `index.html` – the main website structure.
  - `/assets/` – images and other resources for the website.

### 3. **Enable Static Website Hosting**
- Enabled **Static Website Hosting** under the bucket properties.
- Set `index.html` as the index document.

### 4. **Fix Access Permissions**
- Initially received a **403 Forbidden** error.
- Solved by:
  - Enabling **ACLs (Access Control Lists)**.
  - Granting public read access to website files.

### 5. **Access via Endpoint URL**
- AWS generated a **bucket endpoint URL**.
- Once access permissions were correctly configured, the website loaded successfully and became publicly accessible.

---

## 💡 Key Learnings
- Importance of **bucket-level** and **object-level** permissions.
- How to configure **static website hosting** in AWS.
- Understanding **latency and region selection** for better performance.
- Troubleshooting **403 Forbidden** access issues.

---

## 🧩 Challenges Faced
- Resolving the **403 Forbidden** error due to restricted object permissions.
- Understanding how **ACLs** and **public access settings** interact in AWS.

---

## 🎉 Outcome
After adjusting permissions and access settings, the website was successfully hosted on S3 and publicly available via its endpoint URL.

---

## 🕒 Duration
Approx. **45 minutes** to complete.

---

> “It was most rewarding to see my webpage load live and be public to the world.”
