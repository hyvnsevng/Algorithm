from collections import deque

n, k = map(int, input().split())

q = deque()
q.append([n])
time = 0
visited = [False]*200000
visited[n] = True
while q:
    v = q.popleft()
    tmp = set()
    if k in v:
        break
    for num in v:
        if num > 0 and not visited[num-1]:
            tmp.add(num-1)
            visited[num-1] = True
        if num+1 < 200000 and not visited[num+1]:
            tmp.add(num+1)
            visited[num+1] = True
        if num*2 < 200000 and not visited[num*2]:
            tmp.add(num*2)
            visited[num*2] = True

    q.append(tmp)
    time += 1

print(time)