# Habil and Baker Queue Simulation

## Project Description

This project simulates a two-server queueing system involving two service providers: Habil and Baker. Customers arrive randomly over time and are served by the first available server based on availability and probabilistic rules.

The goal is to analyze system performance using a Discrete Event Simulation (DES) model.


## System Overview

- Customers arrive based on a stochastic interarrival process
- Two independent servers (Habil and Baker)
- Each server has its own probabilistic service time distribution
- Customers are assigned to the first available server
- Simulation runs for 30 customers


## Input Distributions

### Interarrival Time
- Discrete random process
- Values between 1 to 5 minutes

### Service Time (Habil)
- Discrete distribution (3 to 6 minutes)

### Service Time (Baker)
- Discrete distribution (3 to 6 minutes)
- Different probability distribution from Habil


## Performance Metrics

- Average waiting time
- Average service time
- Server utilization (Habil)
- Server utilization (Baker)
- Detailed customer logs


## How to Run

```bash
python main.py
```


## Sample Output

```
=== Habil & Baker Queue Simulation ===

Customers Served: 30
Average Waiting Time: 3.27 minutes
Average Service Time: 3.98 minutes
Habil Utilization: 62.15%
Baker Utilization: 58.40%
```


## Project Structure

```
habil-baker-queue-simulation/
├── main.py
└── README.md
```


## 👩‍💻 Author

Fateme Khosravi
Computer Science Graduate | Interested in Data Science, Algorithms, and Systems Analysis


## Notes

This is a stochastic discrete-event simulation. Results may vary due to randomness in arrival and service processes.
