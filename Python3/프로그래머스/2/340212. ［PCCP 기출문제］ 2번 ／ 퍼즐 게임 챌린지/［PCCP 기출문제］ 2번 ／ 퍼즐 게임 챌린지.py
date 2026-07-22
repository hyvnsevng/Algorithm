def check(level, diffs, times, limit):
    total_time = 0
    time_prev = 0
    for i in range(len(diffs)):
        diff = diffs[i]
        time_cur = times[i]
        if diff <= level:
            total_time += time_cur
        else:
            total_time += (time_cur + time_prev) * (diff - level) + time_cur
        time_prev = time_cur
    
    if total_time <= limit:
        return True
    return False
    
        
def solution(diffs, times, limit):
    answer = 0
    s, e = 1, 100000
    while s <= e:
        mid = (s + e) // 2
        if check(mid, diffs, times, limit):
            answer = mid
            e = mid - 1
        else:
            s = mid + 1
    return answer
