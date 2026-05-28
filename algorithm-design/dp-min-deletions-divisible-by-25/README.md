# Minimum Deletions to Make Number Divisible by 25 (DP Solution)

## Problem

Given a number as a string, we can delete digits from it.

We want to find the minimum number of deletions required so that the resulting number is divisible by 25.


## Key Idea

We use Dynamic Programming over prefixes of the number.

Instead of directly working with the full number, we track:

- current prefix
- remainder modulo 25


## DP Definition

dp[i][r] = minimum deletions required using first i digits  
so that the resulting number has remainder r modulo 25


## Transitions

For each digit:

### 1. Delete digit
We increase deletion count:

dp[i][r] = dp[i-1][r] + 1

### 2. Keep digit
We update remainder:

new_r = (r * 10 + digit) % 25

dp[i][new_r] = min(dp[i][new_r], dp[i-1][r])


## Answer

The final answer is:

dp[n][0]

because remainder 0 means divisible by 25.


## Complexity

| Type | Cost |
|------|------|
| Time | O(n × 25) |
| Space | O(n × 25) |


## Concepts Used

- Dynamic Programming
- Modular arithmetic
- State transition on strings
- Optimization with remainder states


## 👩‍💻 Author

Fateme Khosravi  
Computer Science Graduate | Algorithms & Data Science Enthusiast
