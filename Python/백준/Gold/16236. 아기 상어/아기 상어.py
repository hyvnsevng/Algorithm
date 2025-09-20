from collections import deque


def find_feed(lst, size):
    top, left = n, n
    for coor in lst:
        row, col = coor
        if 0 < space[row][col] < size:
            if row < top or row == top and col < left:
                top, left = row, col

    if top < n:
        return top, left


def bfs(row, col):
    global visited

    queue = deque()
    queue.append([[row, col]])
    dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]
    size = 2
    count = 0
    time = 0
    tmp = 0
    while queue:
        v_lst = queue.popleft()

        feed = find_feed(v_lst, size)         # 최우선 먹이 탐색
        if feed:                        # 탐색했다면
            vr, vc = feed
            space[vr][vc] = 0
            count += 1
            time += tmp
            tmp = 0
            queue = deque()

            if count == size:               # 자기 크기와 같은 수의 물고기를 먹은 경우 : 크기 +1, count와 visited 초기화
                size += 1
                count = 0

            visited = [[False for _ in range(n)] for _ in range(n)]

            visited[vr][vc] = True
            v_lst = [[vr, vc]]

        queue_lst = []

        for v in v_lst:
            vr, vc = v
            for k in range(4):
                r, c = vr + dr[k], vc + dc[k]
                if 0 <= r < n and 0 <= c < n and not visited[r][c] and space[r][c] <= size:
                    queue_lst.append([r, c])
                    visited[r][c] = True

        if queue_lst:
            queue.append(queue_lst)

        tmp += 1

    return time


n = int(input())

space = [list(map(int, input().split())) for _ in range(n)]
# print(space)
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            space[i][j] = 0
            print(bfs(i, j))