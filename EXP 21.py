import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create Healthcare Dataset
data = {
    "Patient": range(1, 11),
    "Diabetes": ["Yes","Yes","No","Yes","No","Yes","No","Yes","No","Yes"],
    "Heart_Disease": ["Yes","No","No","Yes","No","Yes","No","Yes","Yes","Yes"]
}

df = pd.DataFrame(data)

print("Healthcare Dataset:\n", df)

# Total Patients
total = len(df)

# Event A: Diabetes
A = df[df["Diabetes"] == "Yes"]
P_A = len(A) / total

# Event B: Heart Disease
B = df[df["Heart_Disease"] == "Yes"]
P_B = len(B) / total

# Intersection A ∩ B
A_and_B = df[(df["Diabetes"] == "Yes") & (df["Heart_Disease"] == "Yes")]
P_A_and_B = len(A_and_B) / total

print("\nP(A) [Diabetes]:", P_A)
print("P(B) [Heart Disease]:", P_B)
print("P(A ∩ B):", P_A_and_B)

# Conditional Probability
P_A_given_B = P_A_and_B / P_B
print("\nP(A | B):", round(P_A_given_B, 2))

# Check Independence
if P_A_and_B == P_A * P_B:
    print("\nEvents are Independent")
else:
    print("\nEvents are Dependent")

# Create cross-tab
ct = pd.crosstab(df["Diabetes"], df["Heart_Disease"])

sns.heatmap(ct, annot=True, cmap="coolwarm")
plt.title("Diabetes vs Heart Disease")
plt.show()