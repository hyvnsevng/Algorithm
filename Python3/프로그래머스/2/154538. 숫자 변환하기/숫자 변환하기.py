def solution(x, y, n):
    limit = 1000000
    dp = [limit] * (3 * limit + 1)
    dp[x] = 0
    for i in range(x, y + 1):
        curr = dp[i]
        dp[i * 2] = min(dp[i * 2], curr + 1)
        dp[i * 3] = min(dp[i * 3], curr + 1)
        dp[i + n] = min(dp[i + n], curr + 1)
    
    return -1 if dp[y] == limit else dp[y]
