import sys

sys.stdin = open('4873_input.txt')

def del_rw(string):
    stack = []
    for char in string:
        if not stack:
            stack.append(char)
            continue
        top = stack.pop()
        if top != char:
            stack.append(top)
            stack.append(char)

    return len(stack)


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    string = input()

    print(f'#{tc} {del_rw(string)}')