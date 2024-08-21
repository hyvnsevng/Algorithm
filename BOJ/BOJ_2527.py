
for _ in range(4):
    data = list(map(int, input().split()))
    x1, y1, p1, q1, x2, y2, p2, q2 = data

    if x1 <= x2 < p1:
        if y2 > q1 or q2 < y1:
            print('d')
        elif y1 == q2 or y2 == q1:
            print('b')
        else:
            print('a')

    elif x2 < x1 < p2 <= p1:
        if y1 > q2 or q1 < y2:
            print('d')
        elif y1 == q2 or y2 == q1:
            print('b')
        else:
            print('a')

    elif x2 < x1 < p1 < p2:
        if y1 > q2 or q1 < y2:
            print('d')
        elif y1 == q2 or y2 == q1:
            print('b')
        else:
            print('a')


    elif x1 == p2 or x2 == p1:          # 1이 위, 2가 아래
        if y1 > q2 or q1 < y2:
            print('d')
        elif y1 == q2 or y2 == q1:
            print('c')
        else:
            print('b')

    elif x1 > p2 or x2 > p1:
        print('d')


