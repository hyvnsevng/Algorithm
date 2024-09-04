def solution(k, n):
    if not dp[k][n-1]:
        if k == 0:
            dp[k][n-1] = n
        elif n == 1:
            dp[k][n - 1] = 1
        else:
            dp[k][n-1] = solution(k-1, n) + solution(k, n-1)

    return dp[k][n-1]


T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    dp = [[0 for _ in range(n)] for _ in range(k+1)]
    solution(k, n)
    print(dp[k][n-1])


    '''
    a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
    각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다
    k층 n호:
    k-1층 1~n호
    k-2층 1~n호        1 5 15 
    ...               1 4 10 20
    1층 1~n호          1 3 6 10
    0층 1~n호          1 2 3 4
    dp(k, n) = dp(k-1, n) + dp(k, n-1)
    '''