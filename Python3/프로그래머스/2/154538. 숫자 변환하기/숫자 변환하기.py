def solution(x, y, n):
    dp = [-1] * (y + 1)
    dp[x] = 0
    for i in range(x, y + 1):
        curr = dp[i]
        if curr == -1:
            continue
        doubled, trippled, added = i * 2, i * 3, i + n
        if doubled <= y:
            if dp[doubled] == -1 or dp[doubled] > curr + 1:
                dp[doubled] = curr + 1
        if trippled <= y:
            if dp[trippled] == -1 or dp[trippled] > curr + 1:
                dp[trippled] = curr + 1
        if added <= y:
            if dp[added] == -1 or dp[added] > curr + 1:
                dp[added] = curr + 1
    
    return dp[y]
