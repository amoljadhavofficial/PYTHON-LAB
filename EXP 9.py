import pandas as pd

# To create employee dataset
data = {
    "Employee_Name": ["Raghav", "Nisha", "Amol", "Simran", "Karan", "Pooja", "Abhishek", "Anjali"],
    "Age": [25, 28, 30, 27, 35, 29, 32, 26],
    "Experience_Years": [2, 4, 6, 3, 10, 5, 7, 2],
    "Salary": [45000, 55000, 65000, 52000, 80000, 65000, 70000, 40000],
    "Working_Hours_per_Week": [40, 45, 50, 42, 48, 44, 46, 40],
    "Attendance_Percentage": [90, 95, 88, 92, 85, 93, 89, 91],
    "Performance_Score": [7, 8, 9, 7, 9, 8, 8, 7]
}

df = pd.DataFrame(data)

# Display dataset
print("Employee Dataset:\n")
print(df.to_string())

# Statistical Summary
print("\nThe statistics summary of dataset:\n")
print(df.describe().to_string())

print("\nAverage Salary:", df["Salary"].mean())
print("Maximum Salary:", df["Salary"].max())
print("Minimum Salary:", df["Salary"].min())

# Correlation Analysis
print("\nCorrelation Matrix:\n")
correlation_matrix = df.corr(numeric_only=True)
print(correlation_matrix.to_string())

print("\nRelationship between Experience and Salary:",
      df["Experience_Years"].corr(df["Salary"]))

print("Relationship between Attendance and Performance:",
      df["Attendance_Percentage"].corr(df["Performance_Score"]))

print("Relationship between Working Hours and Salary:",
      df["Working_Hours_per_Week"].corr(df["Salary"]))

# Categorize salary
df["Salary_Level"] = pd.cut(
    df["Salary"],
    bins=[0, 40000, 60000, 80000, 100000],
    labels=["Low", "Medium", "High", "Very High"]
)

print("\nEmployee Salary Category:\n")
print(df[["Employee_Name", "Salary", "Salary_Level"]])