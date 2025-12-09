def main(n):
    
    if n < 4:
        return 0
    
    MOD = 10007
    dp = [[0]*14 for _ in range(n+1)] # dp[i][j] : 4j개 카드 중 i장을 뽑았을 때 포카드가 없는 경우
    dp[0][0] = 1

    for j in range(1, 14):  # 1~13 중 하나의 숫자 * 4개 문양
        for i in range(0, n+1):
            val = 0
            for t in range(4):  # 1~13 중 몇개 뽑을건지
                if i - t < 0:
                    continue
                val += comb(4, t) * dp[i-t][j-1]
            dp[i][j] = val % MOD
                

    total = comb(52, n) % MOD
    result = (total - dp[n][13]) % MOD
    # print(dp)
    return result


def factorial(x):
    if x == 1 or x == 0:
        return 1
    return x*factorial(x-1)


def comb(n, r):
    if r > n or r < 0:
        return 0
    return factorial(n)//(factorial(n-r)*factorial(r))


N = int(input())
print(main(N))