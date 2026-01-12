def solve(N: int) -> int:
    n = N
    primes = []

    p = 2
    while p * p <= n:
        if n % p == 0:
            primes.append(p)
            while n % p == 0:
                n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        primes.append(n)

    l = len(primes)
    ans = 0
    for mask in range(1, 1 << l):
        x = 1
        bitcnt = 0
        for i in range(l):
            if mask & (1 << i):
                x *= primes[i]
                bitcnt += 1
        cnt = N // x
        if bitcnt % 2 == 1:
            ans -= cnt
        else:
            ans += cnt

    return N + ans

n = int(input())
print(solve(n))