import itertools
import sys

sys.stdin = open('sample_input.txt')


def solution(depth):
    global count, n, k

    if depth == n:
        result = 0
        for i in range(n):
            if visited[i]:
                result += lst[i]
        if result == k:
            count += 1
        return

    visited[depth] = True
    solution(depth + 1)
    visited[depth] = False
    solution(depth + 1)


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    visited = [False] * n
    count = 0

    solution(0)

    print(f'#{tc} {count}')
