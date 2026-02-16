n = int(input())
MAX = 10**(n-1)
def dfs(num):
    if num // MAX:
        print(num)
        return
    
    for i in range(1, 10, 2):
        nxt = num*10+i
        bc = (nxt**0.5)+1
        prime = 3
        while prime < bc:
            if nxt % prime == 0:
                break
            prime += 2
        if prime >= bc:
            dfs(nxt)


monoprimes = [2, 3, 5, 7]
for monoprime in monoprimes:
    dfs(monoprime)