# 백준 11279번 최대 힙

# 구현 ver.
import sys

n = int(sys.stdin.readline())   # 힙에 넣을 숫자 개수 입력받기

heap = [0 for _ in range(n+1)]  # n+1개 크기의 힙 생성
last = 0                        # 마지막 노드 번호

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:        # 숫자가 0이면 힙에서 최대값 출력
        if not last:    # 힙이 비어있다면 0 출력
            print(0)
        else:
            print(heap[1])
            heap[1], heap[last] = heap[last], 0     # 힙의 마지막 원소를 루트로 옮김
            last -= 1                               # 힙에서 pop 했으므로 크기를 1만큼 감소

            # 루트로 이동한 마지막 원소를 자식 노드와 비교하며 위치 조정
            node = 1
            while node*2 <= last:
                # 2번째 자식 노드가 있고 현재 노드와 두 자식 노드 중 가장 큰 경우
                if node*2 + 1 <= last and heap[node*2] < heap[node*2+1] and heap[node] < heap[node*2+1]:
                    heap[node], heap[node*2+1] = heap[node*2+1], heap[node]
                    node = node*2+1
                # 첫번째 자식 노드가 더 큰 경우
                elif heap[node] < heap[node*2]:
                    heap[node], heap[node*2] = heap[node*2], heap[node]
                    node = node*2
                # 올바른 위치로 이동했다면 반복 탈출
                else:
                    break

    else:
        # 힙에 push하기
        last += 1
        heap[last] = num    # 힙의 마지막 노드에 넣기
        node = last
        while node > 1:
            if heap[node] <= heap[node//2]:     # 부모 노드보다 작다면? 올바른 위치에 있음
                break

            # 부모 노드보다 크다면 부모와 위치 교체
            heap[node], heap[node//2] = heap[node//2], heap[node]
            node //= 2

# 라이브러리 사용 ver.

# from heapq import heappop, heappush
# import sys
# n = int(input())
# heap = []
#
# for _ in range(n):
#     num = int(sys.stdin.readline())
#     if num == 0:
#         if not heap:
#             print(0)
#         else:
#             print(-heappop(heap))
#     else:
#         heappush(heap, -num)