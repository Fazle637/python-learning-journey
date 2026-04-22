## ✅ `day9_challenge.py`
import os
import numpy as np
import pandas as pd

CSV_FILE = "employees.csv"

# ------------------------------------------------------------
# 1) Create employees.csv with at least 12 rows
# Columns: name, department, salary, years_exp, rating, promoted
# Departments: Engineering, Marketing, Sales
# ------------------------------------------------------------
data = [
    # Engineering
    {"name": "Amit Rahman", "department": "Engineering", "salary": 35000, "years_exp": 2, "rating": 3.8, "promoted": "No"},
    {"name": "Sadia Khan", "department": "Engineering", "salary": 55000, "years_exp": 5, "rating": 4.3, "promoted": "Yes"},
    {"name": "Rafi Ahmed", "department": "Engineering", "salary": 72000, "years_exp": 7, "rating": 4.6, "promoted": "Yes"},
    {"name": "Nabila Islam", "department": "Engineering", "salary": 48000, "years_exp": 4, "rating": 4.1, "promoted": "No"},
    {"name": "Tanvir Hossain", "department": "Engineering", "salary": 82000, "years_exp": 9, "rating": 4.8, "promoted": "Yes"},

    # Marketing
    {"name": "Mina Akter", "department": "Marketing", "salary": 32000, "years_exp": 1, "rating": 3.5, "promoted": "No"},
    {"name": "Farhan Karim", "department": "Marketing", "salary": 46000, "years_exp": 4, "rating": 4.0, "promoted": "No"},
    {"name": "Rina Chowdhury", "department": "Marketing", "salary": 62000, "years_exp": 6, "rating": 4.4, "promoted": "Yes"},
    {"name": "Shakil Mahmud", "department": "Marketing", "salary": 54000, "years_exp": 5, "rating": 4.2, "promoted": "Yes"},
    {"name": "Tania Sultana", "department": "Marketing", "salary": 38000, "years_exp": 3, "rating": 3.9, "promoted": "No"},

    # Sales
    {"name": "Jamil Hasan", "department": "Sales", "salary": 30000, "years_exp": 1, "rating": 3.6, "promoted": "No"},
    {"name": "Lamia Begum", "department": "Sales", "salary": 50000, "years_exp": 5, "rating": 4.3, "promoted": "Yes"},
    {"name": "Imran Ali", "department": "Sales", "salary": 75000, "years_exp": 8, "rating": 4.7, "promoted": "Yes"},
    {"name": "Sabrina Hossain", "department": "Sales", "salary": 42000, "years_exp": 4, "rating": 4.1, "promoted": "No"},
    {"name": "Kamal Uddin", "department": "Sales", "salary": 68000, "years_exp": 7, "rating": 4.5, "promoted": "Yes"},
]

df = pd.DataFrame(data)
df.to_csv(CSV_FILE, index=False)
print(f"✅ Created {CSV_FILE} with {len(df)} rows.\n")

# ------------------------------------------------------------
# 2) Load it, run all 4 first-look commands
# ------------------------------------------------------------
print("📥 Loading CSV...")
df = pd.read_csv(CSV_FILE)

print("\n🔎 head():")
print(df.head())

print("\n🔎 info():")
df.info()

print("\n🔎 describe():")
print(df.describe())

print("\n🔎 shape:")
print(df.shape)

# ------------------------------------------------------------
# 3) Add salary_band column using np.select()
#    "Junior" (<40k), "Mid" (40–70k), "Senior" (>70k)
# ------------------------------------------------------------
conditions = [
    df["salary"] < 40000,
    (df["salary"] >= 40000) & (df["salary"] <= 70000),
    df["salary"] > 70000
]
choices = ["Junior", "Mid", "Senior"]

df["salary_band"] = np.select(conditions, choices, default="Unknown")

print("\n✅ salary_band added:")
print(df[["name", "salary", "salary_band"]].head())

# ------------------------------------------------------------
# 4) Use groupby("department") to get mean salary and mean rating per department
# ------------------------------------------------------------
dept_stats = df.groupby("department", as_index=False).agg(
    mean_salary=("salary", "mean"),
    mean_rating=("rating", "mean")
)

print("\n📊 Mean salary & mean rating by department:")
print(dept_stats.round(2))

# ------------------------------------------------------------
# 5) Filter: rating >= 4.0 AND years_exp > 3
# ------------------------------------------------------------
filtered = df[(df["rating"] >= 4.0) & (df["years_exp"] > 3)]

print("\n🔍 Filtered (rating >= 4.0 AND years_exp > 3):")
print(filtered[["name", "department", "salary", "years_exp", "rating", "promoted"]].head())

# ------------------------------------------------------------
# 6) Sort by salary descending, print top 5 earners with their department and rating
# ------------------------------------------------------------
top5 = df.sort_values(by="salary", ascending=False).head(5)

print("\n💰 Top 5 earners (by salary):")
print(top5[["name", "department", "salary", "rating"]].to_string(index=False))
