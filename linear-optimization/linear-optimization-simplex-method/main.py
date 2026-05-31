import numpy as np


def simplex_solver(c, A, b):
    m, n = len(b), len(c)

    # Build initial simplex tableau
    tableau = np.zeros((m + 1, m + n + 1))

    # Objective function row
    tableau[0, :n] = -c

    # Constraints
    tableau[1:, :n] = A

    # Slack variables
    tableau[1:, n:n + m] = np.eye(m)

    # Right-hand side
    tableau[1:, -1] = b

    # Simplex iterations
    while np.any(tableau[0, :-1] < 0):

        pivot_col = np.argmin(tableau[0, :-1])

        ratios = tableau[1:, -1] / tableau[1:, pivot_col]
        pivot_row = np.argmin(ratios) + 1

        pivot_element = tableau[pivot_row, pivot_col]

        # Normalize pivot row
        tableau[pivot_row, :] /= pivot_element

        # Eliminate other rows
        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

    solution = {
        "objective_value": tableau[0, -1],
        "variables": tableau[1:, -1]
    }

    return solution


# Example problem
c = np.array([2, 3])
A = np.array([
    [1, -1],
    [3, 1],
    [4, 3]
])
b = np.array([2, 5, 7])

result = simplex_solver(c, A, b)

print("Optimal Solution:")
print("Variables:", result["variables"])
print("Objective Value:", result["objective_value"])
