def solution(queue1, queue2):
    double_queue = queue1 + queue2
    n = len(double_queue) // 2
    qs = sum(double_queue) // 2
    acc_sum = [0]
    for i in range(n * 2):
        acc_sum.append(acc_sum[i] + double_queue[i])
        
    MAX = 20e9
    answer = MAX
    l, r = 0, 1
    while l < r < len(double_queue):
        tmp = acc_sum[r] - acc_sum[l]
        if tmp > qs:
            l += 1
        elif tmp < qs:
            r += 1
        else:
            if r >= n:
                answer = min(answer, l + r - n)
            else:
                answer = min(answer, l + r + n)
            l += 1
            r += 1

    if answer == MAX:
        return -1
    return answer
