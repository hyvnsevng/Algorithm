# 백준 11286번 절댓값 힙

# 최소 힙 문제에 절댓값 기준만 추가한 문제
# 절댓값이 같은 경우 작은 값이 우선순위가 더 높은 것을 구현하는 것이 꽤나 까다로웠다

import sys

n = int(input())
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
            while child <= last:
                if node*2+1 <= last:
                    if abs(heap[node*2]) > abs(heap[node*2+1]):
                        child += 1
                    elif abs(heap[node*2]) == abs(heap[node*2+1]) and heap[node*2] > heap[node*2+1]:
                        child += 1

                if abs(heap[node]) > abs(heap[child]):
                    heap[node], heap[child] = heap[child], heap[node]
                    node = child
                    child *= 2
                else:
                    if abs(heap[node]) == abs(heap[child]) and heap[node] > heap[child]:
                        heap[node], heap[child] = heap[child], heap[node]
                        node = child
                        child *= 2
                    else:
                        break

    else:
        last += 1
        heap[last] = num
        node = last
        while node > 1:
            if abs(heap[node]) < abs(heap[node//2]):
                heap[node], heap[node//2] = heap[node//2], heap[node]
                node //= 2
            elif abs(heap[node]) == abs(heap[node//2]) and heap[node] < heap[node//2]:
                heap[node], heap[node // 2] = heap[node // 2], heap[node]
                node //= 2
            else:
                break

