def func(x, y, arr):
    global n, m
    if x == m:
        answer.append(arr)
        return
    for i in range(y, n+1):
        func(x+1, i, arr+[i])


n, m = map(int, input().split())
answer = []
func(0, 1, [])
for ans in answer:
    print(*ans)