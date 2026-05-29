# Positive Definiteness Check of a Matrix

## Overview

This project provides a simple numerical method to check whether a given matrix is **positive definite** using the quadratic form:

\[
x^T A x
\]

It is an educational implementation in Linear Algebra designed to demonstrate matrix properties using vector transformations.


## Mathematical Background

A symmetric matrix \( A \) is considered **positive definite** if:

\[
x^T A x > 0 \quad \text{for all non-zero vectors } x
\]

In this project, we approximate this property using a single test vector.


## Method Used

The program performs the following steps:

1. Defines a square matrix \( A \)
2. Chooses a non-zero test vector \( x \)
3. Computes the quadratic form:
   \[
   x^T A x
   \]
4. Checks whether the result is positive


## Input

The matrix and vector are defined inside the code:

### Matrix A:
```
[[4, 3, 0],
 [3, 4, -1],
 [0, -1, 4]]
```

### Test vector x:
```
[1, 1, 1]
```


## Output

The program prints:

- `"Matrix is positive definite."` if \( x^T A x > 0 \)
- `"Matrix is not positive definite."` otherwise


## Important Note

This implementation:

- Uses only **one test vector**
- Does **not fully guarantee** positive definiteness
- A complete verification requires checking **eigenvalues**

---

## Concepts Used

- Linear Algebra
- Quadratic Forms
- Matrix Multiplication
- Positive Definiteness


## Technologies Used

- Python
- NumPy

---

## 👩‍💻 Author

Fateme Khosravi
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis
