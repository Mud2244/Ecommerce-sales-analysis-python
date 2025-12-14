
# ===============================
# E-COMMERCE SALES ANALYSIS
# Portfolio / Client-Ready Script
# ===============================

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# -------------------------------
# Setup folders
# -------------------------------
os.makedirs("data", exist_ok=True)
os.makedirs("charts", exist_ok=True)

# Save all printed output to a file
sys.stdout = open("analysis_output.txt", "w")

# -------------------------------
# Load Data
# -------------------------------
df = pd.read_csv("ecommerce_10000.csv")

print("Dataset Loaded Successfully")
print(df.head())
print("\nDataset Info:")
print(df.info())

# -------------------------------
# Data Cleaning
# -------------------------------
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
df.dropna(inplace=True)

# Save cleaned data
df.to_csv("data/cleaned_ecommerce_sales.csv", index=False)
print("\nCleaned data saved successfully")

# -------------------------------
# Exploratory Data Analysis
# -------------------------------

# Sales by Platform
df.groupby("Platform")["TotalAmount"].sum().plot(kind="bar", title="Total Sales by Platform")
plt.tight_layout()
plt.savefig("charts/sales_by_platform.png")
plt.close()

# Sales by Category
df.groupby("Category")["TotalAmount"].sum().plot(kind="bar", title="Sales by Category")
plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
plt.close()

# Monthly Sales Trend
df["Month"] = df["OrderDate"].dt.to_period("M")
df.groupby("Month")["TotalAmount"].sum().plot(title="Monthly Sales Trend")
plt.tight_layout()
plt.savefig("charts/monthly_sales_trend.png")
plt.close()

# Rating vs Sales
plt.scatter(df["Rating"], df["TotalAmount"])
plt.title("Rating vs Total Sales")
plt.xlabel("Rating")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.savefig("charts/rating_vs_sales.png")
plt.close()

print("\nVisualizations saved successfully")

# -------------------------------
# Machine Learning
# -------------------------------
X = df[["Price", "Quantity"]]
y = df["TotalAmount"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
score = r2_score(y_test, predictions)

print("\nMachine Learning Model Performance")
print("R2 Score:", round(score, 2))

print("\nProject execution completed successfully")

sys.stdout.close()
