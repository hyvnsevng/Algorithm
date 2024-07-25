N = str(input())

if sum(list(map(int, (N[len(N)//2:])))) == sum(list(map(int, (N[:len(N)//2])))):
    print('LUCKY')
else:
    print('READY')