n = int(input())

eq = input()

nums = []
for i in range(n):
    nums.append(int(input()))

stack = []
for char in eq:
    if char.isalpha():
        stack.append(nums[ord(char)-65])

    elif char == '+':
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 + num2)

    elif char == '-':
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 - num2)

    elif char == '*':
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 * num2)

    elif char == '/':
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 / num2)

    # print(stack[-1])
ans = "{:.2f}".format(stack.pop())
print(ans)