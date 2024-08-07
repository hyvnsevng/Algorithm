import sys

sys.stdin = open('sample_input(1).txt')

def game(matrix, turn):
    print(turn)
    while turn:
        play = turn.pop()
        for i in range(8):
            nrow1 = play[0] + dr[i]*2
            ncol1 = play[1] + dc[i]*2
            nrow2 = play[0] + dr[i]
            ncol2 = play[1] + dc[i]
            player = play[2]
            if 0 <= nrow1 < n and 0 <= ncol1 < n and matrix[nrow2][ncol2] == 1+(player%2) and matrix[nrow1][ncol1] == player:
                matrix[nrow1][ncol1] = player
                matrix[nrow2][ncol2] = player

    black = 0
    white = 0
    for row in matrix:
        for col in row:
            if col == 1:
                black += 1
            elif col == 2:
                white += 1

    for row in matrix:
        print(row)

    return black, white

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(int, input().split()) # n X n 판에서 m번 돌 놓기

    othello = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(2):
        othello[n//2-i][n//2-i] = 2
        othello[n//2-i][n//2-1+i] = 1

    for row in othello:
        print(*row)


    dr = [1, -1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, 1, -1, 1, -1, 1, -1]

    dol = [0 for _ in range(m)]
    for i in range(m-1, -1, -1):
        col, row, player = map(int, input().split())
        dol[i] = [row-1, col-1, player]

    result = game(othello, dol)
    print(f'#{tc} {result}')