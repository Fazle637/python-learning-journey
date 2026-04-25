import pandas as pd
import numpy as np

data =  {
    "name":   ["Alice","Bob","alice","Clara","Bob","  David  ","EVA"],
    "age":    [28, 24, 28, 31, 24, -5, 26],
    "salary": ["52000","45,000","52000","72000","45,000","61000","48000"],
    "dept":   ["Engineering","marketing","Engineering","MARKETING",
               "marketing","Sales","sales"],
    "score":  [88, 72, 88, 95, 72, 84, 150],
}
df = pd.DataFrame(data)
print(df.dtypes)

# Fix data types
df["salary"] = df["salary"].str.replace(",","").astype(int)
print(f"Salary dtype: {df['salary'].dtype}")

# String cleaning
df["name"] = df["name"].str.strip(). str.lower().str.title()
df["dept"] = df["dept"].str.strip().str.title()
print(df[["name", "dept"]])

# String cleaning
s = pd.Series([" hello world ", "PYTHON ", "data science"])
print(s.str.strip())
print(s.str.lower())
print(s.str.replace("", "_"))
print(s.str.contains("python", case=False))
print(s.str.len())

# Remove  duplicates
print(f"Before: {len(df)} rows")
print(df[df.duplicated()])
df = df.drop_duplicates()
print(f"After: {len(df)} rows")

# Fix Invalid values
df["age"] = df["age"].clip(lower=16, upper=80)
df["score"] = df["score"].clip(lower=0, upper=100)
print(df[["name", "age", "score"]])

# Flag outliers
q1 = df["salary"].quantile(0.25)
q3 = df["salary"].quantile(0.75)
iqr = q3 - q1
df["is_outlier"] = (df["salary"] < q1 - 1.5*iqr) | (df["salary"] > q3 + 1.5*iqr)
print(df[["name", "salary", "is_outlier"]])

print("\n === Clean Result ===")
print(df[["name", "age", "salary", "dept", "score"]])