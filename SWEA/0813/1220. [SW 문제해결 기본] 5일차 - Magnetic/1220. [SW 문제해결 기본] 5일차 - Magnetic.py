import sys
from collections import deque

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    queue = deque()

    T_T = 0
    asdf = True

    for i in range(n):
        for j in range(n):
            mag = table[j][i]
            if queue:
                if queue[-1] == mag:
                    queue.append(table[j][i])




