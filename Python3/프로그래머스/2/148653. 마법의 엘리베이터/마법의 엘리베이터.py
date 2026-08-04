def go_up(floor):
    diff = 10 - (floor % 10)
    return ((floor + diff) // 10 , diff)


def go_down(floor):
    diff = floor % 10
    return ((floor - diff) // 10, diff)


def solution(storey):
    answer = 100
    stack = [(storey, 0)]
    while stack:
        floor, cnt = stack.pop()
        
        while floor % 10 == 0:
            floor //= 10
            
        if floor > 10:            
            n_floor, diff = go_down(floor)
            stack.append((n_floor, cnt + diff))
            n_floor, diff = go_up(floor)
            stack.append((n_floor, cnt + diff))
        else:
            answer = min(answer, cnt + min(floor, 10 - floor + 1))
        
    return answer