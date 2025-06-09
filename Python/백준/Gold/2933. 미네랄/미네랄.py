from collections import deque

r, c = map(int, input().split())
cave = [list(input()) for _ in range(r)]
n = int(input())
heights = list(map(int, input().split()))
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

def throw(height, turn):
    if turn % 2 == 0:
        try:
            col = cave[height].index('x')
            cave[height][col] = '.'
            return [height, col]
        except:
            return
    else:
        try:
            col = c - 1 - list(reversed(cave[height])).index('x')
            cave[height][col] = '.'
            return [height, col]
        except:
            return


def cluster(coor, turn):
    row, col = coor

    for i in range(4):
        if 0 <= row + dr[i] < r and 0 <= col + dc[i] < c and cave[row + dr[i]][col + dc[i]] == 'x':
            broken = find([row + dr[i], col + dc[i]])
            if broken:
                drop(broken)


def find(coor):
    result = [list() for _ in range(c)]
    result[coor[1]].append(coor[0])
    q = deque()
    q.append(coor)

    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[coor[0]][coor[1]] = True

    while q:
        row, col = q.popleft()
        if row == r-1:
            return []
        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc] and cave[nr][nc] == 'x':
                q.append([nr, nc])
                result[nc].append(nr)
                visited[nr][nc] = True

    for _list in result:
        _list.sort()
    return result


def drop(coors):
    step = 0
    stop = False
    while not stop:
        for i in range(c):
            if coors[i]:
                descend = coors[i][-1] + step + 1
                if descend == r or cave[descend][i] == 'x':
                    stop = True
                    break

        if stop:
            break

        step += 1

    if step == 0:
        return

    for i in range(c):
        for row in coors[i]:
            cave[row][i] = '.'

    for i in range(c):
        for row in coors[i]:
            cave[row + step][i] = 'x'


for i in range(n):
    coor = throw(r - heights[i], i)
    if coor:
        cluster(coor, i)

for row in cave:
    print("".join(row))
