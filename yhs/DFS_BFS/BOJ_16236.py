# 백준 16236번 아기 상어

# 상어가 먹을 수 있는 물고기 탐색 -> 몇초까지 먹이를 먹으러 돌아다닐 수 있나?
# BFS 이용해 탐색
# 오랜만에 BFS 문제를 풀었더니 방문처리 구현이 헷갈렸다. 어느 시점에 방문 처리를 할 지에 주의할 것 !!

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

# # 우선순위 큐 이용한 풀이
# def bfs(row, col):
#     def prior(a, b):
#         if a[2] == b[2]:
#             if a[0] == b[0]:
#                 if a[1] < b[1]:
#                     return True
#                 else:
#                     return False
#             elif a[0] < b[0]:
#                 return True
#             else:
#                 return False
#         elif a[2] < b[2]:
#             return True
#         else:
#             return False
#
#     visited = []
#
#     queue = deque()
#     queue.append([row, col, 0])
#     dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]
#     size = 2
#     count = 0
#     time = 0
#
#     while queue:
#         vr, vc, tmp = queue.popleft()
#
#         # 우선순위 큐 수정
#         node = 1
#         child = node*2
#         while child <= len(queue):
#             if child < len(queue) and prior(queue[child], queue[child-1]):
#                 child += 1
#
#             if prior(queue[child-1], queue[node-1]):
#                 queue[child-1], queue[node-1] = queue[node-1], queue[child-1]
#             else:
#                 break
#
#         if 0 < space[vr][vc] < size:
#             space[vr][vc] = 0
#             count += 1
#             time += tmp
#             tmp = 0
#             queue = deque()
#
#             if count == size:               # 자기 크기와 같은 수의 물고기를 먹은 경우 : 크기 +1, count와 visited 초기화
#                 size += 1
#                 count = 0
#             visited = []
#             visited.append([vr, vc])
#
#         for k in range(4):
#             r, c = vr + dr[k], vc + dc[k]
#             if 0 <= r < n and 0 <= c < n and [r, c] not in visited and space[r][c] <= size:
#                 queue.append([r, c, tmp+1])
#                 visited.append([r, c])
#                 child = len(queue)
#                 while child > 1:
#                     if prior(queue[child-1], queue[child//2-1]):
#                         queue[child - 1], queue[child // 2 - 1] = queue[child // 2 - 1], queue[child - 1]
#                         child //= 2
#                     else:
#                         break


n = int(input())

space = [list(map(int, input().split())) for _ in range(n)]
# print(space)
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            space[i][j] = 0
            print(bfs(i, j))