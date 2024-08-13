player = [list(map(int, input().split())) for _ in range(5)]
host = []
for _ in range(5):
    host.extend(list(map(int, input().split())))

player_t = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        v = player[i][j]    # 빙고판에 있는 숫자
        player[i][j] = host.index(v)
        player_t[j][i] = player[i][j]  # 전치


print(player, player_t)

when_bingo = []

diag1 = 0
diag2 = 0
for k in range(5):
    when_bingo.append(max(player[k]))
    when_bingo.append(max(player_t[k]))
    temp1 = player[k][k]
    if temp1 > diag1:
        diag1 = temp1

    temp2 = player[k][4-k]
    if temp2 > diag2:
        diag2 = temp2
when_bingo.append(diag1)
when_bingo.append(diag2)
when_bingo.sort()
print(when_bingo[2]+1)


