import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(node):
    if visited[node] == 1:
        nxt = students[node]
        res = 0
        while nxt != node:
            res += 1
            nxt = students[nxt]
        return res + 1
    if visited[node] == 2:
        return 0

    visited[node] = 1
    r = dfs(students[node])
    visited[node] = 2
    return r



T = int(input())
for tc in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(n+1)]
    ans = 0
    for i in range(1, n+1):
        if not visited[i]: ans += dfs(i)
    print(n - ans)