# 백준 15468번 퇴사 2

# T: 걸리는 시간
# P: 받는 금액

import sys

n = int(input())

dp = [0]*(n+1)
table = []
for _ in range(n):
    t, p = map(int, sys.stdin.readline().split())
    table.append([t, p])


for day in range(n-1, -1, -1):
    t, p = table[day]
    if day + t <= n and p + dp[day] > dp[day + t]:
        for i in range(day + t, n):
            dp[i] = dp[day] + p

print(dp)