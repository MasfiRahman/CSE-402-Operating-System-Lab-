def fcfs_scheduling(requests, initial_head):
  
    total_seek_time = 0
    current_position = initial_head
    seek_sequence = [current_position]
    
    print(f"Initial Head Position: {current_position}")
    print("Processing Requests...")
    
    for request in requests:
        # Calculate distance and add to total seek time
        distance = abs(current_position - request)
        total_seek_time += distance
        
        # Move head to the new request position
        current_position = request
        seek_sequence.append(current_position)
        
    print(f"\nSeek Sequence: {' -> '.join(map(str, seek_sequence))}")
    print(f"Total Head Movement: {total_seek_time} cylinders")
    
    return total_seek_time

request_queue = [55, 58, 39, 18, 90, 160, 150, 38, 184]
head_start = 100

fcfs_scheduling(request_queue, head_start)