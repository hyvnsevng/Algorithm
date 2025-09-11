def stars(depth):
    if depth == 3:
        return ['  *  ', ' * * ', '*****']

    fractal = stars(depth // 2)
    top, bottom = [], []
    for i in range(depth // 2):
        top.append(' ' * (depth // 2) + fractal[i] + ' ' * (depth // 2))
        bottom.append(fractal[i] + ' ' + fractal[i])
    return top + bottom


n = int(input())
for row in stars(n):
    print(row) 