import numpy as np

np.random.seed(42)

# Random generations
uniform = np.random.uniform(0, 100, 10)
normal = np.random.normal(loc=70, scale=10, size=10)
ints = np.random.randint(40, 100, 10)

print(np.round(uniform, 1))
print(np.round(normal, 1))
print(ints)

# Random choice with probabilities
grades = np.array(["A", "B", "C", "D", "F"])
sampled = np.random.choice(grades, size=20, p=[0.1, 0.3, 0.3, 0.2, 0.1])
print(sampled)

#Simulate a realitic class
np.random.seed(0)
n = 200
raw = np.random.normal(loc=68, scale=15, size=n)
scores = np.clip(raw, 0, 100)

print(f"\nSimulated class of {n}:")
print(f"Mean: {np.mean(scores):.1f} | std: {np.std(scores):.1f}")
print(f"Pass rate: {np.mean(scores >= 60)*100:.1f}%")
 
for grade, lo, hi in [("A", 90, 101), ("B", 80, 90), ("C", 70, 80), ("D", 60, 70), ("F", 0, 60)]:
    count = np.sum((scores >= lo) & (scores < hi))
    pct = count / n * 100
    print(f" {grade}: {'#'*int(pct/2)} {count} {pct:.1f}%")

# Monte Carlo pass probability
np.random.seed(1)
trials = 100_000
simulated = np.random.normal(65, 12, trials)  
pass_rate = np.mean(simulated >= 60)
print(f"\n Monte Carlo pass ({trials:,} trials): {pass_rate*100:.2f}%")

# Train split
np.random.seed(42)
dataset = np.arange(1000)
np.random.shuffle(dataset)
split = int(0.8 * len(dataset))
train, test = dataset[:split], dataset[split:]
print(f"Train: {len(train)} | Test: {len(test)}")
