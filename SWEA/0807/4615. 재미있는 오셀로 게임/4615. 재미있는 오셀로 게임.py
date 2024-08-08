import sys

sys.stdin = open('sample_input(1).txt')

def game(matrix, turn):
    print(turn)
    while turn:
        play = turn.pop()
        j = 1
        for i in range(8):
            player = play[2]
            change = []
            while True:
                nrow = play[0] + j * dr[i]
                ncol = play[1] + j * dc[i]
                if not(0 <= nrow < n and 0 <= ncol < n):
                    break
                if matrix[nrow][ncol] == 1+(player%2):
                    change.append([nrow, ncol])
                    j += 1
                elif j>1 and matrix[nrow][ncol] == player:
                    for coor in change:
                        matrix[coor[0]][coor[1]] = player
                    break

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