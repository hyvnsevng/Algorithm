from collections import deque


def bfs(visited):
    global shark_r, shark_c
    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]

    queue = deque()
    queue.append([shark_r, shark_c])
    visited[shark_r][shark_c] = True

    size_shark = 2

    time = 0
    temp = 0
    while queue:
        print(queue)
        print(temp)
        lst = list(queue)
        print(lst)
        queue = deque(lst)
        temp += 1
        print(time, queue)
        length = len(queue)
        for _ in range(length):
            v = queue.popleft()
            is_break = False
            for i in range(4):
                for positions in v:
                    row, col = positions[0] + dr[i], positions[1] + dc[i]

                    if 0 <= row < n and 0 <= col < n and not visited[row][col]:
                        fish = space[row][col]

                        if not fish:
                            queue.append([row, col])
                            visited[row][col] = True

                        elif fish <= size_shark:
                            if fish == size_shark:
                                size_shark += 1
                            space[shark_r][shark_c] = 0
                            shark_r, shark_c = row, col
                            space[row][col] = 0
                            visited = [[False for _ in range(n)] for _ in range(n)]
                            visited[row][col] = True
                            is_break = True
                            queue.append([row, col])
                            time += temp
                            temp = 0
                            break
                if is_break:
                    break
            if is_break:
                break

    return time


n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]

# 아기상어 위치
shark_r, shark_c = 0, 0
for x in range(n):
    for y in range(n):
        if space[x][y] == 9:
            shark_r, shark_c = x, y


a = deque([[1,1], [2,2], [0,0]])
b = list(a)
print(a, b)
b.sort()
print(a, b)
a = deque(b)
print(a, b)

print(bfs(visit))

