DIVIDE = 1000000007

n = int(input())
spicy = list(map(int, input().split()))
spicy.sort()

ans = 0
for interval in range(1, n):    # 길이
    tmp = 0
    for start in range(n-interval):    # 시작 idx
        tmp += spicy[start+interval] - spicy[start]
    ans += tmp * 2**(interval-1)

print(ans % DIVIDE)