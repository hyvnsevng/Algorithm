# 백준 1002번 터렛

T = int(input())
for tc in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d_square = (x1 - x2)**2 + (y1 - y2)**2
    r_square_sum = (r1 + r2)**2
    r_square_sub = (r1 - r2)**2

    if d_square == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif d_square > r_square_sum or d_square < r_square_sub:
        print(0)
    elif d_square == r_square_sum or d_square == r_square_sub:
        print(1)
    elif r_square_sub < d_square < r_square_sum:
        print(2)