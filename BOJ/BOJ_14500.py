# 백준 14500번 테트로미노

# 미리 테트로미노의 모양을 배열에 저장해두고 풀었다.
# pypy로 채점 시 문제가 없지만, python으로 채점 시 시간 초과가 발생했다. 어떻게 해결해야 할까 . . ?


def find(row, col):
    result = 0

    # 5개 모양에 대해 격자 내 정수 합 구하기
    for shape in tetromino:
        # 회전(4)*대칭(2) 한 8가지 경우
        tmp = [graph[row][col]] * 8
        for dr, dc in shape:
            coors = returnCoors(row, col, dr, dc)   # coors: 8개 경우에 대한 좌표를 길이가 8인 배열로 반환
            for i in range(8):
                nr, nc = coors[i]
                if tmp[i] == 0:     # 이미 범위를 벗어난 경우라면 계산하지 않음
                    continue
                if 0 <= nr < n and 0 <= nc < m:     # 범위 내에 있는지 확인 후 계산
                    tmp[i] += graph[nr][nc]
                else:                               # 범위 밖이라면 값을 0으로 설정, 이후 0인 경우는 계산 X
                    tmp[i] = 0

        tmpMax = max(tmp)       # tmp 배열 내 최댓값(5가지 모양 중 한가지 모양에 대해 나올 수 있는 정수합의 최대)
        if tmpMax > result:     # 최댓값 갱신
            result = tmpMax

    return result


def returnCoors(row, col, dr, dc):
    return [[row+dr, col+dc], [row-dr, col+dc], [row+dr, col-dc], [row-dr, col-dc], [row+dc, col+dr], [row-dc, col+dr], [row+dc, col-dr], [row-dc, col-dr]]


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 0

# 5개 모양 테트로미노의 각 격자의 상대좌표 배열
tetromino = [[[1, 0], [2, 0], [3, 0]], [[0, 1], [1, 1], [2, 1]], [[1, 0], [0, 1], [-1, 0]], [[1, 0], [1, 1], [2, 1]], [[1, 0], [1, 1], [0, 1]]]

for i in range(n):
    for j in range(m):
        # (i, j) 좌표를 기준으로 했을 때 나올 수 있는 합의 최대
        result_ = find(i, j)

        # 최대값 갱신하기
        if result_ > ans:
            ans = result_

print(ans)