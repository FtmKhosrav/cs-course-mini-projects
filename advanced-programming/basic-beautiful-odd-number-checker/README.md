# Beautiful Odd Number Checker

## Problem

A number is considered a **beautiful odd number** if:

1. The count of its prime divisors is itself a prime number
2. The number is divisible by that count

The program:

- Finds all beautiful odd numbers from 1 to n
- Computes their total sum
- Prints the reverse of the sum

If no such number exists:

```text
NOT FOUND!
```


## Approach

For each number:

1. Find all divisors
2. Count how many divisors are prime
3. Check the required conditions
4. Add valid numbers to the total

Finally:

- Reverse the digits of the total sum
- Print the result


## Concepts Used

- Loops
- Prime checking
- Divisor counting
- Number manipulation


## Complexity

This implementation uses brute force divisor checking.

Approximate complexity:

O(n³)


## 👩‍💻 Author

Fateme Khosravi  
Computer Science Graduate | Problem Solving Enthusiast
