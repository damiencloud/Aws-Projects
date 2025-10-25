# 🤖 Build a Chatbot with Amazon Lex

This project demonstrates how to build and configure a **chatbot using Amazon Lex**, an AWS service for creating conversational interfaces without coding.  
The project helped me explore key chatbot concepts such as **intents, utterances, fallback responses**, and **confidence thresholds**.

---

## 🚀 Project Overview
The purpose of this project was to learn how **Amazon Lex** simplifies chatbot creation by allowing us to define conversational logic visually instead of writing code.  
I created a functional chatbot that can greet users, handle unknown inputs gracefully, and provide an engaging chat experience.

---

## 🧰 Tools & Concepts Used
- **AWS Lex**
- **IAM Role Permissions**
- **Intents & Utterances**
- **Fallback Intent**
- **Confidence Score Threshold**
- **Response Variations**

---

## 🛠️ Steps Implemented

### 1. **Set Up the Chatbot**
- Created a new chatbot from scratch using **Amazon Lex Console**.
- Setup time: approximately **7 minutes**.
- Created an **IAM role** with basic permissions to allow Lex to interact with AWS services like **Lambda**.

### 2. **Configure Intents**
- Created an intent called **WelcomeIntent**.
- Added sample utterances such as `"Hello"`, `"Hi"`, and `"Help me"`.
- Defined simple response messages for greeting users.

### 3. **Set Confidence Threshold**
- Used the default confidence score threshold of **0.40**.
- This means Lex must be at least **40% confident** before responding to user input.

### 4. **Test & Debug**
- Tested different user inputs:
  - `"Hiya"` and `"Hello"` → worked perfectly.
  - `"How are you"` and `"Good morning"` → triggered **FallbackIntent** since they didn’t match any defined intent.

### 5. **Configure FallbackIntent**
- Customized the **FallbackIntent** so the bot responds naturally when it doesn’t understand.
- Added **multiple response variations** to make replies sound more conversational.

---

## 💡 Key Learnings
- Gained hands-on understanding of **intents, utterances, and fallback logic**.
- Learned how **confidence thresholds** affect chatbot accuracy.
- Experienced how **Lex integrates with IAM** and other AWS services.
- Realized how easy it is to create AI-driven chatbots without coding.

---

## 🧩 Challenges Faced
- Encountered the message:  
  `"Intent FallbackIntent is fulfilled"` when unrecognized inputs were given.  
  Solved it by customizing FallbackIntent to respond properly.

---

## 🎉 Outcome
Created a working **chatbot (BankerBot)** that:
- Responds to greetings.
- Handles unknown inputs politely.
- Demonstrates real-world chatbot behavior using AWS Lex.

---

## 🕒 Duration
Approx. **1 hour** to complete the entire setup and testing.


---

> “It was most rewarding to see my bot respond exactly the way I wanted — without writing a single line of code.”
