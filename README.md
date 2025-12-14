� E‑Commerce Sales Analysis Using Python
🔍 Project Overview
This project presents an end‑to‑end data analysis workflow on an e‑commerce sales dataset using
Python.
It is designed as a portfolio‑ready, client‑friendly project that demonstrates practical skills in data
cleaning, exploratory data analysis (EDA), visualization, and basic machine learning.
All outputs (cleaned data, charts, and analysis reports) are generated automatically by running a single
Python script.
📁 Dataset Description
The dataset contains transactional e‑commerce data with the following key attributes: - Order ID and
order date - Product name, category, and brand - Sales platform (Amazon, Jumia, Souq) - City‑wise sales
information - Price, quantity, and total amount - Customer ratings and review counts
Source: Kaggle (E‑commerce sales dataset)
🛠 Tools & Technologies
• 
• 
• 
• 
• 
Python
Pandas – data cleaning & manipulation
Matplotlib / Seaborn – data visualization
Scikit‑learn – machine learning (sales prediction)
VS Code – development environment
⚙
️ Project Workflow
1. 
2. 
3. 
4. 
5. 
6. 
7. 
Load and inspect raw data
Clean and preprocess data
Perform exploratory data analysis (EDA)
Analyze sales by platform, category, and city
Create and save visualizations
Train a machine learning model for sales prediction
Export cleaned data and analysis reports
📊 Key Visualizations
The following visualizations are generated and saved automatically: - Total sales by platform 
Category‑wise revenue distribution - Monthly sales trend - Relationship between ratings and total sales
1
(All charts are saved inside the 
charts/ folder.)
🤖 Machine Learning Model
• 
• 
• 
• 
Model Used: Linear Regression 
Target Variable: Total Amount 
Features: Price, Quantity 
Objective: Predict sales revenue based on pricing and order size
📂 Project Structure
project/
│
├── data/
│   ├── raw_ecommerce_sales.csv
│   └── cleaned_ecommerce_sales.csv
│
├── charts/
│   ├── sales_by_platform.png
│   ├── sales_by_category.png
│   ├── monthly_sales_trend.png
│   └── rating_vs_sales.png
│
├── portfolio.py
├── analysis_output.txt
├── requirements.txt
└── README.md
▶
️ How to Run the Project
1
️
⃣ Install Dependencies
pip install-r requirements.txt
2
️
⃣ Run the Analysis Script
python portfolio.py
3
️
⃣ Generated Outputs
• 
• 
Cleaned dataset:
data/cleaned_ecommerce_sales.csv
Charts:
charts/ folder
2
Text report:
• 
analysis_output.txt
📈 Key Business Insights
• 
• 
• 
• 
Electronics contribute the highest share of total revenue
Sales performance varies significantly across platforms and cities
High customer ratings do not always translate to higher sales
Price and quantity are strong predictors of revenue
💼 Use Cases
• 
• 
• 
• 
Business sales performance analysis
Market and customer behavior insights
Freelance data analytics projects
Python data analysis portfolio demonstration
👤 Author
Python Data Analyst
Skills showcased: - Data Cleaning & EDA - Data Visualization - Machine Learning Basics 
Business‑focused Insights
⭐ Portfolio Note
This project demonstrates the ability to transform raw e‑commerce data into actionable insights
using Python and deliver professional, client‑ready analytics outputs.
🚀 Future Improvements
• 
• 
• 
Time‑series forecasting
Interactive dashboard (Streamlit / Power BI)
Advanced machine learning models
3# Ecommerce-sales-analysis-python
