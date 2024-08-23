n = int(input())
students = [[] for _ in range(n)]
for i in range(n):
    temp = list(input().split())
    students[i] = list(map(int, temp[1:]))
    students[i].append(temp[0])

students = sorted(students, key = lambda x : (-x[0], x[1], -x[2], x[3]))
for student in students:
    print(student[-1])
