import pandas as pd
import numpy as np

# Series
s = pd.Series([88, 72, 95, 61, 45])
print(s)
print(s.dtype, s.index, s.values)

# Series with named index
scores = pd.Series(
    [88, 72, 95, 61, 45],
    index = ["Alice", "Bob", "Charlie", "David", "Eve"]
)

print(scores["Alice"])
print(scores[scores > 70])
print(scores.idxmax())

# DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "age": [20, 22, 21, 23, 20, 22],
    "score": [88, 72, 95, 61, 45, 78],
    "passed": [True, True, True, False, False, True],
    "Subject": ["Python","SQL","Python","Maths","SQL","Maths"],
}
df = pd.DataFrame(data)

#First Look
print(df.head())
print(df.info())
print(df.head(3))
print(df.describe())

# Selecting
print(df["score"])
print(df[["name", "score"]])
print(type(df["score"]))
print(type(df[["score"]]))

#loc vs iloc
print(df.loc[0])
print(df.loc[0, "score"])
print(df.loc[1:3, ["name", "score"]])

print(df.iloc[0])
print(df.iloc[0, 2])
print(df.iloc[1:4, 0:3])

#Boolean indexing
passing = df[df["passed"] == True]
high_scores = df[df["score"] >= 80]
python_only = df[df["Subject"] == "Python"]
combined = df[(df["age"] <= 21) & (df["score"] >= 70)]

print(passing)
print(high_scores[["name", "score"]])
print(python_only)
print(combined)