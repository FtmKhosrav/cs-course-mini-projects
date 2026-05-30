# Linear Regression using Gradient Descent

## Project Description

This project implements Linear Regression from scratch using Gradient Descent.

The model learns a linear relationship between input feature x and output y using an optimization approach.


## Steps

- Load dataset from `.mat` file
- Visualize data
- Add bias term
- Define cost function
- Apply Gradient Descent
- Optimize parameters θ
- Plot cost convergence
- Plot regression line


## Mathematical Model

Hypothesis:
h(x) = θ₀ + θ₁x

Cost Function:
J(θ) = (1 / 2m) Σ (h(xᵢ) - yᵢ)²

Gradient Descent Update:
θ := θ - α/m * Xᵀ (Xθ - y)


## Requirements

- numpy
- matplotlib
- scipy


## How to Run

```bash
python main.py
```


## Output

- Dataset visualization
- Cost function convergence plot
- Final regression line


## 👩‍💻 Author

Fateme Khosravi
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis
