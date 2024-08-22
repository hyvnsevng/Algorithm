n, m = map(int, input().split())    # 심사대 수, 심사받을 사람 수
time_lst = [int(input()) for _ in range(n)]     # 입국심사대별 걸리는 시간

time_lst.sort()     # 시간 오름차순 정렬
start, end = 1, m * time_lst[0]     # start, end 초기값
mid = (start+end) // 2

while start < end:
    total = 0   # 시간 내 심사받을 수 있는 사람의 수

    for time in time_lst:
        tmp = mid//time     # 해당 심사대에서 시간 안에 몇 명이 심사를 받을 수 있는가?
        if not tmp:         # 시간 안에 입국심사가 끝나지 않는 심사대 등장 -> 반복 종료
            break
        total += tmp

    if total >= m:       # 더 많은 사람이 심사 받을 수 있느 시간이라면
        end = mid       # 더 작은 범위에서 탐색
    else:               # 더 많은 시간이 필요한 경우
        start = mid+1   # 더 큰 범위에서 탐색
    mid = (start + end) // 2

print(mid)