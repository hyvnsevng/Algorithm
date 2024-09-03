import sys
input = sys.stdin.readline

n = int(input())
numlst = []
count = [0]*8001
maxcnt, maxnum = 0, -4001

for _ in range(n):
    num = int(input())
    numlst.append(num)
    count[num+4000] += 1
    if count[num+4000] > maxcnt:
        maxcnt = count[num+4000]

numlst.sort()

print(round(sum(numlst)/n))
print(numlst[n//2])

flag = False
for i in range(8001):
    if flag and count[i] == maxcnt:
        maxnum = i-4000
        break
    if not flag and count[i] == maxcnt:
        flag = True
        maxnum = i-4000

print(maxnum)
print(numlst[-1] - numlst[0])
