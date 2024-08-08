import sys

sys.stdin = open('input.txt')

def sort_time(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m, k = map(int, input().split())     # 손님 n명, m초에 k개 만들 수 있음
    time = list(map(int, input().split()))
    time = sort_time(time)  # 시간 오름차순으로 정렬

    # 시간 배열을 k개 단위로 자름
    # 만약 k개 단위로 자른 x번째 배열의 가장 앞 시간이 m*x보다 이른 시간이면 불가능
    for i in range(0, n, k):
        if time[i] < m*(i//k+1):
            print(f'#{tc} Impossible')
            break
    # 위의 조건에 걸리지 않는다면 가능
    else:
        print(f'#{tc} Possible')

