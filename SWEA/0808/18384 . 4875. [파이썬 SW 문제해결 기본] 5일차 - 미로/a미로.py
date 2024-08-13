import sys

sys.stdin = open('4875_input.txt')

def find_path(s):
    # delta
    drow = [1, 0, -1, 0]
    dcol = [0, 1, 0, -1]
    # 2로 방문처리 하기
    maze[s[0]][s[1]] = 2

    # 인접노드 탐색
    for i in range(4):
        row = s[0] + drow[i]
        col = s[1] + dcol[i]
        if 0 <= row < n and 0 <= col < n:   # 인덱스 범위 확인
            if maze[row][col] == 0: # 방문 안한 길이라면?
                if find_path([row, col]):   # 재귀호출해서 return이 1이라면 (목표지점에 도착했다면) 1 return
                    return 1
            elif maze[row][col] == 3:   # 목표지점 도착
                return 1

    return 0    # 아니면 return 0


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    maze = [list(map(int, input().strip())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j]==2:
                start = [i, j]  # 시작지점 좌표 찾기

    print(f'#{tc} {find_path(start)}')