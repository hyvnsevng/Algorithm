import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    equation = input()

    stack = []
    new_equation = ''
    priority = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 0}

    print(new_equation)

    for char in equation:
        if char.isdigit():
            new_equation += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while True:
                top = stack.pop()
                if top == '(':
                    break
                new_equation += top
        elif not priority[char]:
            if stack:
                while priority[stack[-1]]:
                    new_equation += stack.pop()
            stack.append(char)
        elif priority[char]:
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
        elif char == '-':
            stack.append(num1 - num2)
        elif char == '*':
            stack.append(num1 * num2)
        elif char == '/':
            stack.append(num1 / num2)

    print(stack.pop())