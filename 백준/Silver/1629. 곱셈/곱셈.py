def mod(n, c):
    return n % c


def pow(n, k, c):
    if k == 0:
        return 1
    elif k == 1:
        return mod(n, c)
    else:
        x = mod(pow(n, k // 2, c), c)
        
        if k % 2:
            return mod(mod(x * x, c) * mod(a, c), c)
        else:
            return mod(x * x, c)


a, b, c = map(int, input().split())
print(pow(a, b, c))