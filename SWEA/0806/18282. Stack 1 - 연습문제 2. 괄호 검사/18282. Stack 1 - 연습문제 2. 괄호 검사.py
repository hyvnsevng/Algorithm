import sys

sys.stdin = open('input.txt')

def brackets(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return -1
            stack.pop()
    if stack:
        return -1

    return 1

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    string = input().strip()

    print(f'#{tc} {brackets(string)}')
