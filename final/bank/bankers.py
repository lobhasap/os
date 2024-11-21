def is_safe(available, max_demand, allocation, need, num_processes, num_resources):
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        allocated_in_this_round = False
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                for j in range(num_resources):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_sequence.append(i)
                allocated_in_this_round = True

        if not allocated_in_this_round:
            return False, []

    return True, safe_sequence

def main():
    num_processes = int(input("Enter number of processes: "))
    num_resources = int(input("Enter number of resources: "))

    available = list(map(int, input("Enter available resources (space-separated): ").split()))

    max_demand = []
    print("Enter max demand matrix:")
    for i in range(num_processes):
        max_demand.append(list(map(int, input(f"Process {i}: ").split())))

    allocation = []
    print("Enter allocation matrix:")
    for i in range(num_processes):
        allocation.append(list(map(int, input(f"Process {i}: ").split())))

    need = []
    for i in range(num_processes):
        need.append([max_demand[i][j] - allocation[i][j] for j in range(num_resources)])

    safe, safe_sequence = is_safe(available, max_demand, allocation, need, num_processes, num_resources)

    if safe:
        print("System is in a safe state.")
        print("Safe sequence:", " -> ".join(f"P{p}" for p in safe_sequence))
    else:
        print("System is not in a safe state.")

if __name__ == "__main__":
    main()
