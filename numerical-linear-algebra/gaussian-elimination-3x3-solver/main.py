import numpy as np

def gaussian_elimination():
    print("Enter coefficients of the system:")

    # Input coefficient matrix A (3x3)
    A = np.array([
        [float(input("a11: ")), float(input("a12: ")), float(input("a13: "))],
        [float(input("a21: ")), float(input("a22: ")), float(input("a23: "))],
        [float(input("a31: ")), float(input("a32: ")), float(input("a33: "))]
    ], dtype=float)

    # Input constants vector B (3x1)
    B = np.array([
        float(input("b1: ")),
        float(input("b2: ")),
        float(input("b3: "))
    ], dtype=float)

    n = len(B)

    # Forward Elimination Phase
    # Convert A into upper triangular matrix
    for i in range(n):

        # Partial pivoting: select row with maximum absolute value in current column
        max_row = i + np.argmax(np.abs(A[i:, i]))

        # Check for singular matrix
        if A[max_row, i] == 0:
            raise ValueError("The system has no unique solution (singular matrix).")

        # Swap rows in both A and B
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            B[i], B[max_row] = B[max_row], B[i]

        # Eliminate entries below pivot
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j] -= factor * A[i]
            B[j] -= factor * B[i]

    # Back Substitution Phase
    # Solve upper triangular system
    X = np.zeros(n)

    for i in range(n - 1, -1, -1):
        X[i] = (B[i] - np.dot(A[i, i + 1:], X[i + 1:])) / A[i, i]

    return X


# Run the solver
solution = gaussian_elimination()

print("\nSolution of the system:")
print(f"X1 = {solution[0]:.2f}")
print(f"X2 = {solution[1]:.2f}")
print(f"X3 = {solution[2]:.2f}")