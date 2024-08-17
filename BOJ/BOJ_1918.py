equation = input()

stack = []
new_equation = ''

priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

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

    elif priority[char] == 1:
        while stack and priority[stack[-1]] >= 1:
            top = stack.pop()
            new_equation += top
        stack.append(char)

    elif priority[char] == 2:
        while stack and priority[stack[-1]] >= 2:
            top = stack.pop()
            new_equation += top
        stack.append(char)

while stack:
    new_equation += stack.pop()

print(new_equation)


