def solution(n):
    nums = '124'
    answer = ''
    d = 3
    while n > 0:
        rem = (n - 1) % d
        idx = rem // (d // 3)
        answer += nums[idx]
        n -= d
        d *= 3
    return answer[::-1]