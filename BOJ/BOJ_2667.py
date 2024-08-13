from collections import deque


def dfs(graph, vr, vc):
    if 0 <= vr < n and 0 <= vc < n:
        return False

    if graph[vr][vc]:
        ans = bfs(graph, vr, vc)
        graph[vr][vc] = 0
        dfs(graph, vr + dr[0], vc + dc[0])
        dfs(graph, vr + dr[1], vc + dc[1])
        dfs(graph, vr + dr[2], vc + dc[2])
        dfs(graph, vr + dr[3], vc + dc[3])
        return ans
    return False


def bfs(graph, vr, vc):
    queue = deque([vr, vc])
    graph[vr][vc] = 2

    number = 1

    while queue:
        vr, vc = queue.popleft()
        for i in range(4):
            row = vr + dr[i]
            col = vc + dc[i]
            if 0 <= row < n and 0 <= col < n and graph[row][col] == 1:
                graph[row][col] = 2
                queue.append([row, col])
                number += 1

    return number


n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

danji = 0
house = []

for i in range(n):
    for j in range(n):
        result = dfs(graph, i, j)
        if result:
            house.append(result)
            danji += 1

print(danji)

for num in house:
    print(num)

'''

'''