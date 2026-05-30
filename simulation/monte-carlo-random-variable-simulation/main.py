import numpy as np
import matplotlib.pyplot as plt

# Number of samples
n_samples = 200

# Case 1: Z = X * Y

# Simulate random variables
X = np.random.uniform(0, 20, n_samples)
Y = np.random.uniform(2, 18, n_samples)

Z_product = X * Y

# Statistics
range_product = (np.min(Z_product), np.max(Z_product))
mean_product = np.mean(Z_product)

# Histogram
plt.hist(Z_product, bins=20, edgecolor="black")
plt.title("Distribution of Z = X * Y")
plt.xlabel("Z values")
plt.ylabel("Frequency")
plt.show()

print("=== Z = X * Y ===")
print("Range:", range_product)
print("Mean:", mean_product)


# Case 2: Z = X / Y

X = np.random.uniform(0, 20, n_samples)
Y = np.random.uniform(2, 18, n_samples)

Z_ratio = X / Y

# Statistics
range_ratio = (np.min(Z_ratio), np.max(Z_ratio))
mean_ratio = np.mean(Z_ratio)

# Histogram
plt.hist(Z_ratio, bins=20, edgecolor="black")
plt.title("Distribution of Z = X / Y")
plt.xlabel("Z values")
plt.ylabel("Frequency")
plt.show()

print("=== Z = X / Y ===")
print("Range:", range_ratio)
print("Mean:", mean_ratio)
