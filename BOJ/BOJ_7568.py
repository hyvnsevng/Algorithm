# 백준 7568번 덩치

n = int(input())
infos = []
for i in range(n):
    weight, height = map(int, input().split())
    infos.append([weight, height])

ranks = [1 for _ in range(n)]
for i in range(n):
    count = 0
    for j in range(n):
        if infos[i][0] < infos[j][0] and infos[i][1] < infos[j][1]:
            count += 1

    ranks[i] += count

print(*ranks)