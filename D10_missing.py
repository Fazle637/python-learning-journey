import pandas as pd
import numpy as np

data = {
    "name":   ["Alice","Bob","Clara","David","Eva","Frank","Grace"],
    "age":    [25, np.nan, 31, 28, np.nan, 35, 29],
    "salary": [52000, 45000, np.nan, 61000, 48000, np.nan, 55000],
    "dept":   ["Engineering","Marketing",None,"Sales","Marketing","Engineering",None],
    "score":  [88, 72, 95, np.nan, 79, 84, np.nan],
}
df = pd.DataFrame(data)
print(df)

#Detect missing values
print(df.isna())
print(df.isna().sum())
print(df.isna().sum() / len(df) * 100)
print(df[df.isna().any(axis=1)])

#Drop Missing
df_dropped = df.dropna()
print((f"After dropna(): {len(df_dropped)} rows"))

df_drop_score = df.dropna(subset=["score"])
print(f"After dropna(subset=['score']): {len(df_drop_score)} rows")

# Fill missing
df_filled = df.copy()   # ALWAYS work on a copy

df_filled["age"]    = df_filled["age"].fillna(df_filled["age"].median())
df_filled["salary"] = df_filled["salary"].fillna(df_filled["salary"].mean())
df_filled["score"]  = df_filled["score"].fillna(df_filled["score"].median())
df_filled["dept"]   = df_filled["dept"].fillna(df_filled["dept"].mode()[0])

print(df_filled)
print(df_filled.isna().sum())

# Forward / Backward fill
ts = pd.Series([10, np.nan, np.nan, 40, np.nan, 60])
print(ts.ffill().values)
print(ts.ffill().values)