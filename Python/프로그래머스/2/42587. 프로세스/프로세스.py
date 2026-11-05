from collections import deque

def solution(priorities, location):
    n = len(priorities)
    q = deque()
    for i in range(n):
        priority = priorities[i]
        q.append((priority, i))
    priorities.sort(reverse=True)
        
    answer = 0
    while q:
        priority, process = q.popleft()
        if priorities[answer] > priority:
            q.append((priority, process))
            continue
        answer += 1
        if process == location:
            return answer
    return answer