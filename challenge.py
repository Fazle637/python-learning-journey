import numpy as np

np.random.seed(42)
n = 500

#Simulate study hours
hours = np.random.normal(5, 2, n)
hours = np.clip(hours, 0, 12)

#Simulate scores
noise = np.random.normal(0, 8, n)
scores = 40 + (hours * 5) + noise

# Clip scores 0-100
scores = np.clip(scores, 0, 100)
scores =scores.astype(int)

# Basic statistics
mean = np.mean(scores)
median = np.median(scores)
std = np.std(scores)
min_score = np.min(scores)
max_score = np.max(scores)

# Pass rate
pass_rate = np.mean(scores >= 60) * 100

print(" Score Statistics: ")
print("Mean:", mean)
print("Median:", median)
print("Std Dev:", std)
print("Min:", min_score)
print("Max:", max_score)
print("Pass Rate (%):", pass_rate)

# Correlation
correlation = np.corrcoef(hours, scores)[0, 1]
print("\n Correlation between study hours and scores:")
print(correlation)

#IQR and outliers
Q1 = np.percentile(scores, 25)
Q3 = np.percentile(scores, 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = scores[(scores < lower_bound) | (scores > upper_bound)]

print("\n Outliers:")
print("Number of outliers:", len(outliers))

#Shuffle and split
indices = np.arange(n)
np.random.shuffle(indices)

split = int(0.8 * n)

train_idx = indices[:split]
test_idx = indices[split:]

train_scores = scores[train_idx]
test_scores = scores[test_idx]

print("\n Train/Test Mean scores:")
print("Train Mean:", np.mean(train_scores))
print("Test Mean:", np.mean(test_scores))