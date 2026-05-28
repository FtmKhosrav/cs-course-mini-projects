# Student Grouping using DFS (Graph Components)

## Problem

We are given a list of students where each student may have a supervisor.

If student A supervises student B, there is a connection between them.

We need to divide students into the minimum number of valid groups under given constraints.


## Idea

We model the problem as a graph:

- Each student = a node
- Supervisor relationship = an undirected edge

Then we use DFS to find all connected components.

Each component is treated as a base group.


## Algorithm

1. Build graph from supervisor relationships
2. Run DFS to find connected components
3. Assign group IDs to each component
4. Count required groups while respecting constraints


## Key Insight

The problem reduces to:

> Find connected components in a graph and assign group labels.


## Complexity

| Step | Complexity |
|------|-----------|
| Graph construction | O(n) |
| DFS traversal | O(n + e) |


## Output

Minimum number of valid groups.


## 👩‍💻 Author

Fateme Khosravi  
Computer Science Graduate | Algorithms & Data Science Enthusiast
