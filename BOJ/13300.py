# 백준 13300 방 배정

n, k = map(int, input().split())        # n : 학생 수, k : 방 최대 인원 수

# 학생 정보 : 성별(0,1) 학년(1~6)
student_infos = [list(map(int, input().split())) for _ in range(n)]
student_infos.sort()

lst = [1]

for i in range(len(student_infos) -1):
    student = student_infos[i]
    if student == student_infos[i+1]:
        lst[-1] += 1
    else:
        lst.append(1)

rooms = 0

for num in lst:
    if num > k:
        rooms += num // k
        if num % k:
            rooms += 1

    else:
        rooms += 1

print(rooms)
# 학생 성별(0, 1)과 학년(1~6)
'''
방 개수가 k로 나누어 떨어질 때를 고려하지 못했다.
다양한 케이스를 print 찍어보면서 확인하면 좋을듯?
'''