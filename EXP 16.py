import numpy as np

# Loading data from storage file
data = np.genfromtxt("patients.csv", delimiter=",", skip_header=1)

# Extract columns
patient_id = data[:, 0]
age = data[:, 1]
bp = data[:, 2]
cholesterol = data[:, 3]
sugar = data[:, 4]

# Calculate Health Risk Score
risk_score = bp + cholesterol + sugar

print("Patient Health Risk Scores:\n")
for i in range(len(patient_id)):
    print("Patient ID:", int(patient_id[i]), "Score:", risk_score[i])

# Classification
print("\nPatient Risk Classification:\n")
risk_category = []

for score in risk_score:
    if score < 350:
        risk_category.append("Low Risk")
    elif score < 450:
        risk_category.append("Medium Risk")
    else:
        risk_category.append("High Risk")

for i in range(len(patient_id)):
    print("Patient", int(patient_id[i]), ":", risk_category[i])

# Simple Clustering
print("\nClustering Patients based on BP similarity:\n")

cluster1 = []
cluster2 = []

mean_bp = np.mean(bp)

for i in range(len(bp)):
    if bp[i] < mean_bp:
        cluster1.append(int(patient_id[i]))
    else:
        cluster2.append(int(patient_id[i]))

print("Cluster 1 (Lower BP Patients):", cluster1)
print("Cluster 2 (Higher BP Patients):", cluster2)

# Summary Statistics
print("\nStatistical Analysis")
print("Average Age:", np.mean(age))
print("Average BP:", np.mean(bp))
print("Maximum Cholesterol:", np.max(cholesterol))
print("Minimum Sugar Level:", np.min(sugar))