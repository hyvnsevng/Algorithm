from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n, w = map(int, input().split())
m = float(input())
coors = [tuple(map(int, input().split())) for _ in range(n)]

connected = [[] for _ in range(n)] 
for _ in range(w):
    a, b = map(int, input().split())
    connected[a-1].append(b-1)
    connected[b-1].append(a-1)

hq = [(0, 0)]
distance = [10e9] * (n)
while hq:
    len_sum, node = heappop(hq)
    if len_sum > distance[node]:
        continue
    
    for c in connected[node]:
        if distance[c] > len_sum:
            heappush(hq, (len_sum, c))
            distance[c] = len_sum

    for nxt in range(n):
        l = ((coors[nxt][0] - coors[node][0])**2 + (coors[nxt][1] - coors[node][1])**2)**0.5
        if l <= m and distance[nxt] > len_sum + l:
            heappush(hq, (len_sum + l, nxt))
            distance[nxt] = len_sum + l

print(int(distance[n-1] * 1000))