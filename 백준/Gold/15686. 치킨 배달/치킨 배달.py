import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(n)]
chickens = []
n_home = 0
for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            n_home += 1
        elif town[i][j] == 2:
            chickens.append((i, j))
distances = []
for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            distances.append([abs(row - i) + abs(col - j) for row, col in chickens])

cases = list(combinations([idx for idx in range(len(chickens))], m))

answer = 10e9
for case in cases:
    chicken_distance = 0
    for distance in distances:
        selected = [distance[i] for i in case]
        chicken_distance += min(selected)
    if chicken_distance < answer:
        answer = chicken_distance

print(answer)
