n, k = map(int, input().split())

dp = [0] * (k+1)
dp[0] = 1
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

for coin in coins:
    if coin > k:
        continue

    for i in range(coin, k + 1):
        dp[i] += dp[i-coin]

print(dp[k])