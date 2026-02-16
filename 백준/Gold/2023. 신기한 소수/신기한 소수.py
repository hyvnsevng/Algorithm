n = int(input())

def dfs(num, depth, lmt):
    # print(num)
    if depth==lmt:
        print(num)
        return
    
    for i in range(1, 10, 2):
        nxt = num*10+i
        bc = (nxt**0.5)+1
        prime = 3
        while prime < bc:
            # print(prime)
            if nxt % prime == 0:
                break
            prime += 2
        if prime >= bc:
            dfs(nxt, depth+1, lmt)


monoprimes = [2, 3, 5, 7]
for monoprime in monoprimes:
    dfs(monoprime, 1, n)