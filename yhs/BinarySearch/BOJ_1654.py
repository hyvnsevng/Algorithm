# 백준 1654번 랜선 자르기

import sys

k, n = map(int, input().split())
lst = []
e = 0
for _ in range(k):
    lan = int(sys.stdin.readline())
    lst.append(lan)
    e += lan

s = 1
ans = 0
while s <= e:
    tmp = 0
    m = (s+e)//2
    for length in lst:
        tmp += (length // m)

    if tmp >= n:
        ans = m
        s = m + 1
    else:
        e = m - 1
print(ans)


