n = int(input())
lst = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    tmp = dp[i]
    for j in range(i):
        if lst[i] > lst[j] and dp[j] >= tmp:
            tmp = dp[j]
    dp[i] = tmp + 1

print(max(dp))
