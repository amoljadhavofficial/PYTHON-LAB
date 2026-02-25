import pandas as pd
employee = pd.DataFrame({
    "Emp_ID": [101,102,103,104],
    "Name": ["TEJAS","VIJAY","AYUSH","ANKITA"],
    "Department": ["IT","HR","Finance","IT"]
})

print("Employee Data")
print(employee)

salary = pd.DataFrame({
    "Emp_ID": [101,102,103,104],
    "Salary": [40000,35000,45000,42000]
})

print("\nSalary Data")
print(salary)

print("\nJoin Operation")

joined_data = pd.merge(employee, salary, on="Emp_ID")

print(joined_data)

data1 = pd.DataFrame({
    "Name": ["TEJAS","VIJAY"],
    "Age": [25,28]
})

data2 = pd.DataFrame({
    "Name": ["AYUSH","ANKITA"],
    "Age": [30,27]
})

vertical = pd.concat([data1, data2])

print("\nVertical Combine")
print(vertical)

horizontal = pd.concat([data1, data2], axis=1)

print("\nHorizontal Combine")
print(horizontal)

marks = pd.DataFrame({
    "Name": ["TEJAS","TEJAS","VIJAY","VIJAY"],
    "Subject": ["Math","Science","Math","Science"],
    "Marks": [85,90,78,88]
})

print("\nOriginal Data")
print(marks)

pivot_table = marks.pivot(index="Name",
                          columns="Subject",
                          values="Marks")

print("\nPivot Table")
print(pivot_table)

melted = pd.melt(pivot_table.reset_index(),
                 var_name="Subject",
                 id_vars="Name",
                 value_name="Marks")

print("\nMelted Data")
print(melted)


print("\nStacked Data")
print(pivot_table.stack())

print("\nUnstacked Data")
print(pivot_table.stack().unstack())
