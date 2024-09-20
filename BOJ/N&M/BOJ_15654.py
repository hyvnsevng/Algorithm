def func(x, arr):
    global n, m
    if x == m:
        answer.append(arr)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            func(x+1, arr+[lst[i]])
            visited[i] = False


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False]*(n+1)
answer = []
func(0, [])
for ans in answer:
    print(*ans)