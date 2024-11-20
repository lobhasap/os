def isSafe(processes, avail, max_resources, allot, n, m):
    work = avail[:]
    finish = [False] * n
    safe_seq = []

    count = 0
    while count < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(max_resources[i][j] - allot[i][j] <= work[j] for j in range(m)):
                    for k in range(m):
                        work[k] += allot[i][k]
                    safe_seq.append(processes[i])
                    finish[i] = True
                    found = True
                    count += 1

        if not found:
            print("System is not in a safe state.")
            return False

    print("System is in a safe state.")
    print("Safe sequence:", " -> ".join(f"P{p}" for p in safe_seq))
    return True


def main():
    n = int(input("Enter the number of processes: "))
    m = int(input("Enter the number of resource types: "))

    processes = list(range(n))

    avail = list(map(int, input("Enter available resources: ").split()))

    max_resources = []
    print("Enter maximum resources for each process:")
    for i in range(n):
        max_resources.append(list(map(int, input(f"P{i}: ").split())))

    allot = []
    print("Enter allocated resources for each process:")
    for i in range(n):
        allot.append(list(map(int, input(f"P{i}: ").split())))

    isSafe(processes, avail, max_resources, allot, n, m)


if __name__ == "__main__":
    main()