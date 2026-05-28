# Student Group Partition using Graph DFS

This project solves a graph-based grouping problem using Depth First Search (DFS) to identify connected components and determine valid student group assignments.


## Problem Overview

We are given `n` students where each student may have a supervisory relationship with another student.

This relationship can be represented as a graph:
- Each student is a node
- A supervisory relation forms an undirected edge between two nodes

The goal is to:
- Group students such that no student is in the same group as their direct supervisor
- Minimize the number of groups


## Idea

- Model the problem as a graph
- Use DFS to find connected components
- Assign group IDs to each component
- Ensure constraints between supervisor relationships are respected


## Approach

1. Read number of students `n`
2. Build graph using supervisor relationships
3. Use DFS to find connected components
4. Assign each node to a group
5. Compute minimum valid grouping


## Algorithm

- Graph representation: adjacency list
- Traversal: DFS
- Complexity: O(n + m)


## Input

- `n`: number of students
- Array `supervisors[]` where each value indicates the supervisor of a student (0 means no supervisor)


## Output

- Minimum number of valid groups satisfying constraints


## Key Concepts

- Graph modeling
- Depth First Search (DFS)
- Connected components
- Constraint-based grouping


## 👩‍💻 Author

Fateme Khosravi  
Computer Science Graduate | Interested in AI, Data Science, and Systems Analysis
