import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    length = int(input())
    equation = input()
    new_equation = ''
    stack = []
    # priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    priority = {'+': 1, '*': 2}

    for char in equation:
        if char.isdigit():
            new_equation += char
        elif char == '*':
            stack.append(char)
        elif char == '+':
            if stack:
                while stack and stack[-1] == '*':
                    new_equation += stack.pop()
                stack.append(char)
            else:
                stack.append(char)
    while stack:
        new_equation += stack.pop()



    for char in new_equation:
        if char.isdigit():
            stack.append(int(char))
            continue
        num2 = stack.pop()
        num1 = stack.pop()
        if char == '+':
            stack.append(num1 + num2)
        elif char == '*':
            stack.append(num1*num2)

    print(f'#{tc}, {stack.pop()}')

