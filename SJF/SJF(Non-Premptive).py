def sjf(parameters):
    n = len(parameters)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    remaining = list(parameters)
    gantt = []
    current_time = 0

    while remaining:
        # INDENTED: Everything inside the while loop must be indented
        available = [p for p in remaining if p[1] <= current_time]

        # CPU idle: jump to next arrival
        if not available:
            next_arrival = min(p[1] for p in remaining)
            gantt.append(("IDLE", current_time, next_arrival))
            current_time = next_arrival
            continue

        chosen = min(available, key=lambda p: (p[2], p[1], p[0]))

        start = current_time
        current_time = current_time + chosen[2]
        gantt.append((chosen[0], start, current_time))

        i = parameters.index(chosen)
        completion_time[i] = current_time
        turnaround_time[i] = completion_time[i] - chosen[1]
        waiting_time[i] = turnaround_time[i] - chosen[2]

        remaining.remove(chosen)

    return {
        'process_id': parameters,
        'completion_time': completion_time,
        'turnaround_time': turnaround_time,
        'waiting_time': waiting_time,
        'gantt': gantt
    }


parameters = [
    ('P1', 3, 3), ('P2', 2, 1), ('P3', 5, 2),
    ('P4', 0, 3), ('P5', 1, 2)
]

result = sjf(parameters)

print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
for i, (pid, arrival, burst) in enumerate(result['process_id']):
    print(f"{pid}\t{arrival}\t{burst}\t{result['completion_time'][i]}\t\t"
          f"{result['turnaround_time'][i]}\t\t{result['waiting_time'][i]}")

print("\nGantt Chart:")
for name, start, end in result['gantt']:
    print(f"[{name}: {start}->{end}]", end=" ")
print()

avg_turnaround_time = sum(result['turnaround_time']) / len(result['turnaround_time'])
avg_waiting_time = sum(result['waiting_time']) / len(result['waiting_time'])

print(f"\nAverage Turnaround Time: {avg_turnaround_time}")
print(f"Average Waiting Time: {avg_waiting_time}")