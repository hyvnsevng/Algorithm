import sys

sys.stdin = open('input.txt')

def rot_cw(arr):
    n = len(arr)

    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        temp = str()
        for j in range(n):
            temp += str(arr[n-1-j][i])
        result[i] = temp

    return result


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    arr90 = rot_cw(arr)
    arr180 = rot_cw(arr90)
    arr270 = rot_cw(arr180)


    print(f'#{tc}')
    for i in range(N):
        print(arr90[i], arr180[i], arr270[i])