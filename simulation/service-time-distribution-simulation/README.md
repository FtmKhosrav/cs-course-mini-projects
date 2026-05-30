# Queue Service Distribution Simulation

## Overview

This project simulates a **single-server queueing system** with probabilistic service times.

The simulation analyzes customer waiting behavior and server performance under a random service-time distribution.


## System Configuration

### Arrival Time Distribution

Customers arrive randomly using a uniform distribution:

- Between 1 and 10 minutes


### Service Time Distribution

| Service Time | Probability |
|--------------|-------------|
| 1 | 0.05 |
| 2 | 0.10 |
| 3 | 0.20 |
| 4 | 0.30 |
| 5 | 0.25 |
| 6 | 0.10 |


## Metrics Calculated

- Average Waiting Time
- Maximum Waiting Time
- Maximum Queue Length
- Server Utilization


## Key Observation

Changing the service-time distribution has a major impact on queue behavior.

Increasing the probability of shorter service times helps reduce:

- Queue congestion
- Waiting times
- System delays


## Technologies Used

- Python
- Random module
- Discrete Event Simulation concepts


## 👩‍💻 Author

Fateme Khosravi
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis
