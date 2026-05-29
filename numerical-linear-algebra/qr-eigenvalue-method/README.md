# Eigenvalue Computation using QR Iteration Method

## Overview

This project implements a numerical method to compute the **eigenvalues of a square matrix** using the **QR Iteration Algorithm** (also known as the LR method in iterative form).

It is an educational implementation in Numerical Linear Algebra to demonstrate how eigenvalues can be approximated without direct analytical decomposition.


## Mathematical Idea

Given a square matrix \( A \), the QR algorithm iteratively transforms it as:

1. Decompose:
   \[
   A_k = Q_k R_k
   \]

2. Update:
   \[
   A_{k+1} = R_k Q_k
   \]

As iterations continue, the matrix converges to an upper triangular form, and:

\[
\text{eigenvalues} \approx \text{diagonal elements of } A_k
\]


## Method

The algorithm performs the following steps:

1. Start with matrix \( A \)
2. Apply QR decomposition repeatedly
3. Update matrix using \( RQ \)
4. Check convergence using off-diagonal values
5. Stop when the matrix becomes nearly triangular
6. Extract eigenvalues from the diagonal


## Input

A predefined matrix in the code:

```
A =
[[4, 3],
 [1, 2]]
```


## Output

The program prints:

- Approximate eigenvalues of the matrix

Example output:

```
Eigenvalues of matrix A:
[5. 1.]
```


## Concepts Used

- Linear Algebra
- Eigenvalues & Eigenvectors
- QR Decomposition
- Iterative Numerical Methods
- Matrix Factorization


## Technologies Used

- Python
- NumPy


## Notes

- This is a numerical approximation method
- Accuracy depends on number of iterations and convergence tolerance
- Suitable for educational purposes in Numerical Linear Algebra


## 👩‍💻 Author

Fateme Khosravi
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis
