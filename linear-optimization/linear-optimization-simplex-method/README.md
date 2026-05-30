# Simplex Method for Linear Optimization

## Project Description

This project implements the **Simplex Algorithm** to solve Linear Programming (LP) problems.

The goal is to maximize a linear objective function under a set of linear inequality constraints.


## Problem Formulation

Maximize:

cᵀ x

Subject to:

A x ≤ b
x ≥ 0


## Method

The Simplex algorithm works by:

1. Converting constraints into a tableau form
2. Adding slack variables
3. Iteratively selecting pivot elements
4. Performing row operations to improve the objective value
5. Stopping when no improvement is possible


## Implementation Details

- Tableau-based simplex method
- Slack variables for inequality constraints
- Pivot selection using:
  - Most negative coefficient (entering variable)
  - Minimum ratio test (leaving variable)
- Iterative optimization until optimal solution


## Example

```python
c = [2, 3]

A = [
    [1, -1],
    [3, 1],
    [4, 3]
]

b = [2, 5, 7]
```


## Output

- Optimal variable values
- Maximum objective function value

Example:

```
Variables: [x1, x2, ...]
Objective Value: Z*
```


## Requirements

- numpy

Install dependencies:

```bash
pip install numpy
```


## How to Run

```bash
python main.py
```


## 👩‍💻 Author

Fateme Khosravi
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis
