# Player Report Chain Simulation

This project simulates a reporting system between players, where each player reports exactly one other player. The goal is to trace the chain of reports and determine how players are affected through these connections.


## Problem Overview

We are given `n` players. Each player reports exactly one other player, forming a directed relationship (a functional graph).

Starting from each player, we follow the reporting chain until we reach a previously processed or already marked player.

The task is to determine the final status of each player in this system.


## ⚙️ Logic

- Each player points to exactly one other player.
- Chains of reports are followed step by step.
- Players are marked based on their role in the chain:
  - Starting point of a chain
  - Intermediate player
  - Final affected player


## Input

- `n`: number of players
- `reports[]`: array where `reports[i]` is the player reported by player `i+1`


## Output

An array showing the status of each player:
- `0`: unprocessed
- `1`: starting/reporting player
- `2`: final affected player in a chain


## Key Concepts

- Functional graph representation
- Iterative chain traversal
- Cycle/visited handling idea
- Array-based simulation


## 👩‍💻 Author

Fateme Khosravi  
Computer Science Graduate | Interested in AI, Data Science, and Systems Analysis
