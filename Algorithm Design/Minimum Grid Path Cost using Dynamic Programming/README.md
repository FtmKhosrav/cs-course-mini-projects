# Minimum Grid Path Cost using Dynamic Programming

This mini-project demonstrates how Dynamic Programming (DP) can be used to solve a grid traversal optimization problem.

The program calculates the minimum cost required to move through a grid and checks whether the final cost matches a target value.


## Problem Description

Given an `n × m` grid:

- Moving **right** from cell `(i, j)` to `(i, j+1)` costs `i`
- Moving **down** from cell `(i, j)` to `(i+1, j)` costs `j`

For each test case, determine whether it is possible to reach the destination cell `(n, m)` with a minimum cost exactly equal to `k`.

The output should be:

- `YES` → if the minimum path cost equals `k`
- `NO` → otherwise


## Algorithm Steps

1. Read input values
2. Create DP table
3. Initialize first row and first column
4. Fill remaining cells using recurrence relation
5. Compare final cost with `k`
6. Print result


## Concepts Used

- Dynamic Programming
- Grid Traversal
- State Transition
- Optimization Problems


## Time Complexity

| Operation | Complexity |
|---|---|
| DP Table Construction | O(n × m) |


## Sample Input

```text
2
3 3 8
2 2 3
```


## Sample Output

```text
YES
NO
```


## What I Practiced in This Project

- Building DP state tables
- Recursive-to-iterative thinking
- Grid-based optimization problems
- Translating mathematical relations into code


## 👩‍💻 Author

Fateme Khosravi

Computer Science Graduate  
Interested in Data Science, Algorithms, and Systems Analysis
````
