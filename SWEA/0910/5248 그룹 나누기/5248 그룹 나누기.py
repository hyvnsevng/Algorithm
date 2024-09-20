import sys

sys.stdin = open('5248_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    union = [[] for _ in range(n+1)]
    for i in range(m):
        head = lst[i*2]
        tail = lst[i*2+1]
        if not union[head] and not union[tail]:
            tmp = [head, [head, tail]]
            union[head], union[tail] = tmp, tmp
        else:
            if union[head]:
                tmp1 = union[head][1]
            else:
                tmp1 = [head]
            if union[tail]:
                tmp2 = union[tail][1]
            else:
                tmp2 = [tail]
            tmp = tmp1 + tmp2
            for num in tmp:
                union[num] = [head, tmp]

    count = 0
    union_set = set()
    for i in range(1, n+1):
        if not union[i]:
            count += 1
        else:
            union_set.add(union[i][0])

    print(f'#{tc} {count + len(union_set)}')

