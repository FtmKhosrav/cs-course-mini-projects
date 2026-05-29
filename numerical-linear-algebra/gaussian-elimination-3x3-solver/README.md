# Gaussian Elimination Solver (3×3 Linear System)

## Overview

This project solves a system of **3 linear equations with 3 unknown variables** using the **Gaussian Elimination method with partial pivoting**.

The system is written in matrix form as:

\[
AX = B
\]

where:
- \( A \) is a 3×3 coefficient matrix  
- \( B \) is a constants vector  
- \( X \) is the unknown solution vector  


## Algorithm Description

The solution is computed in two main phases:

### 1. Forward Elimination
The coefficient matrix \( A \) is transformed into an **upper triangular matrix** by eliminating elements below the pivot positions.

To improve numerical stability, **partial pivoting** is used:
- The row with the largest absolute value in the current column is selected as the pivot
- Rows are swapped if necessary


### 2. Back Substitution
Once the matrix is in upper triangular form, the solution vector \( X \) is computed starting from the last equation and moving upward.


## Features

- Solves a 3×3 linear system
- Implements Gaussian Elimination
- Uses Partial Pivoting for stability
- Handles singular or non-unique systems
- Outputs results with 2 decimal precision


## Input Format

The program interactively asks for:

### Coefficient Matrix \( A \):
```
a11 a12 a13
a21 a22 a23
a31 a32 a33
```

### Constants Vector \( B \):
```
b1
b2
b3
```


## Output

The solution is displayed as:

```
X1 = value
X2 = value
X3 = value
```

(values rounded to 2 decimal places)


## Concepts Used

- Gaussian Elimination
- Partial Pivoting
- Forward Elimination
- Back Substitution
- Numerical Linear Algebra


## Technologies

- Python
- NumPy


## Notes

- Works specifically for 3×3 systems
- Pivoting reduces numerical instability
- If matrix is singular, the system has no unique solution


## 👩‍💻 Author

Fateme Khosravi  
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis