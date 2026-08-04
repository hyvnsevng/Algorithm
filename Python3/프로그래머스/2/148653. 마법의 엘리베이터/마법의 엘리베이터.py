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
        
        # 0 떼기
        while floor % 10 == 0:
            floor //= 10
            
        # 두 자릿수 이상이면 버튼 누르고 스택에 추가 
        if floor > 10:            
            n_floor, diff = go_down(floor)
            stack.append((n_floor, cnt + diff))
            n_floor, diff = go_up(floor)
            stack.append((n_floor, cnt + diff))
        # 한 자릿수면 최소값 갱신
        else:
            answer = min(answer, cnt + min(floor, 10 - floor + 1))  # 기존 최소값, 내려가는 버튼만 누르기, 10까지 올라갔다 내려가기
        
    return answer