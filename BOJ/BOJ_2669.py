# 백준 2669번. 직사각형 네개의 합집합의 면적 구하기

graph = [[0 for i in range(100)] for i in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1-1, x2-1):
        for j in range(y1-1, y2-1):
            graph[i][j] = 1

total = 0
for row in graph:
    total += sum(row)

print(total)