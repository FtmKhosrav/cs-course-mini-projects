# Random Variable Simulation (Monte Carlo)

## Project Description

This project simulates random variables and analyzes the distribution of derived variables using Monte Carlo simulation.

Two cases are studied:

- Z = X × Y
- Z = X ÷ Y

where X and Y are uniformly distributed random variables.


## Problem Definition

X ~ Uniform(0, 20)
Y ~ Uniform(2, 18)

We generate 200 samples for each case and compute:

- Product: Z = X × Y
- Ratio: Z = X ÷ Y


## Methodology

For each case:

1. Generate random samples for X and Y
2. Compute Z
3. Plot histogram of Z values
4. Compute:
   - Mean
   - Range (min, max)


## Results

### Case 1: Z = X × Y
- Distribution is skewed to higher values
- Mean is relatively large due to multiplication

### Case 2: Z = X ÷ Y
- Distribution is more concentrated
- Values depend strongly on denominator Y


## Visualization

- Histogram for Z = X × Y
- Histogram for Z = X ÷ Y


## Requirements

```bash
numpy
matplotlib
```


## How to Run

```bash
python main.py
```


## 👩‍💻 Author

Fateme Khosravi
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis
