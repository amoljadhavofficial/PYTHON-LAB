import pandas as pd

dataset = {
    "Name": ["Pratik","Pankaj","Sheetal","Gauri","Raghav","Pratik",None,"Pankaj","Neha","Yash"],
    "Age": [24,None,25,24,21,24,28,23,60,21],
    "City": ["Pune","Mumbai","Nagpur",None,"Surat","Pune","Chennai","Mumbai","Nagpur","Pune"],
    "Salary": [35000,40000,38000,None,42000,35000,39000,80000,47000,45000],
    "Department": ["IT","HR","Operations","Finance","HR","IT","Finance","R&D","HR","Marketing"]
}

df = pd.DataFrame(dataset)
print("The Actual dataset:\n", df)

print("The missing values:\n")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(round(df["Age"].mean(),0))
df["Salary"] = df["Salary"].fillna(round(df["Salary"].mean(),2))
df["Name"] = df["Name"].fillna(df["Name"].mode()[0])
df["City"] = df["City"].fillna(df["City"].mode()[0])

print("\nDataset after handling missing values:\n", df)

df.drop_duplicates(inplace=True)
print("\nDataset after dropping duplicates:\n", df)

df["Name"] = df["Name"].str.upper().str.strip()
df["City"] = df["City"].str.upper().str.strip()
df["Department"] = df["Department"].str.upper().str.strip()

print("\nDataset after formatting text:\n", df)

df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(int)

print("\nDataset after data type conversion:\n", df)

df["Salary"] = (df["Salary"] - df["Salary"].min()) / (df["Salary"].max() - df["Salary"].min())

print("\nDataset after feature scaling:\n", df)

df.to_csv("cleaned_dataset_exp8.csv", index=False)
print("\nCleaned Dataset:\n", df)