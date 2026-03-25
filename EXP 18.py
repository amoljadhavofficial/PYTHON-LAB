import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

months = pd.date_range(start="2025-01-01", periods=12, freq='ME')

sales = [100, 120, 130, 150, 170, 200, 220, 210, 230, 250, 270, 300]

df = pd.DataFrame({
    'Date': months,
    'Sales': sales
})

df.set_index('Date', inplace=True)

print(df)

plt.figure()
plt.plot(df.index, df['Sales'])
plt.title("Monthly Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid()
plt.show()

df['Moving_Avg'] = df['Sales'].rolling(window=3).mean()

plt.figure()
plt.plot(df['Sales'], label="Original Sales")
plt.plot(df['Moving_Avg'], linestyle='--', label="Moving Average")
plt.title("Trend using Moving Average")
plt.legend()
plt.grid()
plt.show()

growth = df['Sales'].iloc[-1] - df['Sales'].iloc[-2]

next_month_sales = df['Sales'].iloc[-1] + growth

print("Predicted Sales for Next Month:", next_month_sales)