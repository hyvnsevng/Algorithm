# 백준 16953번 A -> B

from collections import deque

a, b = map(int, input().split())
answer = 1  # 출력할 정답 초기화(연산 횟수 + 1)
queue = deque([[a, answer]])    # 큐에 시작 정수(a)와 연산 횟수가 요소인 배열 추가

# BFS
while queue:
    v, calc = queue.popleft()
    if v == b:  # 연산 결과가 b인 경우 정답 저장 및 반복 탈출
        answer = calc
        break

    # 두가지 연산과 연산 횟수 큐에 추가하기
    if v*2 <= b:
        queue.append([v*2, calc+1])
    if v*10+1 <= b:
        queue.append([v*10+1, calc+1])

# 만약 a에서 b로 만들 수 없다면(답이 갱신되지 않고 BFS 종료되었다면) -1 출력
if answer == 1:
    print(-1)
else:
    print(answer)