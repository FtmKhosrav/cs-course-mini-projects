import numpy as np
import matplotlib.pyplot as plt

# Simulation Parameters
BUS_INTERVAL = 15  # minutes
MIN_PASSENGER_INTERVAL = 5
MAX_PASSENGER_INTERVAL = 10
TOTAL_PASSENGERS = 500

# Generate Passenger Arrivals
passenger_intervals = np.random.uniform(
    MIN_PASSENGER_INTERVAL,
    MAX_PASSENGER_INTERVAL,
    TOTAL_PASSENGERS
)

passenger_arrival_times = np.cumsum(passenger_intervals)

# Generate Bus Arrivals
bus_arrival_times = np.arange(
    0,
    passenger_arrival_times[-1] + BUS_INTERVAL,
    BUS_INTERVAL
)

# Compute Waiting Times
wait_times = []

for arrival in passenger_arrival_times:
    next_bus = bus_arrival_times[bus_arrival_times >= arrival][0]
    wait_times.append(next_bus - arrival)

wait_times = np.array(wait_times)

# Statistics
mean_wait = np.mean(wait_times)
max_wait = np.max(wait_times)
min_wait = np.min(wait_times)

print(f"Average waiting time: {mean_wait:.2f} minutes")
print(f"Maximum waiting time: {max_wait:.2f} minutes")
print(f"Minimum waiting time: {min_wait:.2f} minutes")

# Visualization
plt.hist(wait_times, bins=20, edgecolor='black')
plt.title('Passenger Waiting Time Distribution')
plt.xlabel('Waiting Time (minutes)')
plt.ylabel('Number of Passengers')
plt.show()
