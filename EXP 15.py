import numpy as np
import matplotlib.pyplot as plt

# creating Numpy arrays
sales = np.array([100,125,150,200,250,300,275,350,450,325,400,500])

months = np.array([
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
])

print("The sales:", sales)
print("The Month:", months)

# Numpy functions
print("-----Numpy functions-----")

average_sales = np.average(sales)
print("The average sales is", round(average_sales,2))

max_sales = np.max(sales)
print("The maximum sales is", round(max_sales,2))

min_sales = np.min(sales)
print("The minimum sales is", round(min_sales,2))

# plotting line chart
plt.plot(months, sales, marker='o', linestyle='-', color='blue')

plt.title("Sales Performance")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)

# Labeling points
for i, value in enumerate(sales):
    plt.text(months[i], sales[i], value)

plt.show()


print("\n-----------Reshape and Product Sales-----------")

data = np.array([50, 60, 70, 80, 90, 100])

matrix = data.reshape(2,3)
print("\nReshaped Matrix:\n", matrix)

products = ["P1", "P2", "P3"]
product_sales = matrix[0]

plt.figure()
plt.bar(products, product_sales)

plt.title("Product Sales Bar Chart")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(axis='y')

for i, v in enumerate(product_sales):
    plt.text(i, v + 1, str(v), ha='center')

plt.show()


print("\n-----------Cumulative Sales Trend---------------")

weekly_sales = np.array([100, 150, 120, 170, 200])

cumulative_sales = np.cumsum(weekly_sales)
print("\nCumulative Sales:", cumulative_sales)

weeks = ["W1", "W2", "W3", "W4", "W5"]

plt.figure()
plt.plot(weeks, cumulative_sales, marker='o')

plt.title("Cumulative Sales Trend")
plt.xlabel("Weeks")
plt.ylabel("Cumulative Sales")
plt.grid(True)

plt.show()