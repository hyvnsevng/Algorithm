import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]
if n < 3:
    print(sum(wines))
else:
    dp = [[0, 0] for _ in range(n)]       # i번째O/i번째X
    for i in range(n):
        if i < 2:
            dp[i] = [sum(wines[:i+1]), sum(wines[:i+1]) - wines[i]]
        else:
            dp[i][0] = max(dp[i-2][0] + wines[i], dp[i-2][1] + wines[i-1] + wines[i])
            dp[i][1] = max(dp[i-1][0], dp[i-2][0])

    print(max(dp[n-1]))