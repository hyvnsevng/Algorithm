N = int(input())

timetable = []

for _ in range(N):
    a, b = map(int, input().split())
    timetable.append((a, b))

timetable.sort()

time_list = []

for times in timetable:
    # 시작 : 첫번째 회의 시간 추가
    if not time_list:
        time_list.append(times)

    else:

        
        last_time = time_list[-1]

        # 회의시간(time_list 마지막 요소)과 비교해서 더 짧은 것으로 변경
        if last_time[1] > times[1]:
            time_list.remove(last_time)
            time_list.append(times)
        
        # 다음 회의시간 추가
        elif last_time[1] <= times[0]:
            time_list.append(times)

print(len(time_list))

'''
12 14
8 12
8 11
6 10
5 9
5 7
3 8
3 5
2 13
1 5
0 6'''