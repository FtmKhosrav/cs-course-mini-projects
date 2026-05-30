# Time-Weighted Queue Analysis

## Overview

This project simulates a single-server queueing system and computes:

- Time-weighted average number of customers in the system
- Time-weighted average waiting time in the queue

The simulation is based on discrete-event queueing concepts.


## System Configuration

### Arrival Distribution

Customers arrive according to a uniform distribution:

- Between 1 and 10 minutes


### Service-Time Distribution

| Service Time | Probability |
|--------------|-------------|
| 1 | 0.05 |
| 2 | 0.10 |
| 3 | 0.20 |
| 4 | 0.30 |
| 5 | 0.25 |
| 6 | 0.10 |


## Metrics Computed

- Waiting Time
- System Time
- Time-Weighted Average System Time
- Time-Weighted Average Queue Time


## Key Insight

Weighted averages provide more realistic system analysis compared to simple arithmetic averages because they account for how long customers remain in the system.

This approach is commonly used in:

- Queueing theory
- Operations research
- Service system analysis
- Performance engineering


## Technologies Used

- Random module
- Discrete Event Simulation


## 👩‍💻 Author

Fateme Khosravi
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis
