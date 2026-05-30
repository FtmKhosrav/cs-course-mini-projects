import random

# Arrival Time Generator
def generate_arrival_time(min_time=1, max_time=8):
    return random.uniform(min_time, max_time)

# Service Time Generator
def generate_service_time():
    service_times = [1, 2, 3, 4, 5, 6]
    probabilities = [0.1, 0.2, 0.3, 0.25, 0.1, 0.05]

    r = random.random()
    cumulative = 0

    for time, prob in zip(service_times, probabilities):
        cumulative += prob
        if r <= cumulative:
            return time

    return service_times[-1]  # fallback

# Simulation
def simulate(num_customers=20):
    arrival_times = []
    service_times = []
    waiting_times = []
    system_times = []

    current_time = 0

    for i in range(num_customers):

        arrival = generate_arrival_time()
        service = generate_service_time()

        arrival_times.append(arrival)
        service_times.append(service)

        # service starts when server is free and customer arrives
        start_service = max(arrival, current_time)

        wait = start_service - arrival
        end_service = start_service + service

        system_time = end_service - arrival

        waiting_times.append(wait)
        system_times.append(system_time)

        current_time = end_service

    return waiting_times, system_times

# Run Simulation
waiting, system = simulate()

# Simple Analysis
print("Average waiting time:", sum(waiting) / len(waiting))
print("Max waiting time:", max(waiting))
print("Min waiting time:", min(waiting))
