from heapq import heappop, heappush

tc = int(input())

for _ in range(tc):
    k = int(input())

    max_heap = list()
    min_heap = list()
    nums_cnt = dict()

    for __ in range(k):
        task, num = input().split()
        num = int(num)
        if task == "I":
            heappush(max_heap, -num)
            heappush(min_heap, num)
            nums_cnt[num] = nums_cnt.get(num, 0) + 1

        elif task == "D" and len(nums_cnt):
            # 최대값 pop
            if num == 1:
                while -max_heap[0] not in nums_cnt:
                    heappop(max_heap)
                val = -heappop(max_heap)
                nums_cnt[val] -= 1
                if nums_cnt[val] == 0:
                    del nums_cnt[val]

            # 최소값 pop
            elif num == -1:
                while min_heap[0] not in nums_cnt:
                    heappop(min_heap)
                val = heappop(min_heap)
                nums_cnt[val] -= 1
                if nums_cnt[val] == 0:
                    del nums_cnt[val]

    while max_heap and -max_heap[0] not in nums_cnt:
        heappop(max_heap)
    while min_heap and min_heap[0] not in nums_cnt:
        heappop(min_heap)
    if nums_cnt.items():
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")
