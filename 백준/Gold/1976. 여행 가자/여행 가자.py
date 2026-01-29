import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[0] * (n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
parents = [_ for _ in range(n+1)]


def find(x):
    if x == parents[x]:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x1, y1 = find(x), find(y)
    if x1 < y1:
        parents[y1] = x1
    else:
        parents[x1] = y1



for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] and find(i) != find(j):
            union(i, j)

sg = find(plan[0])
for city in plan:
    if sg != find(city):
        print("NO")
        break
else:
    print("YES")
