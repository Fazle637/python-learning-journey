import numpy as np

scores = np.array([72, 88, 45, 95, 61, 78, 53, 84, 91, 67])

# core statistics
print(f"Mean: {np.mean(scores):.2f}")
print(f"Median: {np.median(scores):.2f}")
print(f"Std: {np.std(scores):.2f}")
print(f"Var: {np.var(scores):.2f}")
print(f"Range: {np.ptp(scores)}")

# mean vs median
with_outlier = np.append(scores, 200)
print(f"\nWith outlier 200:")
print(f" Mean: {np.mean(with_outlier):.2f}")
print(f" Median: {np.median(with_outlier):.2f}")

# percentiles and quartiles
q1 = np.percentile(scores, 25)
q3 = np.percentile(scores, 75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

test = np.array([72, 88, 45, 95, 61, 78, 53, 84, 200, -10])
outliers = test[(test < lower) | (test > upper)]
clean = test[(test >= lower) & (test <= upper)]

print(f"\nQ1={q1}, Q3={q3}, IQR={iqr}")
print(f"Fences: [{lower:.1f}, {upper:.1f}]")
print(f"Outliers: {outliers}")
print(f"Clean: {clean}")

# Sorting & ranking with argsort
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
arr = np.array([72, 88, 45, 95, 61])
ranked = np.argsort(arr)[::-1]

print("\nRanking:")
for rank, idx in enumerate(ranked):
    print(f" {rank+1}. {names[idx]}: {arr[idx]}")
    
# Correlation
study_hours = np.array([2, 5, 1, 8, 3, 7, 4, 6])
test_scores = np.array([55, 80, 45, 95, 60, 90, 70, 85])
corr = np.corrcoef(study_hours, test_scores)[0, 1]
print(f"\nCorrelation: {corr:.2f}")

# cumulative
sales = np.array([120, 145, 98, 170, 155, 210])
print(f"Cumulative: {np.cumsum(sales)}")
