n = int(input()) # 색종이 장수
paper_info = [list(map(int, input().split())) for _ in range(n)]

min_row = 1001
max_row = 0

min_col = 1001
max_col = 0

for info in paper_info:
    r, c, dr, dc = info
    if r + dr > max_row:
        max_row = r + dr
    if r < min_row:
        min_row = r
    if c + dc > max_col:
        max_col = c + dc
    if c < min_col:
        min_col = c

lst = [[0 for _ in range(max_col)] for _ in range(max_row)]

for k in range(1, n+1):
    r, c, dr, dc = paper_info[k-1]
    for i in range(dr):
        for j in range(dc):
            lst[r + i][c + j] = k


papers = [0 for _ in range(n)]
for i in range(min_row, max_row):
    for j in range(min_col, max_col):
        paper = lst[i][j]
        if paper > 0:
            papers[paper - 1] += 1

for area in papers:
    print(area)