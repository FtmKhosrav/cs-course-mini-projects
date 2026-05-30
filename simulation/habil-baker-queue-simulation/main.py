import random


# Interarrival time distribution
def generate_interarrival_time():
    probabilities = [0.10, 0.20, 0.35, 0.20, 0.15]
    cumulative = [0.10, 0.30, 0.65, 0.85, 1.00]

    r = random.random()

    for i, p in enumerate(cumulative):
        if r <= p:
            return i + 1


# Habil service time distribution
def generate_habil_service_time():
    probabilities = [0.30, 0.30, 0.25, 0.15]
    cumulative = [0.30, 0.60, 0.85, 1.00]

    r = random.random()

    for i, p in enumerate(cumulative):
        if r <= p:
            return i + 3


# Baker service time distribution
def generate_baker_service_time():
    probabilities = [0.35, 0.25, 0.20, 0.20]
    cumulative = [0.35, 0.60, 0.80, 1.00]

    r = random.random()

    for i, p in enumerate(cumulative):
        if r <= p:
            return i + 3


NUM_CUSTOMERS = 30

customers = []

current_arrival_time = 0

habil_available_time = 0
baker_available_time = 0

habil_busy_time = 0
baker_busy_time = 0

for customer_id in range(1, NUM_CUSTOMERS + 1):

    # Generate arrival time
    current_arrival_time += generate_interarrival_time()

    # Assign customer to the first available server
    if habil_available_time <= baker_available_time:
        server = "Habil"

        service_time = generate_habil_service_time()

        service_start = max(
            current_arrival_time,
            habil_available_time
        )

        waiting_time = service_start - current_arrival_time

        service_end = service_start + service_time

        habil_available_time = service_end
        habil_busy_time += service_time

    else:
        server = "Baker"

        service_time = generate_baker_service_time()

        service_start = max(
            current_arrival_time,
            baker_available_time
        )

        waiting_time = service_start - current_arrival_time

        service_end = service_start + service_time

        baker_available_time = service_end
        baker_busy_time += service_time

    customers.append({
        "customer": customer_id,
        "arrival": current_arrival_time,
        "server": server,
        "service_time": service_time,
        "waiting_time": waiting_time,
        "end_time": service_end
    })

simulation_end_time = max(
    habil_available_time,
    baker_available_time
)

average_waiting_time = (
    sum(c["waiting_time"] for c in customers)
    / NUM_CUSTOMERS
)

average_service_time = (
    sum(c["service_time"] for c in customers)
    / NUM_CUSTOMERS
)

habil_utilization = (
    habil_busy_time / simulation_end_time
) * 100

baker_utilization = (
    baker_busy_time / simulation_end_time
) * 100

print("=== Habil & Baker Queue Simulation ===\n")

print(f"Customers Served: {NUM_CUSTOMERS}")
print(f"Average Waiting Time: {average_waiting_time:.2f} minutes")
print(f"Average Service Time: {average_service_time:.2f} minutes")
print(f"Habil Utilization: {habil_utilization:.2f}%")
print(f"Baker Utilization: {baker_utilization:.2f}%")

print("\nCustomer Details:")
print("-" * 70)

for customer in customers:
    print(
        f"Customer {customer['customer']:2d} | "
        f"Server: {customer['server']:5s} | "
        f"Arrival: {customer['arrival']:3d} | "
        f"Service: {customer['service_time']} | "
        f"Wait: {customer['waiting_time']:2d}"
    )
