# 백준 1874번 스택 수열

n = int(input())

ans = []
stack = []
last = 0
for i in range(1, n+1):
    num = int(input())

    if num > last:
        for j in range(last+1, num+1):
            stack.append(j)
            ans.append('+')
        stack.pop()
        ans.append('-')
        last = num
    else:
        if num != stack[-1]:
            print('NO')
            break
        ans.append('-')
        stack.pop()

else:
    for calc in ans:
        print(calc)