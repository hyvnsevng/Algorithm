def solution(order):
    answer = 0
    n = order[-1]
    max_box_num = 0
    container = []
    for box in order:
        if box > max_box_num:
            container += [x for x in range(max_box_num + 1, box)]
            max_box_num = box
            answer += 1
        elif container and container[-1] == box:
            container.pop()
            answer += 1
        else:
            break
        
    return answer
