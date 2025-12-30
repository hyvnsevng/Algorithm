import sys
input = sys.stdin.readline

INF = 10**9

n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]

FULL = (1 << n) - 1

dp = [[INF] * n for _ in range(1 << n)]
dp[1 << 0][0] = 0  # 0에서 출발

for mask in range(1, 1 << n):
    for i in range(n):
        # i가 포함되는 mask만 봄
        if not (mask & (1 << i)):
            continue
        cur = dp[mask][i]
        # 만약 mask를 방문하여 i까지 오는 경우가 없다면 skip
        if cur == INF:
            continue

        # i -> j로 이동
        for j in range(n):
            if mask & (1 << j): # j를 이미 방문했다면 skip
                continue
            if W[i][j] == 0:    # i -> j로 가는 길이 없다면 skip
                continue

            nmask = mask | (1 << j)
            nd = cur + W[i][j]
            # 최소값 갱신
            if nd < dp[nmask][j]:
                dp[nmask][j] = nd

# 0으로 되돌아오는 cost 포함해서 최솟값 찾기
ans = INF
for i in range(1, n):
    if W[i][0] > 0:
        ans = min(ans, dp[FULL][i] + W[i][0])

print(ans)
