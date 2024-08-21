length, height = map(int, input().split())
n = int(input())

shops = [list(map(int, input().split())) for _ in range(n)]

nswe, dis = map(int, input().split())

distance = 0

for shop in shops:
    if nswe == shop[0]:
        distance += abs(dis - shop[1])

    elif nswe + shop[0] == 3:   # 북 남
        distance += (min(dis + shop[1], (length - dis) + (length - shop[1])) + height)

    elif nswe + shop[0] == 4:   # 북 서
        distance += (shop[1] + dis)

    elif nswe + shop[0] == 5:   # 북 동 / 남 서
        if nswe == 1:
            distance += (length - dis + shop[1])
        elif nswe == 2:
            distance += (dis + height - shop[1])
        elif nswe == 3:
            distance += (height - dis + shop[1])
        else:
            distance += (dis + length - shop[1])

    elif nswe + shop[0] == 6:   # 남 동
        distance += (length + height - shop[1] - dis)

    elif nswe + shop[0] == 7:   # 동 서
        distance += (min(shop[1] + dis, (height - shop[1]) + (height - dis)) + length)

print(distance)
'''
1: 북
2: 남
3: 서
4: 동

3 (1+2)
4 (1+3)
5 (1+4, 2+3)  북-동, 남-서
6 (2+4)
7 (3+4)
'''