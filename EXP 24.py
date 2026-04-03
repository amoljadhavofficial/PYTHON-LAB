import numpy as np # Generates random data
import pandas as pd # Handles dataset (table format)
import scipy.stats as stats # Performs statistical test (t-test)
import matplotlib.pyplot as plt # Visualization
import seaborn as sns #Visualization

# Create Dataset
np.random.seed(42)
n = 75
data = pd.DataFrame({
 "Student_ID": range(1, n + 1),
 "Study_Hours": np.random.randint(1, 6, n), # Assigns random study hours (1 to 5 hours)
})

# Generate marks (with slight effect of study)
# Base marks = 50, Study effect = +5 marks per hour, Noise = random variation (real-life uncertainty)
data["Marks"] = 50 + data["Study_Hours"] * 5 + np.random.normal(0, 10, n)

print("\nThe Dataset:\n", (round(data.head(10),2).to_string()))

# Create Groups: Compare performance between two groups
# Low Study Group: ≤ 2 hours
group_low = data[data["Study_Hours"] <= 2]["Marks"]

# High Study Group → ≥ 4 hours
group_high = data[data["Study_Hours"] >= 4]["Marks"]

# Hypothesis Testing: H0: No difference in marks, H1: High study students score higher
t_stat, p_value = stats.ttest_ind(group_low, group_high) # Independent t-test

print("\n ---- Result of Hypothesis Test-----")
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
 print("Result: Significant difference (Reject H0)")
else:
 print("Result: No significant difference (Fail to Reject H0)")

# Visualization
plt.figure(figsize=(8, 5))
sns.boxplot(x=data["Study_Hours"], y=data["Marks"])
plt.title("Marks vs Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# p-Hacking Concept
print("\n ---p-Hacking Concept----")
p_values = []

# multiple random subsets
for i in range(20):
 sample = data.sample(frac=0.5) # Takes random 50% samples multiple times (20 trials)
 g1 = sample[sample["Study_Hours"] <= 2]["Marks"]
 g2 = sample[sample["Study_Hours"] >= 4]["Marks"]

 if len(g1) > 5 and len(g2) > 5:
  _, p = stats.ttest_ind(g1, g2)
  p_values.append(p)
  print(f"Trial {i + 1}: p-value = {p}")

# Check if any false significant result appears
significant = [p for p in p_values if p < 0.05]
print("\nNumber of significant p-values found:", len(significant))

# Plotting of p-values
plt.figure(figsize=(8, 5))
plt.hist(p_values, bins=10)
plt.axvline(0.05)
plt.title("Distribution of p-values (p-hacking effect)")
plt.xlabel("p-value")
plt.ylabel("Frequency")
plt.show()