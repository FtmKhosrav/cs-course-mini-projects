# String DP Pair Sum with Range Queries

This project solves a string-based dynamic programming problem with efficient range query processing.

The goal is to preprocess a string and answer multiple queries based on computed DP values.


## Problem Description

We are given a string `s`.

We define a dynamic programming array `dp` such that:

- If two consecutive characters are equal, we update the DP value
- Otherwise, we carry forward the previous value

After preprocessing, we answer multiple queries `(a, b)` by computing:

```
dp[b-1] - dp[a-1]
```


## Idea

We preprocess the string using DP:

- `dp[i]` stores accumulated values based on valid adjacent character pairs
- If `s[i] == s[i-1]`, we update:
  ```
  dp[i] = dp[i-2] + i
  ```
- Otherwise:
  ```
  dp[i] = dp[i-1]
  ```

This allows fast query answering in O(1).


## Algorithm Steps

1. Read input string `s`
2. Build DP array
3. Precompute all values
4. Answer `m` queries using prefix differences


## Complexity

| Phase | Complexity |
|------|-----------|
| DP Preprocessing | O(n) |
| Each Query | O(1) |
| Total | O(n + m) |


## Input

- String `s`
- Integer `m` (number of queries)
- Queries `(a, b)`


## Output

- Result of each query


## Key Concepts

- Dynamic Programming
- String processing
- Prefix sum technique
- Range queries optimization


## 👩‍💻 Author

Fateme Khosravi  
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis
