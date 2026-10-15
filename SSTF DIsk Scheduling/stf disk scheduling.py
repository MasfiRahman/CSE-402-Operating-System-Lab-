def sstf(requests, head):
	requests = requests.copy()
	total_seek = 0
	seek_sequence = []
	current_head = head

	while requests:
		closest = min(requests, key=lambda x: abs(x - current_head))

		total_seek += abs(closest - current_head)
		current_head = closest

		seek_sequence.append(closest)
		requests.remove(closest)

	print("Seek Sequence:", seek_sequence)
	print("Total Head Movement:", total_seek)

head = 50

requests = [60, 20, 100, 10, 15, 22, 42]

sstf(requests, head)