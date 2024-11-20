import matplotlib.pyplot as plt

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    gantt = []

    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        start_time = current_time
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        gantt.append((process.pid, start_time, process.completion_time))
        current_time += process.burst_time

        print(f"Process {process.pid}: Completion Time = {process.completion_time}, "
              f"Turnaround Time = {process.turnaround_time}, Waiting Time = {process.waiting_time}")

    draw_gantt_chart(gantt)

def draw_gantt_chart(gantt):
    fig, gnt = plt.subplots()
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Process ID')
    gnt.set_yticks([i for i in range(len(gantt))])
    gnt.set_yticklabels([f'P{g[0]}' for g in gantt])
    for idx, (pid, start, end) in enumerate(gantt):
        gnt.broken_barh([(start, end - start)], (idx - 0.4, 0.8), facecolors='tab:blue')
    plt.show()

# Example
processes = [Process(1, 0, 2), Process(2, 1, 2), Process(3, 5, 3), Process(4, 6, 4)]
fcfs(processes)
