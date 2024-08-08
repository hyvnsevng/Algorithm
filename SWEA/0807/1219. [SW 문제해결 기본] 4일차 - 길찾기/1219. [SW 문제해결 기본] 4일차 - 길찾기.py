import sys

sys.stdin = open('input.txt')

def find_path(data):
    stack = [0] # 스택에 시작지점 추가

    # 모든 연결 노드 탐색
    while stack:
        v = stack.pop()     # 스택의 top 요소
        # v의 다음 노드 확인
        for i in data[v]:
            stack.append(i)     # 다음 노드 큐에 넣기
            if i == 99:     # 도착지점일 경우 1 반환
                return 1

    # 모두 탐색했는데 도착지점에 못 갔으면 0 반환
    return 0


# Testcase 수
T = 10
# Testcase 만큼 반복
for _ in range(1, T+1):
    tc, n = map(int, input().split())

    edge = list(map(int, input().split()))  # 순서쌍

    data = [[] for _ in range(100)]         # (인덱스)번째 노드에서 갈 수 있는 노드
    for i in range(n):
        data[edge[2*i]].append(edge[2*i + 1])

    print(f'#{tc} {find_path(data)}')
