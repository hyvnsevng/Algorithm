# 백준 1927번 최소 힙

# 구현 ver.
import sys

n = int(sys.stdin.readline())
heap = [0 for _ in range(n+1)]
last = 0
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if not last:
            print(0)
        else:
            print(heap[1])
            heap[1], heap[last] = heap[last], 0
            last -= 1
            node = 1
            child = node*2
            while node*2 <= last:
                if node*2 + 1 <= last and heap[node*2] > heap[node*2+1]:
                    child += 1

                if heap[node] > heap[child]:
                    heap[node], heap[child] = heap[child], heap[node]
                    node = child
                    child = node*2
                else:
                    break

    else:
        last += 1
        heap[last] = num
        node = last
        while node > 1:
            if heap[node] >= heap[node//2]:
                break

            heap[node], heap[node//2] = heap[node//2], heap[node]
            node //= 2

# 라이브러리 사용 ver.

# import sys
# from heapq import heappop, heappush
#
# n = int(sys.stdin.readline())
# heap = []
#
# for _ in range(n):
#     num = int(sys.stdin.readline())
#     if num == 0:
#         if not heap:
#             print(0)
#         else:
#             print(heappop(heap))
#
#     else:
#         heappush(heap, num)
