import matplotlib.pyplot as plt

def SJFNonPreemptive(n, pid, at, bt):
    ct = [0] * n  # Completion times
    tt = [0] * n  # Turnaround times
    wt = [0] * n  # Waiting times
    tottt = 0      # Total turnaround time
    totwt = 0       # Total waiting time
    gantt_chart = []  # To store process execution (pid, start_time, duration)

    # Sort processes by burst time only (ignoring arrival time)
    processes = sorted(zip(pid, at, bt), key=lambda x: x[2])
    pid, at, bt = zip(*processes)

    # Scheduling logic
    current_time = 0
    completed = 0
    is_completed = [False] * n

    while completed != n:
        # Find the process with the shortest burst time that has arrived
        index = -1
        shortest_bt = float('inf')

        for i in range(n):
            if not is_completed[i] and bt[i] < shortest_bt:
                shortest_bt = bt[i]
                index = i

        if index == -1:
            current_time += 1  # If no process is available, increment time
        else:
            # Calculate start time and completion time
            start_time = max(current_time, at[index])
            current_time = start_time + bt[index]
            ct[index] = current_time
            tt[index] = ct[index] - at[index]
            wt[index] = tt[index] - bt[index]
            tottt += tt[index]
            totwt += wt[index]

            # Mark process as completed
            is_completed[index] = True
            completed += 1

            # Add to Gantt chart
            gantt_chart.append((pid[index], start_time, bt[index]))

    # Output Process Information
    print("\nProcess ID | AT | BT | CT | TT | WT")
    for i in range(n):
        print(f" {pid[i]}         {at[i]}  {bt[i]}  {ct[i]}   {tt[i]}   {wt[i]}")

    # Averages
    print(f"\nAverage Turnaround Time: {tottt / n:.2f}")
    print(f"Average Waiting Time: {totwt / n:.2f}")

    # Textual Gantt Chart
    print("\nGantt Chart")
    print("|", end="")
    for process, start, duration in gantt_chart:
        print(f" P{process} {' ' * duration}|", end="")
    print("\n")

    # Visual Gantt Chart
    plt.figure(figsize=(10, 3))
    for process, start, duration in gantt_chart:
        plt.barh(y=0, width=duration, left=start, edgecolor='black', label=f"P{process}" if gantt_chart[0][0] == process else "")
        plt.text(start + duration / 2, 0, f"P{process}", ha='center', va='center', color='white', fontsize=10)

    plt.yticks([])  # Remove y-axis ticks
    plt.xlabel("Time")
    plt.title("Gantt Chart - SJF Non-Preemptive Scheduling")
    plt.legend(loc='upper right')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

# Example usage
n = 3
pid = [1, 2, 3]
at = [0, 1, 2]  # Arrival times
bt = [10, 5, 8]  # Burst times

SJFNonPreemptive(n, pid, at, bt)
