n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
op_idx = [5, 3, 4, 1, 2, 0]         # 주사위 전개도에서 반대편의 인덱스

max_sum = 0

for j in range(6):              # 가장 아래 주사위의 모든 방향 탐색
    top = dices[0][j]
    base = []
    for _ in range(6):
        if not(_ == j or op_idx[_] == j):       # 위, 아래 제외 모든 옆면 base에 추가
            base.append(dices[0][_])

    sum_ = max(base)                            # 옆면의 수 중 최댓값

    for i in range(1, n):
        bottom = top
        bottom_idx = dices[i].index(bottom)
        top = dices[i][op_idx[bottom_idx]]

        # print(top)
        lst = []
        for k in range(6):
            if not (dices[i][k] == top or dices[i][op_idx[k]] == top):  # 다음 주사위 중 옆면 최댓값 구하기
                lst.append(dices[i][k])
        sum_ += max(lst)

    if sum_ > max_sum:
        max_sum = sum_
    # print()

print(max_sum)

'''
[up, left, back, right, front, down]
0, 5
1, 3
2, 4

맨 아래 주사위의 방향이 정해지면 그 위에 오는 주사위 방향도 정해져있음
'''


