import math

# Cholesky Decomposition A = L L^T
def cholesky_decomposition(A):

    # Initialize lower triangular matrix L with zeros
    L = [[0.0 for _ in range(3)] for _ in range(3)]

    # Compute entries of L
    for i in range(3):
        for j in range(i + 1):

            # Sum of products for previous terms
            sum_value = sum(L[i][k] * L[j][k] for k in range(j))

            if i == j:
                # Diagonal elements
                L[i][j] = math.sqrt(A[i][i] - sum_value)
            else:
                # Off-diagonal elements
                L[i][j] = (A[i][j] - sum_value) / L[j][j]

    return L


# Solve Ly = b (Forward substitution)
def forward_substitution(L, b):

    y = [0.0 for _ in range(3)]

    for i in range(3):
        sum_value = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_value) / L[i][i]

    return y


# Solve L^T x = y (Backward substitution)
def backward_substitution(L, y):

    x = [0.0 for _ in range(3)]

    for i in range(2, -1, -1):
        sum_value = sum(L[j][i] * x[j] for j in range(i + 1, 3))
        x[i] = (y[i] - sum_value) / L[i][i]

    return x


# Input section
print("Enter coefficients for matrix A (3x3):")
A = [[float(input(f"A[{i+1},{j+1}]: ")) for j in range(3)] for i in range(3)]

print("Enter constants for vector b (3x1):")
b = [float(input(f"b[{i+1}]: ")) for i in range(3)]


# Solve system
L = cholesky_decomposition(A)

y = forward_substitution(L, b)

x = backward_substitution(L, y)


# Output result
x_rounded = [round(num, 3) for num in x]
print("Solution (rounded to 3 decimal places):", x_rounded)