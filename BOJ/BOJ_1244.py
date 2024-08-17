n_switch = int(input())
switches = list(map(int, input().split()))

students = []
n_student = int(input())
for _ in range(n_student):
    lst = list(map(int, input().split()))
    students.append(lst)

state = [1, 0]

for student in students:
    idx = student[1]

    if student[0] == 1:
        i = 1
        while idx*i-1 < n_switch:
            switches[idx*i-1] = state[switches[idx*i-1]]
            i += 1

    else:
        i = 0
        while idx+i-1 < n_switch and idx-i-1 >= 0:
            s1, s2 = switches[idx-i-1], switches[idx+i-1]
            if s1 != s2:
                break

            switches[idx-i-1], switches[idx+i-1] = state[s1], state[s1]
            i+=1

for i in range(n_switch):
    if i > 0 and not i % 20:
        print()
    print(switches[i], end=' ')
