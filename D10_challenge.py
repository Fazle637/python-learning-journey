import pandas as pd
import numpy as np

dirty_data = {
    "name":       ["Alice","Bob","alice","Clara",None,"  Eve  ","Frank","Grace"],
    "age":        [24, 30, 24, np.nan, 28, -3, 200, 26],
    "salary":     ["48,000","62000","48,000",np.nan,"55000","51,000","70000","58000"],
    "city":       ["London","PARIS","London","berlin","London","Paris","BERLIN","london"],
    "rating":     [4.2, 3.8, 4.2, 4.9, np.nan, 5.7, 3.5, 4.1],
    "department": ["Engineering","Sales","Engineering","Marketing",
                   "sales","SALES","Engineering","Marketing"],
}
df = pd.DataFrame(dirty_data)

#Before Report
print("🔴 BEFORE CLEANING")
print("Shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nData types:\n", df.dtypes)
print("\nDuplicate rows:", df.duplicated().sum())

# Drop missing names
df = df.dropna(subset=["name"])

# Fix salary
df["salary"] = df["salary"].str.replace(",", "", regex=False)
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["salary"] = df["salary"].fillna(df["salary"].median()).astype(int)

print("\nSalary fixed:\n", df["salary"])

#Fix age
df["age"] = df["age"].fillna(df["age"].median())
df["age"] = df["age"].clip(16, 75)

print("\nAge fixed:\n", df["age"])

#Fix Rating
df["rating"] = df["rating"].fillna(df["rating"].mean())
df["rating"] = df["rating"].clip(1.0, 5.0)

print("\nRating fixed:\n", df["rating"])

# stirng cleaning
df["name"] = df["name"].str.strip().str.lower().str.title()
df["city"] = df["city"].str.strip().str.title()
df["department"] = df["department"].str.strip().str.title()

print("\nCleaned text columns:\n", df[["name", "city", "department"]])

#Remove duplicates
print("\nBefore duplicates:", len(df))
print(df[df.duplicated()])

df = df.drop_duplicates()
print("After duplicatrs:", len(df))

# After report
print("\n After Cleaning")
print("Shape:", df.shape)
print("\nMissing values:", df.isna().sum())
print("\nData types:\n", df.dtypes)
print("\nDuplicates:", df.duplicated().sum())

#save file
df.to_csv("cleaned.csv", index=False)
print("\n cleaned.csv saved")

# Final Result
print("\n=== Final Clean Data ===")
print(df)
