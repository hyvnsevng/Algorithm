from collections import deque

n, m = map(int, input().split())

campus = [list(input()) for _ in range(n)]

start = [-1, -1]
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            start = [i, j]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
ans = 0
q = deque([start])
while q:
    v = q.popleft()
    for i in range(4):
        x = dx[i] + v[0]
        y = dy[i] + v[1]
        if 0 <= x < n and 0 <= y < m and campus[x][y] != 'X':
            q.append([x, y])
            if campus[x][y] == 'P':
                ans += 1
            campus[x][y] = 'X'

if ans:
    print(ans)
else:
    print('TT')
