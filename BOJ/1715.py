# 미완

import sys
from collections import deque

N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(sys.stdin.readline()))


num_list.sort()
queue = deque(num_list)

ans = 0

while len(queue) > 2:
    if queue[0] + queue[1] < queue[1] + queue[2]:
        queue[0] = queue.popleft()+queue[0]
        ans += queue[0]

    else: 
        first_index = queue.popleft()
        queue[1] = queue[0] + queue[1]
        queue[0] = first_index
        ans += queue[1]


print(ans+sum(queue))


# 3 3 3 5 7
# 3+3+8+14+21
