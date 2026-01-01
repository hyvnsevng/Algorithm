dx, dy = [1, 1, -1, -1], [1, -1, 1, -1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

bishops = [[], []]
for i in range(n):
    for j in range(n):
        if board[i][j]:
            bishops[(i + j) % 2].append((i, j))

ans = [0, 0]


def dfs(color, idx, tmp):
    if ans[color] < tmp:
        ans[color] = tmp
    
    l = len(bishops[color]) - 1
    if tmp + l - idx < ans[color] or idx > l:
        return
    
    x, y = bishops[color][idx]
    # print(x, y, tmp)
    
    if not catch_me(x, y):
        board[x][y] = -1
        dfs(color, idx + 1, tmp + 1)
        board[x][y] = 1
    dfs(color, idx + 1, tmp)


def catch_me(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        while 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == -1:
                return True
            nx += dx[i]
            ny += dy[i]
        
    return False


def rollback(x, y):
    board[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        while 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] > 1:
                board[nx][ny] -= 1
            nx += dx[i]
            ny += dy[i]


dfs(0, 0, 0)
dfs(1, 0, 0)
print(sum(ans))