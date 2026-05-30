# Single Server Queue Simulation

## Overview

This project simulates a **single-server queueing system** using discrete event simulation techniques.

Customers arrive randomly and are served one at a time based on a probabilistic service-time distribution.


## System Assumptions

- Number of customers: 20
- Arrival distribution: Uniform (1 to 8 minutes)
- Service time distribution:

| Service Time | Probability |
|--------------|-------------|
| 1 | 0.10 |
| 2 | 0.20 |
| 3 | 0.30 |
| 4 | 0.25 |
| 5 | 0.10 |
| 6 | 0.05 |


## Metrics Calculated

- Waiting Time
- Total Time in System
- Queue behavior (implicit via waiting times)
- Server utilization (can be extended)


## Experiment Extension

The simulation can be repeated using different arrival distributions (e.g., exponential distribution) to study system sensitivity.


## Key Insight

Even with simple random arrivals, queueing systems naturally produce:

- Accumulated waiting times
- Burst behavior in queues
- Non-linear delay effects


## Tools

- Random module
- Discrete Event Simulation logic


## 👩‍💻 Author

Fateme Khosravi
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis
