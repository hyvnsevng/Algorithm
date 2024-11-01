# 백준 17626번 Four Squares

# 제곱수가 아닌 n을 최소 개수의 제곱수로 나타내려면 n - k**2 (n - k**2 는 자연수)를 나타내는 최소 개수의 제곱수에 1을 더한 것과 같다.
# dp를 사용했지만 pypy로만 통과. python으로는 시간초과가 발생했다.
# python으로 통과하려면 어떻게 풀이해야 할지 생각해보자.

def dp(n):
    if not table[n]:
        ans = 4
        for i in range(1, int(n ** 0.5+1)):
            ans = min(ans, dp(n-i**2) + 1)
        table[n] = ans

    return table[n]


n = int(input())
table = [0 if _ ** 0.5 % 1 else 1 for _ in range(n+1)]

for i in range(1, n+1):
    dp(i)

print(dp(n))
