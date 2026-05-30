import random

# Arrival Time Generator
def generate_arrival_time():
    return random.uniform(1, 10)

# Service Time Generator
def generate_service_time():
    service_times = [1, 2, 3, 4, 5, 6]
    probabilities = [0.05, 0.10, 0.20, 0.30, 0.25, 0.10]

    r = random.random()
    cumulative = 0

    for time, prob in zip(service_times, probabilities):
        cumulative += prob
        if r <= cumulative:
            return time

    return service_times[-1]

# Simulation Parameters
NUM_CUSTOMERS = 20

customers = []

current_arrival = 0
server_free_time = 0

# Simulation Loop
for i in range(NUM_CUSTOMERS):

    # Generate arrival
    inter_arrival = generate_arrival_time()
    current_arrival += inter_arrival

    # Generate service time
    service_time = generate_service_time()

    # Determine service start time
    start_time = max(current_arrival, server_free_time)

    # Waiting time
    waiting_time = start_time - current_arrival

    # End of service
    end_time = start_time + service_time

    # Total system time
    system_time = end_time - current_arrival

    customers.append({
        "id": i + 1,
        "arrival": current_arrival,
        "start": start_time,
        "end": end_time,
        "waiting": waiting_time,
        "system": system_time,
        "service": service_time
    })

    # Update server state
    server_free_time = end_time

# Time-Weighted Calculations

total_simulation_time = customers[-1]["end"]

weighted_system_sum = 0
weighted_queue_sum = 0

for customer in customers:

    weighted_system_sum += customer["system"] * customer["service"]

    weighted_queue_sum += customer["waiting"] * customer["service"]

average_system = weighted_system_sum / total_simulation_time

average_queue = weighted_queue_sum / total_simulation_time

# Display Results
print("\n=== Time-Weighted Queue Analysis ===")

print(f"Weighted Average Time in System: {average_system:.2f} minutes")

print(f"Weighted Average Waiting Time: {average_queue:.2f} minutes")
