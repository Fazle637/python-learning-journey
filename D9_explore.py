import pandas as pd
import numpy as np

# Generate students.CSV
np.random.seed(7)
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank",
         "Grace", "Heidi", "Isla", "Jack", "Kate", "Liam", "Mia", "Noah", "Olivia"]

rows = ["name,age,maths,english,science,hours_studied,passed"]
for name in names:
    age = np.random.randint(18, 24)
    m = int(np.clip(np.random.normal(68,15), 20, 100))
    e = int(np.clip(np.random.normal(70,12), 20, 100))
    s = int(np.clip(np.random.normal(65,10), 20, 100))
    hrs = round(np.random.uniform(1,10), 1)
    avg = (m + e + s) / 3
    p = "True" if avg >= 60 else "False"
    rows.append(f"{name}, {age}, {m}, {e}, {s}, {hrs}, {p}")

with open("students.csv", "w") as f:
    f.write("\n".join(rows))

#Load and explore
df = pd.read_csv("students.csv")

# Always run these 4 first
print(df.shape)
print(df.info())
print(df.head())
print(df.describe().round(2))

# Add computed columns
df["average"] = ((df["maths"] + df["english"] + df["science"]) / 3).round(2)

conditions = [df["average"]>=90, df["average"]>=80, df["average"]>=70, df["average"]>=60]
choices = ["A", "B", "C", "D"]
df["grade"] = np.select(conditions, choices, default="F")

print(df[["name", "average", "grade"]])

struggling = df[df["average"] < 60]
print(f"Struggling: {len(struggling)}")
print(struggling[["name", "average", "hours_studied"]])

#Aggregations
print(f"Class mean: {df['average'].mean():.2f}")
print(f"Class median: {df['average'].median():.2f}")
print(df.groupby("grade")["hours_studied"].mean().round(2))

for subj in ["maths", "english", "science"]:
    print(f" {subj:10} {df[subj].mean():.1f}")

