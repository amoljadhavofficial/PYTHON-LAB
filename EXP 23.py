import numpy as np
import scipy.stats as stats

# Flip the coin n times
n = 50
coin = np.random.choice(['H', 'T'], size=n)

# Count heads and tails
heads = list(coin).count('H')
tails = list(coin).count('T')

p_hat = heads / n

print("Coin Outcomes:", coin)
print("Total Flips:", n)
print("Number of Heads:", heads)
print("Number of Tails:", tails)
print("Proportion of Heads (p̂):", round(p_hat, 3))

# Hypothesis Testing
# H0: p = 0.5 (Coin is fair)
# H1: p ≠ 0.5 (Coin is biased)

p = 0.5

# Z-test formula
z = (p_hat - p) / ((p * (1 - p) / n) ** 0.5)

# Calculating p-value
p_value = 2 * (1 - stats.norm.cdf(abs(z)))

print("\nZ-score:", round(z, 3))
print("P-value:", round(p_value, 5))

# Decision-Making
alpha = 0.05

if p_value < alpha:
    print("Decision: Reject H0: Coin is Biased")
else:
    print("Decision: Fail to Reject H0: Coin is Fair")