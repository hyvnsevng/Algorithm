def func(x, arr):
    global n, m
    if x == m:
        if arr not in answer:
            answer.add(arr)
        return
    for i in range(n):
        if not x:
            func(x+1, (lst[i], ))
        elif arr[-1] <= lst[i]:
            func(x+1, arr+(lst[i], ))


n, m = map(int, input().split())
lst = list(map(int, input().split()))
answer = set()
func(0, tuple())
answer = sorted(answer)
for ans in answer:
    print(*ans)