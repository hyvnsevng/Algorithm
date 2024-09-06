import sys
n = int(sys.stdin.readline())

for _ in range(n):
    ps = sys.stdin.readline().strip()
    op, cl = 0, 0
    for char in ps:
        if char == '(':
            op += 1
        else:
            cl += 1

        if op < cl:
            print('NO')
            break
    else:
        if op == cl:
            print('YES')
        else:
            print('NO')

