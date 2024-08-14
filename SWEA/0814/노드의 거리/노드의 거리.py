import sys
from collections import deque

sys.stdin = open('5102_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)

    start, end = map(int, input().split())

    queue = deque([[start, 0]])

    answer = 0

    while queue:
        vertex, distance = queue.popleft()
        visited[vertex] = True
        for node in adj[vertex]:
            if not visited[node]:
                queue.append([node, distance + 1])
                if node == end:
                    answer = distance + 1
                    break
        if answer:
            break

    print(f'#{tc} {answer}')

