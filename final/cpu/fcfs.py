import matplotlib.pyplot as plt

def FCFS(n, pid, at, bt):
    # Sort processes by arrival time
    processes = sorted(zip(pid, at, bt), key=lambda x: x[1])
    pid, at, bt = zip(*processes)

    ct = [0] * n  # Completion times
    tt = [0] * n  # Turnaround times
    wt = [0] * n  # Waiting times
    tottt = 0  # Total Turnaround Time
    totwt = 0  # Total Waiting Time
    start_times = [0] * n  # Start times for Gantt chart

    # Completion Time Calculation
    for i in range(n):
        if i == 0:
            start_times[i] = at[i]  # First process starts at its arrival time
        else:
            start_times[i] = max(ct[i - 1], at[i])  # Start after the previous process or arrival time

        ct[i] = start_times[i] + bt[i]
        tt[i] = ct[i] - at[i]
        wt[i] = tt[i] - bt[i]
        tottt += tt[i]
        totwt += wt[i]

    # Output Process Information
    print("\nProcess ID | AT | BT | CT | TT | WT")
    for i in range(n):
        print(f" {pid[i]}       {at[i]}   {bt[i]}   {ct[i]}   {tt[i]}   {wt[i]}")

    # Averages
    print(f"\nAverage Turnaround Time: {tottt / n:.2f}")
    print(f"Average Waiting Time: {totwt / n:.2f}")

    # Visual Gantt Chart
    plt.figure(figsize=(10, 3))
    for i in range(n):
        plt.barh(y=0, width=bt[i], left=start_times[i], edgecolor='black', label=f"P{pid[i]}" if i == 0 else "")
        plt.text(start_times[i] + bt[i] / 2, 0, f"P{pid[i]}", ha='center', va='center', color='white', fontsize=10)

    plt.yticks([])
    plt.xlabel("Time")
    plt.title("Gantt Chart - FCFS Scheduling")
    plt.legend(loc='upper right')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

# Input Data
n = 4
pid = [1, 2, 3, 4]
at = [0, 1, 5, 6]
bt = [2, 2, 3, 4]
FCFS(n, pid, at, bt)
