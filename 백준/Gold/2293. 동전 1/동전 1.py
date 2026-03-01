n, k = map(int, input().split())
dp = [0]*(k+1)
dp[0] = 1
for _ in range(n):
    coin = int(input())
    for price in range(0, k-coin+1):
        dp[price+coin] += dp[price]

print(dp[k])