# Linear Programming Duality Converter

## Overview

This project takes a **Linear Programming (LP) problem (primal form)** as input and constructs its corresponding **dual problem**.

It is an educational implementation designed to demonstrate how primal constraints, objective functions, and matrices are transformed into their dual representation.

---

## Features

- Reads a Linear Programming problem from user input
- Supports:
  - Objective function coefficients
  - Constraint matrix (A)
  - Right-hand side vector (b)
  - Constraint signs (≤, ≥, =)
- Prints the original (primal) LP
- Generates and prints the dual LP formulation

---

## Concept

Given a primal LP:

```
Maximize:     cᵀx
Subject to:   Ax (≤, ≥, =) b
```

The program constructs its dual form:

```
Minimize:     bᵀy
Subject to:   Aᵀy (≥, ≤, =) c
```

---

## How It Works

1. The constraint matrix is transposed (A → Aᵀ)
2. The RHS vector becomes part of the dual objective
3. The primal objective coefficients become dual constraints
4. Constraint directions are adjusted based on inequality types


## Input Format

The program interactively asks for:

- Number of variables
- Number of constraints
- Objective function coefficients
- Constraint matrix values
- RHS values of constraints
- Constraint signs (`<=`, `>=`, `=`)


## Output

The program displays:

- Primal LP structure
- Dual LP matrix
- Dual objective coefficients
- Dual constraints


## Example Use Case

This tool is useful for:

- Learning Linear Programming fundamentals
- Understanding LP duality transformation
- Educational demonstrations in Optimization courses


## Technologies Used

- Python
- NumPy


## Notes

- This implementation focuses on **LP transformation only**
- It does **not solve** the optimization problem
- It is intended for academic learning purposes


## 👩‍💻 Author

Fateme Khosravi
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis
