import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Create Retail Sales Dataset (Case Study)
data = {
 "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
 "Sales": [200, 220, 250, 300, 320, 350, 370, 400, 420, 450, 480, 500],
 "Ad_Spend": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
 "Footfall": [150, 160, 180, 200, 220, 240, 260, 280, 300, 320, 350, 370],
 "Discount": [5, 7, 10, 10, 12, 15, 15, 18, 20, 20, 22, 25]
}
# Convert into DataFrame
df = pd.DataFrame(data)
# Display dataset
print("Dataset:\n", df)
# Statistical Analysis
print("\nStatistical Summary:\n")
print(df.describe())
# Mean
print("\nMean Values:\n", df.mean(numeric_only=True))
# Median
print("\nMedian Values:\n", df.median(numeric_only=True))
# Standard Deviation
print("\nStandard Deviation:\n", df.std(numeric_only=True))
# Correlation Analysis
print("\nCorrelation Matrix:")
correlation = df.corr(numeric_only=True)
print(correlation)
# Visualization: Line Plot (Sales Trend)
plt.figure()
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()
# Scatter Plot : Ad Spend vs Sales
plt.figure()
plt.scatter(df["Ad_Spend"], df["Sales"])
plt.title("Ad Spend vs Sales")
plt.xlabel("Advertising Spend")
plt.ylabel("Sales")
plt.show()
# Scatter Plot (Footfall vs Sales)
plt.figure()
plt.scatter(df["Footfall"], df["Sales"])
plt.title("Footfall vs Sales")
plt.xlabel("Customer Footfall")
plt.ylabel("Sales")
plt.show()
# Heatmap
plt.figure()
sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.show()
