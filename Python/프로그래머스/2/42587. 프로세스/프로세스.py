from collections import deque
from heapq import heappop, heappush, heapify

def solution(priorities, location):
    n = len(priorities)
    pq = []
    q = deque()
    for i in range(n):
        priority = priorities[i]
        heappush(pq, -priority)
        q.append((priority, i))
        
    answer = 0
    while q:
        priority, process = q.popleft()
        if -pq[0] > priority:
            q.append((priority, process))
            continue
        heappop(pq)
        answer += 1
        if process == location:
            return answer
    return answer