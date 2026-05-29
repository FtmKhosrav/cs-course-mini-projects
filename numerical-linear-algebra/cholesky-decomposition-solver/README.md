# Cholesky Decomposition Solver

## Overview

This project implements a numerical method to solve a system of linear equations using **Cholesky Decomposition**.

Given a system:

\[
Ax = b
\]

where:
- \( A \) is a symmetric and positive definite matrix
- \( b \) is the constant vector
- \( x \) is the unknown vector

the solution is computed using matrix factorization.


## Mathematical Idea

Cholesky Decomposition factorizes matrix \( A \) as:

\[
A = L L^T
\]

where:
- \( L \) is a lower triangular matrix
- \( L^T \) is its transpose

The system is solved in two steps:

1. Forward substitution:
\[
Ly = b
\]

2. Backward substitution:
\[
L^T x = y
\]


## Algorithm Steps

1. Compute Cholesky factor \( L \)
2. Solve \( Ly = b \) using forward substitution
3. Solve \( L^T x = y \) using backward substitution
4. Output solution vector \( x \)


## Input

User provides:

- A 3×3 matrix \( A \)
- A 3×1 vector \( b \)

Example:

```
A[i,j]: value
b[i]: value
```


## Output

The program outputs:

- Solution vector \( x \) rounded to 3 decimal places

Example:

```
Solution (rounded to 3 decimal places): [x1, x2, x3]
```


## Concepts Used

- Numerical Linear Algebra
- Matrix Factorization
- Cholesky Decomposition
- Forward Substitution
- Backward Substitution


## Requirements

- Python 3.x
- math library (standard)


## Notes

- Matrix A must be symmetric and positive definite
- Method is efficient for such matrices compared to general LU decomposition
- Numerical stability depends on input matrix properties


## 👩‍💻 Author

Fateme Khosravi  
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis