MOD = 1000000007

n = int(input())
spicy = list(map(int, input().split()))
spicy.sort()
POWER = [0]*n

for i in range(1, n):
    POWER[i] = (2 * POWER[i-1] + 1) % MOD

ans = 0
for i in range(n):
    cnt = POWER[i] - POWER[n-i-1]
    if cnt < 0:
        cnt += MOD
    added = spicy[i] * cnt
    ans += added

print(ans % MOD)