n = int(input())
monoprimes = [2, 3, 5, 7]
MAX_NUM = int((10**(n))**0.5)
ans = []
checked = [0] * MAX_NUM
prime_set = set()
x=2
while x<MAX_NUM:
    if checked[x]==0:
        prime_set.add(x)
        k = x * 2
        plus = 2
        if x != 2:
            k = x * 3
            plus = x * 2
        while k < MAX_NUM:
            checked[k] = 1
            k += plus
    if x == 2:
        x += 1
    else:
        x += 2
        

def is_prime(num):
    if num in prime_set:
        return True
    for prime in prime_set:
        if num % prime == 0:
            return False
    return True


def solve(num, depth, lmt):
    if depth and not is_prime(num):
        return
    
    if depth==lmt:
        ans.append(num)
        return
    
    _range = range(1, 10, 2)
    if depth == 0:
        _range = monoprimes
    for i in _range:
        solve(num*10+i, depth+1, lmt)

solve(0, 0, n)
for prime in ans:
    print(prime)