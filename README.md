# 🇿🇦 SA Consumer Inflation & Welfare Loss Calculator

A policy-grade microeconomic analytics platform that measures how inflation affects South African households across income groups and estimates welfare losses using household expenditure and CPI data.

This project applies welfare economics, cost-of-living theory, and distributional analysis to quantify inflation inequality and simulate targeted policy interventions.

---

## 🎯 Objectives

- Calculate household-specific inflation rates
- Estimate welfare losses using compensating variation
- Measure inflation inequality across income deciles
- Simulate policy interventions (subsidies, VAT cuts, price shocks)
- Visualise results via an interactive Streamlit dashboard

---

## 🧠 Economic Framework

This project implements:
- Household-specific CPI
- Cost-of-living indices
- Compensating variation (CV)
- Inflation inequality metrics
- Distributional welfare analysis

---

## 📊 Data Sources (South Africa)

| Dataset | Source |
|--------|--------|
| Household Expenditure Survey (HIES) | Statistics South Africa |
| CPI by Category | Statistics South Africa |
| Income Data | Synthetic / Survey-based |

---

## 📁 Repository Structure
sa-consumer-inflation-welfare-loss/
│
├── data/
│   ├── raw/
│   │   ├── sa_household_expenditure.csv
│   │   ├── sa_cpi_by_category.csv
│   │   └── sa_household_income.csv
│   └── processed/
│       └── master_dataset.csv
│
├── src/
│   ├── data_loader.py
│   ├── inflation_engine.py
│   ├── welfare_calculator.py
│   ├── inequality_metrics.py
│   ├── policy_simulator.py
│   └── utils.py
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE

---
## 🖥️ Dashboard Pages

- **Overview:** Inflation by decile, inequality, total welfare loss
- **Household Impact:** Distribution of household inflation and CV
- **Category Exposure:** CPI contribution by category and income group
- **Policy Simulator:** VAT cuts, subsidies, and inflation shock scenarios
---

## 🚀 How to Run
1. Clone the repo:
```bash
git clone https://github.com/yourusername/sa-consumer-inflation-welfare-loss.git
cd sa-consumer-inflation-welfare-loss
