def solution(video_len, pos, op_start, op_end, commands):
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds
    def seconds_to_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"
    
    video_length = time_to_seconds(video_len)
    current_pos = time_to_seconds(pos)
    op_start_seconds = time_to_seconds(op_start)
    op_end_seconds = time_to_seconds(op_end)           
    
    for command in commands:
        if op_start_seconds <= current_pos <= op_end_seconds:
            current_pos = op_end_seconds
            print(seconds_to_time(current_pos))
            print(1)
        
        if command == "prev":
            current_pos = max(0, current_pos - 10)
            print(seconds_to_time(current_pos))
            print(2)
            
        elif command == "next":
            current_pos = min(video_length, current_pos + 10)
            print(seconds_to_time(current_pos))
            print(3)
        
        if op_start_seconds <= current_pos <= op_end_seconds:
                current_pos = op_end_seconds
                print(seconds_to_time(current_pos))
                print(1)
        
    return seconds_to_time(current_pos)
