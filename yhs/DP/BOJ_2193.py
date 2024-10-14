# 백준 2193번 이친수

def dp(n):
    if not table[n]:
        if n == 0:
            table[n] = 1
        elif n == 1:
            table[n] = 1
        elif n == 2:
            table[n] = 2
        else:
            table[n] = dp(n-1) + dp(n-2)
    return table[n]


N = int(input())
table = [0 for _ in range(N)]
print(dp(N-1))

