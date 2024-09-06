import sys

# sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    ans = 0
    for b in B:
        left, right, find = True, True, True
        start, end = 0, len(A)-1

        while start <= end:
            mid = (start+end)//2

            if A[mid] == b:
                if find:
                    ans += 1
                break

            elif A[mid] < b:
                left = True
                if not right:
                    find = False
                right = False
                start = mid + 1

            else:
                right = True
                if not left:
                    find = False
                left = False
                end = mid - 1

    print(f'#{tc} {ans}')
