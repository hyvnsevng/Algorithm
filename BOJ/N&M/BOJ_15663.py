def func(x, arr):
    global n, m
    if x == m:
        if arr not in answer:
            answer.add(arr)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            func(x+1, arr+(lst[i], ))
            visited[i] = False


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False]*(n+1)
answer = set()
func(0, tuple())
answer = sorted(answer)
for ans in answer:
    print(*ans)