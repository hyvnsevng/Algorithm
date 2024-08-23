import sys
import heapq

N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

heapq.heapify(num_list)
ans = 0

for i in range(N-1):
    num1 = heapq.heappop(num_list)
    num2 = heapq.heappop(num_list)
    min_sum = num1 + num2
    ans += min_sum
    heapq.heappush(num_list, min_sum)

print(ans)