import numpy as np

# Input matrix A
A = np.array([
    [4, 3, 0],
    [3, 4, -1],
    [0, -1, 4]
])

# Test vector x (non-zero vector)
X = np.array([1, 1, 1])

# Convert x to column vector form
X_T = X.reshape(1, -1)

# Compute x^T A
XT_A = np.dot(X_T, A)

# Compute quadratic form x^T A x
result = np.dot(XT_A, X)

# Check positive definiteness (simplified test)
if result > 0:
    print("Matrix is positive definite (based on test vector).")
else:
    print("Matrix is NOT positive definite (based on test vector).")
