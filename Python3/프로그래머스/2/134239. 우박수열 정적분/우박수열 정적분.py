def solution(k, ranges):
    answer = []
    arr = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        arr.append(k)
    
    n = len(arr)
    acc_sum = [0] * n
    for i in range(n - 1):
        acc_sum[i + 1] = acc_sum[i] + (arr[i + 1] + arr[i]) / 2
        
    for a, b in ranges:
        if n + b - 1 < a:
            answer.append(-1)
        else:
            answer.append(acc_sum[n + b - 1] - acc_sum[a])
        
    return answer
