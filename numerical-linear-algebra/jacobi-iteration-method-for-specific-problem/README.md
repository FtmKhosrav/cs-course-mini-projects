# Jacobi Iteration Method for Solving Linear Systems

## Overview

This project implements the **Jacobi Iteration Method** to solve a system of linear equations.

It is a numerical method used to approximate solutions of the form:

Ax = b


## System of Equations

The implemented system is:

10x1 + x2 + x3 = 12
x1 + 10x2 + x3 = 12
x1 + x2 + 10x3 = 12


## Method

The Jacobi method updates each variable using values from the previous iteration:

- Each variable is computed independently
- Values are updated simultaneously after each iteration


## Output

The program prints the values of x1, x2, x3 after each iteration.

Example:

Iteration 1: x1 = 1.200, x2 = 1.200, x3 = 1.200
Iteration 2: x1 = 0.960, x2 = 0.960, x3 = 0.960


## Concepts Used

- Linear Algebra
- Iterative Methods
- Jacobi Algorithm
- Matrix Computation


## Tools

- Python
- NumPy


## 👩‍💻 Author

Fateme Khosravi
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis
