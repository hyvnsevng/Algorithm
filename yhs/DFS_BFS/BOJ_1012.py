import sys

sys.setrecursionlimit(10**6)        # 재귀 깊이 제한 늘리기


def dfs(graph, vi, vj):
    # 범위 밖으로 벗어날 시 False
    if vi>=len(graph) or vi<0 or vj>=len(graph[0]) or vj<0:
        return False

    # 방문 안 한 노드일 시 방문처리 후 인접 노드 탐색
    if graph[vi][vj]:
        graph[vi][vj] = 0
        dfs(graph, vi+1, vj)
        dfs(graph, vi, vj+1)
        dfs(graph, vi - 1, vj)
        dfs(graph, vi, vj - 1)
        return True

    # 방문한 노드일 시 False
    return False


T = int(input())

for tc in range(1, T + 1):
    m, n, k = map(int, input().split())     # 열, 행, 배추 수

    # 지도에 배추 위치 표시
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        col, row = map(int, input().split())
        graph[row][col] = 1

    # 모든 위치에서 dfs
    answer = 0
    for i in range(n):
        for j in range(m):
            if dfs(graph, i, j):
                answer += 1

    print(answer)