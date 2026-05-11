# 🎯 Customer Segmentation & RFM Analysis

<div align="center">

# 📊 Customer Segmentation Dashboard

### Using RFM Analysis to Understand Customer Behavior & Drive Business Growth

**Author:** Rehana Hassan Muhumed  
**Program:** IBM Data Analyst Professional Certificate  
**Date:** May 2026  

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0-green.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.26-orange.svg)](https://numpy.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.18-purple.svg)](https://plotly.com/)
[![Dash](https://img.shields.io/badge/Dash-2.14-red.svg)](https://dash.plotly.com/)
[![Render](https://img.shields.io/badge/Render-Deployed-brightgreen.svg)](https://render.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black.svg)](https://github.com/rihhanna)

---

### 🌐 Live Dashboard

## 🚀 [Open Interactive Dashboard](https://customer-segmentation-dashboard-qjhp.onrender.com)

> No installation required — open the dashboard and explore customer insights instantly.

</div>

---

# 📌 Project Overview

This project focuses on **Customer Segmentation using RFM Analysis** — a powerful marketing technique used by businesses to identify their most valuable customers and improve customer retention strategies.

The dashboard analyzes customer purchasing behavior based on:

| Metric | Meaning | Business Importance |
|--------|----------|---------------------|
| 🔵 **Recency** | How recently a customer purchased | Recent customers are more likely to buy again |
| 🟢 **Frequency** | How often a customer purchases | Frequent customers are usually loyal |
| 🟡 **Monetary** | How much money a customer spends | High spenders generate more revenue |

By combining these three metrics, customers are grouped into meaningful business segments such as VIP customers, loyal customers, at-risk customers, and new customers.

---

# 🎯 Project Objectives

✔ Analyze customer purchasing behavior  
✔ Perform RFM calculations using Python  
✔ Create meaningful customer segments  
✔ Build interactive visual dashboards using Plotly & Dash  
✔ Provide business recommendations for each segment  
✔ Deploy the dashboard online using Render  

---

# 🛠️ Tools & Technologies

| Technology | Purpose |
|------------|---------|
| **Python 3.13** | Core programming language |
| **Pandas** | Data cleaning and manipulation |
| **NumPy** | Numerical calculations |
| **Matplotlib** | Static charts |
| **Seaborn** | Data visualization |
| **Plotly** | Interactive visualizations |
| **Dash** | Web dashboard framework |
| **Jupyter Notebook** | Analysis environment |
| **Render** | Cloud deployment |
| **Git & GitHub** | Version control and portfolio hosting |

---

# 📂 Project Structure

```bash
customer-segmentation/
│
├── 📁 dashboard/
│   ├── app.py
│   ├── customer_data.csv
│   └── requirements.txt
│
├── 📁 data/
│   ├── online_retail_II.xlsx
│   └── rfm_data.csv
│
├── 📁 images/
│   ├── segment_distribution.png
│   └── segment_profiles.png
│
├── 📁 notebooks/
│   └── 01_rfm_analysis.ipynb
│
├── 📁 reports/
│   └── segmentation_report.txt
│
├── 📄 README.md
├── 📄 render.yaml
├── 📄 requirements.txt
└── 📄 runtime.txt
```

---

# 📊 Customer Segments

| Segment | Description | Customer Share | Recommended Action |
|---------|-------------|----------------|--------------------|
| 🔴 **VIP Customers** | High spenders who buy frequently and recently | 15% | Loyalty rewards & premium support |
| 🟠 **Loyal Customers** | Consistent repeat buyers | 25% | Referral and cross-sell campaigns |
| 🟡 **At-Risk Customers** | Previously active but inactive recently | 35% | Re-engagement campaigns |
| 🟢 **New Customers** | Recently joined customers | 25% | Welcome and onboarding series |
| 🔵 **Regular Customers** | Average purchasing behavior | — | Nurture campaigns |
| ⚫ **Inactive Customers** | No purchases for a long time | — | Win-back promotions |

---

# 📈 Dashboard Features

| Feature | Description |
|---------|-------------|
| 📌 Segment Filter | Filter dashboard by customer segment |
| 💰 Monetary Slider | Filter customers by spending amount |
| 📊 KPI Cards | Revenue, customers, orders, recency |
| 🔵 Scatter Plot | Recency vs Monetary analysis |
| 🥧 Pie Chart | Segment distribution |
| 📉 Bar Charts | Compare segment metrics |
| 💡 Recommendations | Segment-specific business actions |
| 📋 Data Table | Explore customer records |
| ⬇ Download Button | Export filtered data to CSV |

---

# 📊 Key Business Insights

## 📌 Segment Distribution

```text
VIP Customers      → 15%
Loyal Customers    → 25%
At-Risk Customers  → 35%
New Customers      → 25%
```

## 📌 Important Findings

- VIP customers generate the highest revenue despite being a smaller group.
- At-Risk customers represent the largest percentage and require immediate attention.
- Loyal customers have strong repeat purchase behavior.
- New customers need onboarding campaigns to increase retention.

---

# 💡 Business Recommendations

## 🔴 VIP Customers

High-value customers should receive premium experiences.

### Recommended Strategies
- Offer exclusive loyalty rewards
- Provide early access to new products
- Send personalized thank-you messages
- Create VIP memberships with free shipping
- Invite customers to beta testing and surveys

---

## 🟠 Loyal Customers

Loyal customers help maintain consistent revenue.

### Recommended Strategies
- Launch referral programs
- Provide cross-selling recommendations
- Reward repeat purchases with points
- Offer personalized promotions

---

## 🟡 At-Risk Customers

These customers were active before but may stop purchasing.

### Recommended Strategies
- Send re-engagement emails
- Offer special discounts (20–30%)
- Run “We Miss You” campaigns
- Remind them about unused rewards

---

## 🟢 New Customers

New customers need onboarding and education.

### Recommended Strategies
- Send welcome email sequences
- Provide first-purchase discounts
- Share tutorials and product guides
- Ask for reviews after purchase

---

# 📸 Dashboard Preview

## 📊 Interactive Dashboard

![Dashboard Preview](images/segment_distribution.png)

---

## 📈 Segment Profiles

![Segment Profiles](images/segment_profiles.png)

---

# 📄 Sample Analysis Report

```text
========================================
     CUSTOMER SEGMENTATION REPORT
========================================

Analysis Date: 2026-04-28
Total Customers Analyzed: 5,000

========================================
SEGMENT SUMMARY
========================================

VIP Customers:
   - Count: 750 customers (15.0%)
   - Average Recency: 15 days
   - Average Frequency: 12.5 purchases
   - Average Monetary: $2,500

Loyal Customers:
   - Count: 1,250 customers (25.0%)
   - Average Recency: 30 days
   - Average Frequency: 6.2 purchases
   - Average Monetary: $1,200

At-Risk Customers:
   - Count: 1,750 customers (35.0%)
   - Average Recency: 90 days
   - Average Frequency: 8.0 purchases
   - Average Monetary: $800

========================================
END OF REPORT
========================================
```

---

# ⚙️ Installation & Setup

## 📌 Prerequisites

Before running the project locally, install:

- Python 3.13+
- Jupyter Notebook
- Git (optional)

---

## 🚀 Run the Project Locally

```bash
# 1. Clone repository
git clone https://github.com/rihhanna/customer-segmentation.git

# 2. Enter project folder
cd customer-segmentation

# 3. Install dependencies
pip install pandas numpy matplotlib seaborn plotly dash

# 4. Run Jupyter Notebook
jupyter notebook notebooks/01_rfm_analysis.ipynb

# 5. Launch Dashboard
cd dashboard
python app.py
```

---

## 🌐 Open Dashboard

```text
http://127.0.0.1:8050
```

---

# 🚀 Deployment

The dashboard is deployed using **Render.com** free cloud hosting.

## 🌐 Live Deployment

### 🔗 https://customer-segmentation-dashboard-qjhp.onrender.com

---

## 📄 render.yaml

```yaml
services:
  - type: web
    name: customer-segmentation-dashboard
    runtime: python
    rootDir: dashboard
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:server
```

---

# 📚 Related Portfolio Projects

| Project | Description |
|---------|-------------|
| 📊 Telco Customer Churn Analysis | Customer churn prediction project |
| 📈 Sales Performance Dashboard | Interactive sales analytics dashboard |
| 🦠 COVID-19 Data Pipeline | ETL and analytics pipeline |
| 🎯 Customer Segmentation | RFM customer analysis dashboard |

---

# 👩‍💻 About the Author

<div align="center">

## Rehana Hassan Muhumed

### Data Analyst | Software Engineering Student | Dashboard Developer

</div>

| Information | Details |
|------------|---------|
| 🎓 Program | IBM Data Analyst Professional Certificate |
| 💼 Focus | Data Analytics & Visualization |
| 🌍 Location | Somalia |
| 💻 GitHub | https://github.com/rihhanna |
| 🔗 LinkedIn | https://linkedin.com/in/rehana-hassan |
| 📚 Interests | Data Analytics, Dashboards, Machine Learning |

---

# 🙏 Acknowledgments

Special thanks to:

- **IBM** for the Data Analyst learning path
- **Open Source Community** for amazing Python libraries
- **Render** for free deployment services
- **Plotly & Dash** for interactive visualizations

---

# 📅 Project Timeline

| Phase | Status |
|-------|--------|
| ✅ Data Collection | Complete |
| ✅ Data Cleaning | Complete |
| ✅ RFM Analysis | Complete |
| ✅ Customer Segmentation | Complete |
| ✅ Dashboard Development | Complete |
| ✅ Deployment | Complete |
| ✅ Documentation | Complete |

---

# ⭐ Support This Project

If you found this project useful:

- ⭐ Star the repository on GitHub
- 🔗 Share the dashboard with others
- 💬 Provide feedback and suggestions
- 🤝 Connect with me on LinkedIn

---

<div align="center">

# ❤️ Built with Passion by Rehana Hassan Muhumed

### “Turning customer data into actionable business insights.”

</div>
