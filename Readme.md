# 🏦 Retail Lending Risk Intelligence System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Data-Pandas-orange)
![MySQL](https://img.shields.io/badge/Database-MySQL-blue)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📌 Overview

An **end-to-end data analytics project** that analyzes retail lending data to identify **loan default risks**, generate **business insights**, and build a **visual risk dashboard**.

This project simulates how financial institutions:

* Detect high-risk customers
* Monitor loan performance
* Reduce non-performing assets (NPAs)

---

## 🎯 Key Objectives

* Analyze factors influencing loan defaults
* Identify high-risk customer segments
* Measure financial stress using EMI-to-income ratio
* Provide actionable insights for decision-making

---

## 🏗️ Project Architecture

```text
Data → Cleaning → Feature Engineering → EDA → Visualization → Database → Insights
```

---

## 📂 Project Structure

```text
loan-risk-analysis/
│
├── data/
│   └── RetailLendingRiskIntelligence.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── eda.py
│   ├── visualization.py
│   ├── database.py
│   └── insights.py
│
├── loan_risk_analysis_dashboard.png
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Features

✔️ Data Cleaning & Preprocessing

✔️ Feature Engineering (EMI Ratio, Risk Flags)

✔️ Exploratory Data Analysis (EDA)

✔️ Risk Visualization Dashboard

✔️ MySQL Database Integration

✔️ Business Insights Generation

---

## 📊 Dashboard

![Loan Risk Dashboard](loan_risk_analysis_dashboard.png)

### Insights from Dashboard:

* 📌 Auto loans show relatively higher default rates
* 📌 Medium & High credit score groups still carry risk
* 📌 High EMI-to-income ratio strongly correlates with defaults
* 📌 Certain regions exhibit consistently higher NPAs

---

## 🛠️ Tech Stack

| Category       | Tools Used    |
| -------------- | ------------- |
| Language       | Python        |
| Data Analysis  | Pandas        |
| Visualization  | Matplotlib    |
| Database       | MySQL         |
| ORM            | SQLAlchemy    |
| Env Management | python-dotenv |

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
DB_URL=mysql+mysqlconnector://username:password@localhost/database_name
```

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/loan-risk-analysis.git
cd loan-risk-analysis
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Environment Variables

Create `.env` file and add your database credentials

### 4️⃣ Run Project

```bash
python main.py
```

---

## 📈 Output

* 📊 Loan Risk Dashboard
* 📉 Default Rate Analysis
* 🧠 Risk Segmentation
* 🗄️ Data Stored in MySQL

---

## 🔍 Key Business Insights

* High EMI-to-income ratio (>0.5) significantly increases default probability
* Low credit score customers are major contributors to NPAs
* Unsecured loans (Personal Loans, Credit Cards) carry higher risk
* Regional trends highlight localized financial risk patterns

---

## 🚀 Future Enhancements

* 🤖 Machine Learning model for default prediction
* 📊 Interactive dashboard (Streamlit / Power BI)
* ☁️ Cloud deployment (AWS / Azure)
* 🔄 Automated data pipeline

---

## 📬 Connect With Me

<p align="center">
  <a href="https://www.linkedin.com/in/varun-sai-kedarisetty-bb86bb23b/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Visit%20Profile-blue?style=for-the-badge&logo=linkedin" />
  </a>
</p>

---

