def scan_left_scheduling(requests, initial_head, disk_end=0):
   
   
    left_requests = sorted([r for r in requests if r <= initial_head], reverse=True)
    right_requests = sorted([r for r in requests if r > initial_head])
    
    
    max_request = max(requests)
    seek_sequence = [initial_head] + left_requests + [disk_end] + [max_request]
    

    total_seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) 
                          for i in range(len(seek_sequence) - 1))
                          
    print(f"Left SCAN Seek Sequence: {' -> '.join(map(str, seek_sequence))}")
    print(f"Total Head Movement: {total_seek_time} cylinders")
    return total_seek_time

request_queue = [55, 58, 39, 18, 90, 160, 150, 38, 184]
head_start = 100


scan_left_scheduling(request_queue, head_start, disk_end=0)