import random

# Generate Customer Arrival Time
def generate_arrival_time():
    return random.uniform(1, 10)

# Generate Service Time
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

current_time = 0
server_free_time = 0

waiting_time_sum = 0

# Simulation Loop
for i in range(NUM_CUSTOMERS):

    # Generate arrival and service times
    inter_arrival = generate_arrival_time()
    arrival_time = current_time + inter_arrival

    service_time = generate_service_time()

    # Service starts when customer arrives or server becomes free
    start_time = max(arrival_time, server_free_time)

    # Waiting time
    waiting_time = start_time - arrival_time

    # Service end time
    end_time = start_time + service_time

    # Save customer data
    customers.append({
        "customer_id": i + 1,
        "arrival_time": arrival_time,
        "start_time": start_time,
        "end_time": end_time,
        "waiting_time": waiting_time,
        "service_time": service_time
    })

    waiting_time_sum += waiting_time

    # Update times
    current_time = arrival_time
    server_free_time = end_time

# Performance Analysis
average_waiting_time = waiting_time_sum / NUM_CUSTOMERS

max_waiting_time = max(c["waiting_time"] for c in customers)

# Approximate queue length
max_queue_length = 0

for t in range(int(server_free_time) + 1):
    queue_size = sum(
        1 for c in customers
        if c["arrival_time"] <= t < c["start_time"]
    )
    max_queue_length = max(max_queue_length, queue_size)

# Server utilization
busy_time = sum(c["service_time"] for c in customers)

utilization = (busy_time / server_free_time) * 100

# Display Results
print("\n=== Simulation Results ===")

print(f"Average Waiting Time: {average_waiting_time:.2f} minutes")
print(f"Maximum Waiting Time: {max_waiting_time:.2f} minutes")
print(f"Maximum Queue Length: {max_queue_length} customers")
print(f"Server Utilization: {utilization:.2f}%")

# Simulation Table
print("\n=== Customer Table ===")

header = f"{'ID':<5}{'Arrival':<12}{'Start':<12}{'End':<12}{'Wait':<12}"
print(header)

for c in customers:
    print(
        f"{c['customer_id']:<5}"
        f"{c['arrival_time']:<12.2f}"
        f"{c['start_time']:<12.2f}"
        f"{c['end_time']:<12.2f}"
        f"{c['waiting_time']:<12.2f}"
    )
