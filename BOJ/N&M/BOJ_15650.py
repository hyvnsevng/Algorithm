def func(x, y, arr):
    if x == m+1:
        answer.append(arr)
    for i in range(y, n+1):
        func(x+1, i+1, arr+[i])


n, m = map(int, input().split())
answer = []
func(1, 1, [])
for ans in answer:
    print(*ans)


