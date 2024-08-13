import sys

sys.stdin = open('4871_input.txt')


def path(arr, start, goal):
    stack = [start]
    neighbour = start

    while stack:
        s = neighbour   # 출발노드
        neighbour = stack.pop() # 도착노드

        # 경로 있나요?
        if neighbour == goal:
            return 1    # 있으면 1 반환

        # 방문처리
        arr[s - 1][neighbour - 1] = 0

        # 인접노드 stack에 넣기
        for i in range(v):
            if arr[neighbour - 1][i]:
                stack.append(i + 1)

    # 모두 탐색했는데 경로 없으면 0 반환
    return 0


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    v, e = map(int, input().split())
    link = [list(map(int, input().split())) for _ in range(e)]
    start, goal = map(int, input().split())

    # 인접행렬 만들기
    arr = [[0 for _ in range(v)] for _ in range(v)]
    for edge in link:
        n1, n2 = edge[0], edge[1]
        arr[n1-1][n2-1] = 1

    print(f'#{tc} {path(arr, start, goal)}')
