
cpu_schudule = [(3, 3),   # P1
        (2, 1),   # P2
        (5, 2),   # P3
        (0, 3),   # P4
        (1, 2)]   # P5


def fcfs(cpu_schedule):
    
    procs = [(f"P{i+1}", at, bt) for i, (at, bt) in enumerate(cpu_schedule)]

   
    order = sorted(procs, key=lambda p: (p[1], p[0]))

    time, results, gantt = 0, [], []

    for pid, at, bt in order:
       
        if time < at:
            gantt.append(("IDLE", time, at))
            time = at

start = time
        ct    = start + bt        # Completion Time
        tat   = ct - at           # Turnaround Time
        wt    = tat - bt          # Waiting Time

        gantt.append((pid, start, ct))
        results.append([pid, at, bt, ct, tat, wt])
        time = ct

    return results, gantt


def print_results(results):
    print(f"{'PID':<5}{'AT':>3}{'BT':>4}{'CT':>4}{'TAT':>5}{'WT':>4}")
    print("-" * 25)
    for pid, at, bt, ct, tat, wt in sorted(results):
        print(f"{pid:<5}{at:>3}{bt:>4}{ct:>4}{tat:>5}{wt:>4}")

    n = len(results)
    print("-" * 25)
    print(f"Average Turnaround Time = {sum(r[4] for r in results) / n:.2f}")
    print(f"Average Waiting Time    = {sum(r[5] for r in results) / n:.2f}")


def print_gantt(gantt):
    print("\nGantt Chart:")
    top, bottom = "", ""
    for pid, s, e in gantt:
        top    += f"| {pid:^4} "
        bottom += f"{s:<7}"
    top    += "|"
    bottom += str(gantt[-1][2])
    print(top)
    print(bottom)


if __name__ == "__main__":
    results, gantt = fcfs(cpu_schudule)
    print_results(results)
    print_gantt(gantt)
