def find(n, r, c):
    if n == 1:
        if r+c==0:
            return 0
        elif r<c:
            return 1
        elif r>c:
            return 2
        else:
            return 3

    a, b = 0, 0
    if r+1 > 2**(n-1):
        a = 1
        r = r%(2**(n-1))
    if c+1 > 2**(n-1):
        b = 1
        c = c % (2 ** (n - 1))

    return (2*a+b)*((2**(n-1))**2) + find(n-1, r, c)


n, r, c = map(int, input().split())

print(find(n, r, c))