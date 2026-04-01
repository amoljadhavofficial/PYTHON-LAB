import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataset
data = {
    "Student_ID": range(1, 21),
    "Study": ["Regular", "Regular", "Regular", "Regular", "Regular", "Regular", "Regular",
              "Regular", "Not Regular", "Not Regular", "Not Regular", "Not Regular",
              "Not Regular", "Not Regular", "Regular", "Regular", "Not Regular",
              "Regular", "Not Regular", "Regular"],
    "Marks": ["High", "High", "Low", "High", "High", "Low", "High", "High",
              "Low", "High", "Low", "Low", "High", "Low", "High", "Low",
              "Low", "High", "Low", "High"]
}

df = pd.DataFrame(data)

print(df.head(21))

# Count total students
total = len(df)

# Probabilities
P_R = len(df[df["Study"] == "Regular"]) / total

P_H_given_R = len(df[(df["Study"] == "Regular") & (df["Marks"] == "High")]) / \
              len(df[df["Study"] == "Regular"])

P_H_given_not_R = len(df[(df["Study"] == "Not Regular") & (df["Marks"] == "High")]) / \
                  len(df[df["Study"] == "Not Regular"])

# Total probability of High marks
P_H = len(df[df["Marks"] == "High"]) / total

# Apply Bayes Theorem
P_R_given_H = (P_H_given_R * P_R) / P_H

print("Probability student studies regularly given high marks - P(Regular | High Marks):",
      round(P_R_given_H, 2))

# Visualization
sns.countplot(data=df, x="Study", hue="Marks")
plt.title("Study Habit vs Marks Distribution")
plt.show()