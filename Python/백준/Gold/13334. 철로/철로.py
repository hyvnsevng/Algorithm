import sys
import heapq
input = sys.stdin.readline

n = int(input())
locs = []
for _ in range(n):
    h, o = map(int, input().split())
    if h < o:
        locs.append((h, o))
    else:
        locs.append((o, h))

d = int(input())

# d보다 간격이 긴 경우 미리 제거
locs = [(a, b) for a, b in locs if b - a <= d]
# 끝점 기준 오름차순 정렬
locs.sort(key=lambda x: x[1])  # (start, end) 중 end 기준

heap = []  # 시작점들을 담는 최소 힙
ans = 0

for a, b in locs:
    # 현재 구간을 후보에 추가(작은 수 추가)
    heapq.heappush(heap, a)

    # 작은 수 < b - d 인 것들 pop
    left = b - d
    while heap and heap[0] < left:
        heapq.heappop(heap)

    # 힙에 남아 있는 구간 수 = 현재 [b-d, b] 선분 안에 들어오는 사람 수
    ans = max(ans, len(heap))

print(ans)