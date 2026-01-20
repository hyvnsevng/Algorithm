import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0, 0] for _ in range(n)]
    for i in range(len(dp)):
        if i == 0:
            dp[i][0] = stickers[0][i]
            dp[i][1] = stickers[1][i]
        elif i == 1:
            dp[i][0] = dp[i-1][1] + stickers[0][i]
            dp[i][1] = dp[i-1][0] + stickers[1][i]
        else:
            for j in range(2):
                dp[i][j] = max(dp[i-1][not j], dp[i-2][not j]) + stickers[j][i]
    

    print(max(dp[n-1]))
