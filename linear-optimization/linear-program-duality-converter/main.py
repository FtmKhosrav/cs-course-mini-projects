import numpy as np

# ==============================
# Generate Dual of LP Problem
# ==============================
def generate_dual(lp_matrix, lp_objective, lp_constraints, constraint_signs):

    # Transpose matrix A → A^T (for dual constraints)
    def transpose(matrix):
        return np.transpose(matrix)

    # Convert primal objective coefficients → dual RHS (simplified mapping)
    def switch_objective(obj):
        return [-c for c in obj]

    # Convert RHS constraints based on inequality type
    def switch_constraints(constraints, signs):
        result = []
        for c, sign in zip(constraints, signs):

            if sign == "=":
                result.append(c)
            elif sign == ">=":
                result.append(-c)
            else:  # "<="
                result.append(c)

        return result

    # Build dual components
    dual_matrix = transpose(lp_matrix)
    dual_objective = switch_constraints(lp_constraints, constraint_signs)
    dual_constraints = switch_objective(lp_objective)

    return dual_matrix, dual_objective, dual_constraints


# ==============================
# Read LP Problem from User
# ==============================
def read_lp_input():

    num_variables = int(input("Number of variables: "))
    num_constraints = int(input("Number of constraints: "))

    # Objective function
    print("\nEnter objective function coefficients:")
    lp_objective = [
        float(input(f"Coefficient of x{i + 1}: "))
        for i in range(num_variables)
    ]

    # Constraint matrix A
    print("\nEnter constraint matrix:")
    lp_matrix = [
        [
            float(input(f"A[{i+1},{j+1}]: "))
            for j in range(num_variables)
        ]
        for i in range(num_constraints)
    ]

    # RHS vector b
    print("\nEnter RHS values:")
    lp_constraints = [
        float(input(f"b[{i+1}]: "))
        for i in range(num_constraints)
    ]

    # Constraint types
    print("\nEnter constraint signs (<=, >=, =):")
    constraint_signs = [
        input(f"Sign for constraint {i+1}: ")
        for i in range(num_constraints)
    ]

    return (
        np.array(lp_matrix),
        np.array(lp_objective),
        np.array(lp_constraints),
        constraint_signs
    )


# ==============================
# Print Primal LP
# ==============================
def print_lp_problem(lp_matrix, lp_objective, lp_constraints, constraint_signs):

    print("\n=== Primal Linear Program ===")

    print("\nConstraint Matrix (A):")
    print(lp_matrix)

    print("\nObjective Coefficients (c):")
    print(lp_objective)

    print("\nConstraints:")
    for i in range(len(lp_constraints)):
        print(f"{lp_matrix[i]} {constraint_signs[i]} {lp_constraints[i]}")


# ==============================
# Main Program
# ==============================

# Read primal LP
lp_matrix, lp_objective, lp_constraints, constraint_signs = read_lp_input()

# Print primal LP
print_lp_problem(lp_matrix, lp_objective, lp_constraints, constraint_signs)

# Generate dual LP
dual_matrix, dual_objective, dual_constraints = generate_dual(
    lp_matrix,
    lp_objective,
    lp_constraints,
    constraint_signs
)

# Print dual LP
print("\n=== Dual Linear Program ===")

print("\nDual Matrix (A^T):")
print(dual_matrix)

print("\nDual Objective Coefficients:")
print(dual_objective)

print("\nDual Constraints:")
for i in range(len(dual_constraints)):
    print(f"{dual_matrix[i]} {dual_constraints[i]}")
