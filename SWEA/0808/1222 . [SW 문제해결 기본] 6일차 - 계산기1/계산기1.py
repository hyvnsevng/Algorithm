import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    eq = input()
    result = ''
    stack = []

    for char in eq:
        if char.isdigit():
            result += char
        else:
            if stack and stack[-1] == '+':
                result += stack.pop()
                stack.append(char)
            else:
                stack.append(char)
    while stack:
        result += stack.pop()

    for char in result:
        if char.isdigit():
            stack.append(char)
        elif char == '+':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(int(num1)+int(num2))

    print(f'#{tc} {stack.pop()}')
