# Row Dominance in a 4x3 Matrix

## Problem

A 4×3 matrix is given. The program:

1. Ensures all values are unique and less than 100
2. Finds the maximum element in each row
3. Checks whether that element is greater than all elements in its column
4. Prints the index (1–4) of the row that satisfies the condition


## Idea

For each row:
- Find its maximum value
- Identify its column position
- Compare it with other rows in the same column


## Concepts Used

- Matrix traversal
- Max finding
- Index mapping
- Conditional checks


## Notes

The original implementation uses extensive manual inequality checks which can be simplified using sets or loops.


## 👩‍💻 Author

Fateme Khosravi
Computer Science Student
