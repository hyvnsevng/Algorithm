c, r = map(int, input().split())

n = int(input())

if n > c*r:
    print(0)

else:
    x, y = 1, 1
    c -= 1
    r -= 1

    while True:
        if n <= 2*(r+c):
            if n <= r:
                y += n-1
            elif r < n <= r+c:
                x += n-r-1
                y += r

            elif r+c < n <= 2*r+c:
                x += c
                y += 2*r+c+2-n-1  # n = 32 - 22 = 10, c-d = 4, r-d = 3 y =

            else:
                x += 2*(r+c) - n + 1
            break

        x += 1
        y += 1
        n -= 2 * (r + c)
        r -= 2
        c -= 2


    print(x, y)

