# 2491번 수열

n = int(input())
lst = list(map(int, input().split()))

ascending = 1
descending = 1
max_len = 0

for i in range(n-1):
    if lst[i+1] > lst[i]:
        ascending += 1
        if descending > max_len:
            max_len = descending
        descending = 1
    elif lst[i+1] < lst[i]:
        descending += 1
        if ascending > max_len:
            max_len = ascending
        ascending = 1
    else:
        ascending += 1
        descending += 1

length = max(ascending, descending)
if length > max_len:
    max_len = length

print(max_len)

