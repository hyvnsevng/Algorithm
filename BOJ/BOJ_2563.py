# 2563번 색종이

canvas = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(10):
        for j in range(10):
            canvas[x + i][y + j] = 1

total = 0
for row in canvas:
    total += sum(row)

print(total)