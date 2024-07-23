from collections import deque

n, w, l = map(int, input().split())

trucks = list(map(int, input().split()))

queue = deque([0 for _ in range(w)])

time = 0

for truck in trucks:
    while sum(list(queue)[1:]) + truck > l:
        # print(queue)
        queue.popleft()
        queue.append(0)
        time += 1
    # print(queue)
    queue.popleft()
    queue.append(truck)
    time += 1
time += len(queue)
print(time)