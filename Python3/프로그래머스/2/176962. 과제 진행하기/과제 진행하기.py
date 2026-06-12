def convert_time(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)


def solution(plans):
    answer = [] 
    plans.sort(key=lambda x: convert_time(x[1]))
    stack = []
    last_end = convert_time(plans[0][1])    # 마지막 과제 시간 
    
    for name, start, playtime in plans:
        # 현재 시간
        curr = convert_time(start)
        
        # 현재 시간까지 과제들 처리
        while stack:
            fin_name, fin_time = stack.pop()
            
            # 과제 마무리 시간이 현재 시간 이후라면 스택, 시간 갱신 후 반복 탈출
            if fin_time + last_end > curr:
                stack.append((fin_name, fin_time + last_end - curr))
                last_end = curr
                break
                
            answer.append(fin_name)
            last_end += fin_time
        
        # 스택에 현재 과제 push
        stack.append((name, int(playtime)))
        last_end = curr
        
    # 스택 털기
    while stack:
        name, _ = stack.pop()
        answer.append(name)
        
    return answer