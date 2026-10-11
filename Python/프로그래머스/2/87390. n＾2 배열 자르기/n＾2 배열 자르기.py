def solution(n, left, right):
    answer = [max(x // n, x % n) + 1 for x in range(left, right + 1)]
    return answer
