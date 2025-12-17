from collections import deque


def push(X, sec, cnt):
    # 범위 밖의 좌표일 경우 무시
    if X < 0 or X > 100000:
        return
    
    # 방문한 적 있는지 확인
    time, prev_cnt = visited.get(X, (sec, 0))
    # 없다면 새로 등록
    if prev_cnt == 0:
        q.append((X, sec))
    # 지금이 최단시간이라면 횟수 갱신
    if time == sec:
        visited[X] = (sec, cnt + prev_cnt)


N, K = map(int, input().split())

q = deque([(N, 0)])
visited = dict()
visited[N] = (0, 1)

while q:
    X, sec = q.popleft()
    if X == K:
        break
    
    cnt = visited[X][1]
    n_sec = sec + 1
    push(2 * X, n_sec, cnt)
    push(X - 1, n_sec, cnt)
    push(X + 1, n_sec, cnt)

result = visited[K]
for ans in result:
    print(ans)