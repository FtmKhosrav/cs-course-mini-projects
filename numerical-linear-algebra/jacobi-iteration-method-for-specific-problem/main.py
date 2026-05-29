import numpy as np

# Coefficient matrix A
A = np.array([
    [10, 1, 1],
    [1, 10, 1],
    [1, 1, 10]
], dtype=float)

# Right-hand side vector b
b = np.array([12, 12, 12], dtype=float)

# Initial guess for x
x = np.array([0.0, 0.0, 0.0])

# Number of iterations
iterations = 3


# Jacobi Iteration Method
for i in range(iterations):

    # New approximation vector
    x_new = np.zeros_like(x)

    # Update each variable using previous iteration values
    x_new[0] = (b[0] - (A[0, 1] * x[1] + A[0, 2] * x[2])) / A[0, 0]
    x_new[1] = (b[1] - (A[1, 0] * x[0] + A[1, 2] * x[2])) / A[1, 1]
    x_new[2] = (b[2] - (A[2, 0] * x[0] + A[2, 1] * x[1])) / A[2, 2]

    # Print current iteration results
    print(f"Iteration {i+1}: x1 = {x_new[0]:.3f}, x2 = {x_new[1]:.3f}, x3 = {x_new[2]:.3f}")

    # Update solution
    x = x_new
