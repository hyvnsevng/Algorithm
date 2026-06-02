def solution(info, n, m):
    INF = 120
    dp = [INF] * n
    dp[0] = 0
    
    for da, db in info:
        for a in range(n-1, -1, -1):
            if dp[a] == INF:
                continue
                
            cur_b = dp[a]
            
            # A가 훔치는 경우
            if a + da < n:
                dp[a + da] = min(dp[a + da], cur_b)
                
            # B가 훔치는 경우
            dp[a] = cur_b + db
    
    for b in range(n):
        if dp[b] < m:
            return b
    return -1