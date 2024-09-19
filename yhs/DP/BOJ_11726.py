def dp(k):
    if not table[k]:
        if k == 1:
            table[k] = 1
        elif k == 2:
            table[k] = 2
        else:
            table[k] = dp(k-1) + dp(k-2)

    return table[k]


n = int(input())
table = [0]*(n+1)

print(dp(n) % 10007)
