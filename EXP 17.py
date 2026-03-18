import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating Multi-Dimensional Array: Rows = Stores, Columns = Months
sales_data = np.array([
    [200, 220, 250, 300, 280],  # Store A
    [180, 210, 240, 260, 270],  # Store B
    [220, 240, 260, 310, 300]   # Store C
])

ad_cost = np.array([
    [50, 60, 65, 80, 70],
    [45, 55, 60, 75, 65],
    [55, 65, 70, 85, 75]
])

stores = ["Store A", "Store B", "Store C"]
months = ["Jan", "Feb", "Mar", "Apr", "May"]

# Creating DataFrame
df_sales = pd.DataFrame(sales_data, index=stores, columns=months)
df_ads = pd.DataFrame(ad_cost, index=stores, columns=months)

print("Sales Data:\n", df_sales)
print("\nAdvertising Cost:\n", df_ads)

# Exploring Data
print("\nOverall Statistics:\n", df_sales.describe())

# Store-wise total sales
store_total = df_sales.sum(axis=1)
print("\nTotal Sales per Store:\n", store_total)

# Month-wise total sales
monthly_total = df_sales.sum(axis=0)
print("\nTotal Sales per Month:\n", monthly_total)

# Feature Engineering: Profit Calculation
profit = df_sales - df_ads

# Growth Rate Calculation (Month-wise % change)
growth_rate = df_sales.pct_change(axis=1) * 100

print("\nProfit:\n", profit)
print("\nGrowth Rate (%):\n", growth_rate)

# Advanced Filtering
# Find months where any store had sales > 300
high_performance = df_sales[df_sales > 300]
print("\nHigh Performance (Sales > 300):\n", high_performance)

# Identify underperforming store (lowest total)
underperforming_store = store_total.idxmin()
print("\nUnderperforming Store:", underperforming_store)

# Correlation Analysis
sales_flat = sales_data.flatten()
ads_flat = ad_cost.flatten()

correlation = np.corrcoef(sales_flat, ads_flat)[0, 1]
print("\nCorrelation between Sales and Ads:", correlation)

# Ranking
ranking = store_total.sort_values(ascending=False)
print("\nStore Ranking:\n", ranking)

# Visualization: Line Chart
plt.figure()

for i in range(len(stores)):
    plt.plot(months, sales_data[i], marker='o', label=stores[i])

plt.title("Store-wise Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()

# Visualization: Bar Chart
plt.figure()

plt.bar(months, monthly_total)

plt.title("Total Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()