# Legendary AWS Networks – VPC

## 🚀 Project Overview
This project focuses on building a **Virtual Private Cloud (VPC)** using **Amazon Web Services (AWS)**. The goal was to understand how to create a secure, isolated network environment that enables efficient control over subnets, routing, and internet connectivity.

---

## 🌐 What is Amazon VPC?
**Amazon VPC (Virtual Private Cloud)** is a virtual network within AWS that allows you to launch and manage resources securely.  
It’s useful because it provides complete control over:
- IP addressing
- Routing tables
- Subnets (public and private)
- Internet connectivity

---

## 🛠️ How I Used Amazon VPC in This Project
In this project, I created a **secure, isolated network environment** by configuring:
- A **custom VPC** with a defined IPv4 CIDR block.
- **Subnets** for organizing resources and enabling efficient routing.
- An **Internet Gateway (IGW)** to allow public access for specific instances.
- **Auto-assign public IPv4** to ensure new instances automatically receive public IPs.

This configuration allowed smooth communication between resources and ensured public-facing instances were accessible through the internet.

---

## 💡 Key Learnings
- Attaching an **Internet Gateway** is crucial for enabling internet access.  
  Without it, users cannot reach instances in the public subnet.
- **Subnets** act like neighborhoods within a city — each serving a specific purpose.
- **Auto-assigning public IPv4** simplifies deployment for public-facing resources like web servers.
- Even small routing misconfigurations can completely block network access.

---

## ⏱️ Time Taken
This project took approximately **45 minutes** to complete.

---

## 🧠 Reflection
One thing I didn’t expect in this project was how vital proper subnet configuration and routing were. A small oversight in settings could block internet access entirely, highlighting the importance of precision in cloud networking.

---

## 📚 Learn More
You can explore more cloud projects and discussions at  
👉 [NextWork.org](https://community.nextwork.org)

---

**Author:** Damien Joseph  
**Platform:** [NextWork](https://community.nextwork.org)
