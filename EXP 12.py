import pandas as pd   # for DataFrame handling
import numpy as np    # for generating random data

# Create Dataset : Ice Cream Company Sales Dataset
# Every time you run the program, you get the same random dataset
np.random.seed(10)

dates = pd.date_range("2024-01-01", periods=24, freq="ME")

data = {
    "Date": np.repeat(dates, 4),
    "Region": ["North", "South", "East", "West"] * 24,
    "Flavor": np.random.choice(["Vanilla", "Chocolate", "Strawberry", "Mango"], 96),
    "Units_Sold": np.random.randint(400, 1000, 96),
    "Price": np.random.randint(20, 35, 96),
    "Cost": np.random.randint(10, 18, 96),
    "Discount": np.random.choice([0, 5, 10], 96)
}

df = pd.DataFrame(data)

print(df)
print("--------------------------------------")
print("Shape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Feature Engineering
df["Effective_Price"] = df["Price"] - df["Discount"]
df["Revenue"] = df["Units_Sold"] * df["Effective_Price"]
df["Total_Cost"] = df["Units_Sold"] * df["Cost"]
df["Profit"] = df["Revenue"] - df["Total_Cost"]

# Handle Missing Values (Simulate Missing Data)
df.loc[5, "Units_Sold"] = np.nan
df["Units_Sold"] = df["Units_Sold"].fillna(df["Units_Sold"].mean())

# MultiIndex
df.set_index(["Region", "Flavor"], inplace=True)

# Multi-level Grouping
region_profit = df.groupby(level="Region")["Profit"].sum()
flavor_growth = df.groupby(level="Flavor")["Revenue"].pct_change().mean()

# Pivot Table (Dashboard)
pivot = pd.pivot_table(df,
                       values="Profit",
                       index="Region",
                       columns="Flavor",
                       aggfunc="sum")

# Time-Series Analysis
df_reset = df.reset_index()
df_reset.set_index("Date", inplace=True)

monthly_revenue = df_reset["Revenue"].resample("ME").sum()
growth_rate = monthly_revenue.pct_change()

# Rolling Average (Trend Analysis)
rolling_avg = monthly_revenue.rolling(window=3).mean()

# Detect Outliers (Z-score Method)
df_reset["Z_score"] = (df_reset["Profit"] - df_reset["Profit"].mean()) / df_reset["Profit"].std()
outliers = df_reset[df_reset["Z_score"].abs() > 2]

# Rank Regions by Profit
ranking = region_profit.rank(ascending=False)

print("Region Profit:\n", region_profit)
print("\nRegion Ranking:\n", ranking)
print("\nPivot Table:\n", pivot)
print("\nMonthly Growth Rate:\n", growth_rate)
print("\nOutliers:\n", outliers.head())