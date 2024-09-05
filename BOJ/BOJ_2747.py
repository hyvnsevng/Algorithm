def dp(n):
    if not table[n]:
        if n == 0:
            table[n] = 0
        elif n == 1 or n == 2:
            table[n] = 1
        else:
            table[n] = dp(n-1) + dp(n-2)

    return table[n]


n = int(input())
table = [0 for _ in range(n+1)]
print(dp(n))
