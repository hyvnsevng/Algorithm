def get_modem(arr, interval):

    '''
    :param arr: 집 위치 배열
    :param interval: 최소간격
    :return: 최소 간격을 interval로 했을 때 몇개의 집에 공유기를 설치할 수 있는가?
    '''

    pos = arr[0]
    total = 0
    for home in arr:
        if home >= pos:
            total += 1
            pos = home + interval

    return total


n, c = map(int, input().split())
modem = [int(input()) for _ in range(n)]

modem.sort()

start = 1
end = modem[n-1] - modem[0]

while start < end:
    mid = (start + end + 1) // 2
    result = get_modem(modem, mid)
    # print(start, mid, end)
    # print(result)
    if result >= c:          # 더 많은 집에 공유기 설치 가능 -> 간격 넓혀서 탐색
        start = mid
    elif result < c:        # 이 간격으로는 부족하다 -> 간격 좁혀서 탐색
        end = mid - 1

print((start+end)//2)