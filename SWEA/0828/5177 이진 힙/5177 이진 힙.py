import sys

sys.stdin = open('5177_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    heap = [0, lst[0]]
    for i in range(2, n+1):
        heap.append(lst[i-1])
        jasik = i
        bumo = i//2
        while bumo > 0:
            if heap[bumo] > heap[jasik]:
                heap[bumo], heap[jasik] = heap[jasik], heap[bumo]
                jasik //= 2
                bumo = jasik//2
            else:
                break

    # print(heap)

    num = (len(heap)-1)//2
    answer = 0

    while num > 0:
        answer += heap[num]
        num //= 2

    print(f'#{tc} {answer}')
