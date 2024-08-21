n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]

    a_cnt = []
    b_cnt = []

    draw = True

    for i in range(4, 0, -1):
        a_card = a.count(i)
        b_card = b.count(i)
        if a_card != b_card:
            draw = False
        a_cnt.append(a_card)
        b_cnt.append(b_card)

    a_cnt.append('A')
    b_cnt.append('B')

    shobu = [a_cnt, b_cnt]
    shobu.sort(reverse=True)

    if draw:
        print('D')
    else:
        print(shobu[0][-1])
