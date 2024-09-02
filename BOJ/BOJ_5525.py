n = int(input())
m = int(input())
s = input()

find = False
idx = 0
check = 0
ans = 0
for i in range(m):
    if find:
        if i % 2 == idx % 2 and s[i] == 'I':
            check += 1
            continue
        elif i % 2 != idx % 2 and s[i] == 'O':
            check += 1
            continue
        else:
            if check // 2 >= n:
                ans += (check // 2) - n + 1
            check = 0
            find = False

    if s[i] == 'I':
        idx = i
        find = True
else:
    if check // 2 >= n:
        ans += (check // 2) - n + 1

print(ans)