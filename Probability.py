import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson

# --- 1. BASIC PROBABILITY SIMULATION ---
print("=== Basic Probability ===")
np.random.seed(0)

# Simulate 10 coin flips
coin_flips = np.random.choice(['H', 'T'], size=10)
print("Coin flips:", coin_flips)

# Simulate 10 dice rolls
dice_rolls = np.random.randint(1, 7, size=10)
print("Dice rolls:", dice_rolls)


# --- 2. DISTRIBUTIONS ---
print("\n=== Distributions ===")

x = np.linspace(-5, 5, 1000)
normal_dist = norm.pdf(x, loc=0, scale=1)

# Binomial distribution (n=10, p=0.5)
binomial_dist = binom.pmf(np.arange(0, 11), n=10, p=0.5)

# Poisson distribution (λ = 3)
poisson_dist = poisson.pmf(np.arange(0, 11), mu=3)

# Plot distributions
plt.figure(figsize=(12, 4))

# Normal
plt.subplot(1, 3, 1)
plt.plot(x, normal_dist)
plt.title("Normal Distribution (μ=0, σ=1)")
plt.grid(True)

# Binomial
plt.subplot(1, 3, 2)
plt.bar(np.arange(0, 11), binomial_dist)
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.grid(True)

# Poisson
plt.subplot(1, 3, 3)
plt.bar(np.arange(0, 11), poisson_dist)
plt.title("Poisson Distribution (λ=3)")
plt.grid(True)

plt.tight_layout()
plt.show()


# --- 3. BAYES' THEOREM ---
print("\n=== Bayes' Theorem ===")
# Example:
# 1% of people have a disease
# Test is 99% accurate (true positive rate = 0.99, false positive rate = 0.01)
P_disease = 0.01
P_no_disease = 0.99
P_pos_given_disease = 0.99
P_pos_given_no_disease = 0.01

# Bayes' Theorem: P(disease | positive) = ?
numerator = P_pos_given_disease * P_disease
denominator = (P_pos_given_disease * P_disease) + (P_pos_given_no_disease * P_no_disease)

P_disease_given_positive = numerator / denominator
print(f"Probability of disease given positive test: {P_disease_given_positive:.4f}")
