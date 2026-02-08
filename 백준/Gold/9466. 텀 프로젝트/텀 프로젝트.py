import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    indegree = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        indegree[students[i]] += 1
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        curr = q.popleft()
        nxt = students[curr]
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

    print(n-sum(indegree))
