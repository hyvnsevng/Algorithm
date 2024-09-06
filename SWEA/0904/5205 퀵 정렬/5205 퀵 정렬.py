# import sys
#
# sys.stdin = open('input.txt')

def quick(l, r):
    pivot =
    for

    if l < r:
        s = partition(l, r)
        quick(l, s-1)
        quick(s+1, r)


def partition(a, b):
    p = lst[a]
    i, j = a+1, b

    while i <= j:
        while i <= j and lst[i] <= p:
            i += 1

        while i <= j and lst[j] >= p:
            j -= 1

        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    return j


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    quick(0, len(lst)-1)
    print(lst)
    print(f'#{tc} {lst[n//2]}')

