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

# 마지막 날의 일정부터 체크
for day in range(n-1, -1, -1):
    t, p = table[day]

    if day + t <= n:    # 상담 일정이 퇴사 전에 끝난다면
        dp[day] = max(dp[day + t] + p, dp[day + 1])     # DP테이블을 당일값 + p와 익일값 중 큰 값으로 갱신
    else:
        dp[day] = dp[day+1]

print(max(dp))
