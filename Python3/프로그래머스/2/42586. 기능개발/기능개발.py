import math

def calc_day(progress, speed):
    return math.ceil((100 - progress) / speed)

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    day, size = 0, 0 
    for i in range(n):
        t_day = calc_day(progresses[i], speeds[i])
        if size == 0:
            day = t_day
            size += 1
        elif day >= t_day:
            size += 1
        else:
            answer.append(size)
            size = 1
            day = t_day
    else:
        answer.append(size)
        
    return answer