import numpy as np

# Input matrix A
A = np.array([
    [4, 3],
    [1, 2]
])

# QR Iteration for Eigenvalues
def qr_eigenvalues(matrix, max_iterations=1000, tolerance=1e-10):

    # Copy matrix to avoid modifying original
    A_k = np.copy(matrix)

    for iteration in range(max_iterations):

        # QR decomposition
        Q, R = np.linalg.qr(A_k)

        # Update step: A_{k+1} = RQ
        A_k = R @ Q

        # Check convergence (off-diagonal elements)
        off_diagonal = np.sqrt(np.sum(np.triu(A_k, 1)**2))

        if off_diagonal < tolerance:
            break

    # Eigenvalues are approximated by diagonal elements
    return np.diag(A_k)


# Compute eigenvalues
eigenvalues = qr_eigenvalues(A)


# Output
print("Eigenvalues of matrix A:")
print(eigenvalues)
