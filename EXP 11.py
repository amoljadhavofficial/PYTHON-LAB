import pandas as pd

# Creating Employee Dataset
emp_data = {
    "Employee": ["Amit", "Sneha", "Rohan", "Pooja", "Kiran", "Neha", "Vikas", "Anjali"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "IT"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Salary": [60000, 45000, 75000, 50000, 47000, 80000, 52000, 72000],
    "Performance": ["High", "Medium", "High", "Low", "Medium", "High", "Low", "Medium"]
}

df = pd.DataFrame(emp_data)

# Converting Columns to Categorical
df["Department"] = df["Department"].astype("category")
df["Gender"] = df["Gender"].astype("category")

# Ordered categorical data
performance_order = ["Low", "Medium", "High"]
df["Performance"] = pd.Categorical(
    df["Performance"],
    categories=performance_order,
    ordered=True
)

print("Employee Dataset:\n", df)

# Category Information
print("\nDepartment Categories:", df["Department"].cat.categories)
print("Performance Categories:", df["Performance"].cat.categories)

# GroupBy - Multiple Aggregations
dept_summary = df.groupby("Department", observed=True)["Salary"].agg(
    ["mean", "sum", "max", "min", "count"]
)
print("\nDepartment Salary Summary:\n", dept_summary)

# GroupBy with Multiple Columns
dept_gender_avg = df.groupby(
    ["Department", "Gender"], observed=True
)["Salary"].mean()
print("\nAverage Salary by Department and Gender:\n", dept_gender_avg)

# Using transform()
df["Dept_Avg_Salary"] = df.groupby(
    "Department", observed=True
)["Salary"].transform("mean")

print("\nEmployee Dataset with Department Average Salary:\n", df)

# Filtering Groups
high_salary_dept = df.groupby(
    "Department", observed=True
).filter(lambda x: x["Salary"].mean() > 50000)

print("\nDepartments with Avg Salary > 50000:\n", high_salary_dept)

# Performance Based Analysis
print("\nHighest Performance Level:", df["Performance"].max())