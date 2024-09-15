# 백준 1966번 프린터 큐

from collections import deque

T = int(input())
for tc in range(T):
    m, n = map(int, input().split())
    lst = list(map(int, input().split()))

    q = deque()
    for i in range(m):
        q.append([lst[i], i])

    count = 0
    while True:
        v, idx = q.popleft()
        for imp in q:
            if imp[0] > v:
                q.append([v, idx])
                break
        else:
            count += 1
            if idx == n:
                break

    print(count)
