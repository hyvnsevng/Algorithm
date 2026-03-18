from collections import deque


def bfs():
    global answer       # 글로벌 변수 answer : 인구 이동 시 답 수정

    queue = deque()
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    temp = 0            # 인구 이동이 일어났는 지 확인

    # 모든 국가 순회
    for i in range(n):
        for j in range(n):
            move = []   # 국경이 개방된 나라의 위치 저장
            if not visited[i][j]:
                queue.append([i, j])    # 해당 위치 큐에 넣기
                move.append([i, j])
                visited[i][j] = True    # 해당 위치 방문처리
                sum = land[i][j]        # 인구의 합
                cnt = 1                 # 인구 이동이 일어난 나라의 수

                while queue:
                    vr, vc = queue.popleft()
                    for k in range(4):      # 인접 국가 확인
                        row, col = vr + dr[k], vc + dc[k]
                        if 0 <= row < n and 0 <= col < n and not visited[row][col]: # 인덱스 범위 내에 있고 방문하지 않았는지 확인
                            if l <= abs(land[row][col] - land[vr][vc]) <= r:        # 인구 차이가 조건과 맞는다면
                                visited[row][col] = True    # 인접국가 방문처리
                                queue.append([row, col])    # 큐에 넣기
                                move.append([row, col])     # 인구 이동한 나라 목록에 추가
                                sum += land[row][col]       # 인구 수 합 갱신
                                cnt += 1                    # 인구 이동 일어난 나라의 수 갱신
                                temp = 1                    # 인구이동 체크

                avg = sum//cnt                              # 모든 국경선 확인 후 평균 구하기

                for moved in move:
                    land[moved[0]][moved[1]] = avg          # 인구 이동동

    if temp:         # temp가 0이 아니라면(인구 이동이 발생했다면)
        answer += 1      # answer(인구 이동이 발생한 날) 갱신
        return True     # 인구 이동했습니다~
    return False        # 이제 인구 이동 안됩니다~


n, l, r = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

answer = 0

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = bfs()  # bfs 함수 당 하루
    if not result:  # 인구 이동이 더 이상 일어나지 않는다면 반복 탈출
        break
print(answer)


