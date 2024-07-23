N = int(input())
tiem = list(map(int, input().split()))
tiem.sort()

tot = 0
for i in range(N):
    tot += sum(tiem[:i+1])

print(tot)