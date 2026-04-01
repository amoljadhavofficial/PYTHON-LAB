import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Create LIC Dataset
data = {
    "Customer_ID": [2601,2602,2603,2604,2605,2606,2607,2608,2609,2610],
    "Age": [25,30,35,40,28,50,45,32,38,29],
    "Annual_Income": [300000,400000,500000,600000,350000,800000,750000,450000,520000,380000],
    "Premium": [15000,20000,25000,30000,18000,40000,38000,22000,26000,19000],
    "Policy_Term": [10,15,20,25,15,30,16,21,25,15]
}

df = pd.DataFrame(data)
print("\nDataset:\n", df)

# Customer Segmentation
def segment_customer(row):
    if row["Annual_Income"] > 600000:
        return "High Value"
    elif row["Annual_Income"] > 400000:
        return "Medium Value"
    else:
        return "Low Value"

df["Segment"] = df.apply(segment_customer, axis=1)

# Age Group Classification
def age_group(age):
    if age < 30:
        return "Young"
    elif age < 45:
        return "Middle Age"
    else:
        return "Senior"

df["Age_Group"] = df["Age"].apply(age_group)

# Strategy Generation
def generate_strategy(row):
    if row["Segment"] == "High Value":
        return "Premium Plans"
    elif row["Segment"] == "Medium Value":
        return "Savings Plans"
    else:
        return "Low-cost Plans"

df["Strategy_Type"] = df.apply(generate_strategy, axis=1)

# Display Data
print("\nSegmented Data:\n", df.to_string())

# Visualization

# Scatter Plot
plt.figure()
sns.scatterplot(
    x="Annual_Income",
    y="Premium",
    hue="Segment",
    style="Age_Group",
    data=df,
    s=100
)
plt.title("Income vs Premium (Segment-wise)")
plt.show()

# Regression Plot
plt.figure()
sns.regplot(x="Annual_Income", y="Premium", data=df)
plt.title("Regression: Income vs Premium")
plt.show()

# Boxplot
plt.figure()
sns.boxplot(x="Segment", y="Premium", data=df)
plt.title("Premium Distribution by Segment")
plt.show()

# Bar Plot
plt.figure()
avg_premium = df.groupby("Segment")["Premium"].mean().reset_index()
sns.barplot(x="Segment", y="Premium", data=avg_premium)
plt.title("Average Premium by Segment")
plt.show()

# Heatmap
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Pair Plot
sns.pairplot(df, hue="Segment")
plt.show()

# Business insights
print("\n---Business insights---")
print("\nAverage Premium by Segment:\n",
      df.groupby("Segment")["Premium"].mean())

print("\nAverage Policy Term by Age Group:\n",
      df.groupby("Age_Group")["Policy_Term"].mean())

# Final Strategy Output
print("\n---Marketing Strategy---\n")
print(df[["Customer_ID", "Segment", "Age_Group", "Strategy_Type"]])