# Iterative List Transformation Simulation

This project simulates repeated transformations on a list until all elements converge to stable values (0 or 1), and then computes a range-based result.


## Problem Description

We are given an initial list of size `n`, where all elements start with value `1`.

The list evolves over time based on neighbor-based transformation rules.

We repeatedly update each element using its left and right neighbors until all elements become either `0` or `1`.

Finally, we count how many `1`s exist in a given range `[s, e]`.


## Idea

Each element `x` is updated based on its neighbors:

Let:
- `left = lst[i-1]`
- `right = lst[i+1]`

Then:

- If `x` is even and neighbors match:
  ```
  x = x / 2
  ```

- If neighbors follow increasing pattern:
  ```
  x = x - 1
  ```

- If neighbors follow decreasing pattern:
  ```
  x = x + 1
  ```

The process repeats until stabilization.


##️ Algorithm Steps

1. Initialize list with all values = 1
2. Repeat until convergence:
   - Update each element based on neighbor rules
   - Check if all values are 0 or 1
3. Count number of `1`s in range `[s, e]`


## Complexity

| Phase | Complexity |
|------|-----------|
| Iterative updates | O(k × n) |
| Final query | O(n) |

Where `k` is number of iterations until convergence.


## Input

- `n`: size of list
- `s, e`: query range


## Output

- Number of `1`s in range `[s, e]` after stabilization


## Key Concepts

- Iterative simulation
- State transformation systems
- Neighbor-based updates
- Convergence logic


## 👩‍💻 Author

Fateme Khosravi  
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis
