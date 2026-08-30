def round_robin(parameters, quantum):
    n = len(parameters)
    pid = [p[0] for p in parameters]
    arrival = [p[1] for p in parameters]
    burst = [p[2] for p in parameters]
    remaining = burst.copy()

    completion = [0] * n
    turnaround = [0] * n
    waiting = [0] * n
    response = [0] * n
    first_run = [-1] * n

    order = sorted(range(n), key=lambda i: (arrival[i], pid[i]))
    queue = []
    gantt = []
    current_time = 0
    completed = 0
    ptr = 0

    while completed < n:
        # CPU idle: jump to next arrival
        if not queue:
            current_time = max(current_time, arrival[order[ptr]])
            queue.append(order[ptr])
            ptr += 1

        i = queue.pop(0)

        if first_run[i] == -1:
            first_run[i] = current_time
            response[i] = first_run[i] - arrival[i]

        # Run for at most one time quantum (preemption point)
        exec_time = min(quantum, remaining[i])
        start = current_time
        current_time += exec_time
        remaining[i] -= exec_time

        if gantt and gantt[-1][0] == pid[i] and gantt[-1][2] == start:
            gantt[-1] = (pid[i], gantt[-1][1], current_time)
        else:
            gantt.append((pid[i], start, current_time))

        # Newly arrived processes enter queue BEFORE current process re-joins
        while ptr < n and arrival[order[ptr]] <= current_time:
            queue.append(order[ptr])
            ptr += 1

        if remaining[i] == 0:
            completed += 1
            completion[i] = current_time
            turnaround[i] = completion[i] - arrival[i]
            waiting[i] = turnaround[i] - burst[i]
        else:
            queue.append(i)

    return {
        'pid': pid, 'arrival': arrival, 'burst': burst,
        'completion': completion, 'turnaround': turnaround,
        'waiting': waiting, 'response': response, 'gantt': gantt,
        'avg_tat': sum(turnaround) / n,
        'avg_wt': sum(waiting) / n,
        'avg_rt': sum(response) / n
    }


def display(r, name, quantum=None):
    title = name if quantum is None else f"{name} (Time Quantum = {quantum})"
    print(f"===== {title} =====")
    print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting\tResponse")
    for i in range(len(r['pid'])):
        print(f"{r['pid'][i]}\t{r['arrival'][i]}\t{r['burst'][i]}\t"
              f"{r['completion'][i]}\t\t{r['turnaround'][i]}\t\t"
              f"{r['waiting'][i]}\t\t{r['response'][i]}")
    print("Gantt Chart:")
    for p, s, e in r['gantt']:
        print(f"[{p}: {s}->{e}]", end=" ")
    print(f"\nAverage Turnaround Time: {round(r['avg_tat'], 2)}")
    print(f"Average Waiting Time: {round(r['avg_wt'], 2)}")
    print(f"Average Response Time: {round(r['avg_rt'], 2)}")


parameters = [
    ('P1', 0, 7), ('P2', 1, 4), ('P3', 2, 15),
    ('P4', 3, 11), ('P5', 4, 20), ('P6', 4, 9)
]

display(round_robin(parameters, 5), "Round Robin", 5)