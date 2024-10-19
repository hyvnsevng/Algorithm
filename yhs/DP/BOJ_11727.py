# 백준 11727번 2xn 타일링 2

# 2xn 직사각형을 채우는 경우의 수를 f(n)이라고 할 때, 점화식은 f(n) = f(n-1) + 2 * f(n-2)
# n-1개를 채우고 2x1 타일을 하나 붙이는 경우 + n-2개를 채우고 1x2 두 개 or 2x2 하나를 붙이는 경우

def dp(n):
    if not table[n]:
        if n == 1:
            table[n] = 1
        elif n == 2:
            table[n] = 3
        else:
            table[n] = dp(n-1) + 2*dp(n-2)

    return table[n] % 10007


n = int(input())
table = [0 for _ in range(n+1)]
print(dp(n))
