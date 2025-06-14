# 📊 CloudQuant

CloudQuant is a fully serverless stock market data pipeline built using **AWS CDK (Python)**. It automates the ingestion, transformation, storage, and analysis of real-time stock data using modern AWS services, all provisioned through infrastructure as code.

---

## 🚀 Features

- 📥 Scheduled stock data ingestion from public APIs
- 🧪 Data transformation using AWS Lambda or Glue
- 🪣 Data lake architecture using Amazon S3
- 🔎 Query-ready data with Athena or DynamoDB
- 🔐 Fully managed permissions and roles
- 📈 Monitoring with CloudWatch
- 💻 Deployable using AWS CDK (Python)

---

## 🛠️ Tech Stack

- **AWS CDK (Python)**
- **Amazon S3**
- **AWS Lambda**
- **AWS Glue (optional)**
- **Amazon Athena or DynamoDB**
- **Amazon EventBridge**
- **Amazon CloudWatch**

---

## ✅ Setup Instructions

### 1. 📦 Install Prerequisites

- AWS CLI configured with credentials
- [Node.js](https://nodejs.org/) (for CDK CLI)
- Python 3.8+
- AWS CDK CLI

### 2. 🧱 Create a Virtual Environment

`python -m venv .venv
.venv\Scripts\activate`

### 3. 📦 Install Python Dependencies

`pip install -r requirements.txt`

### 4. 🏗️ Bootstrap Your AWS Environment (first time only)

`cdk bootstrap`

### 6. 🚀 Deploy the Stack

`cdk deploy`

---

## 📋 Trello Board

https://trello.com/b/OW6rRuEM/cloudquant
