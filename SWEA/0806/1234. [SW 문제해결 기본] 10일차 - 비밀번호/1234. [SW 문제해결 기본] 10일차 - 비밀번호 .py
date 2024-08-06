import sys

sys.stdin = open('input.txt')

def password(string):
    stack = []

    for char in string:
        if not stack:
            stack.append(char)
            continue

        top = stack.pop()
        if top != char:
            stack.append(top)
            stack.append(char)

    return stack

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, string = map(str, input().split())
    n = int(n)

    # print(n, string)

    result = password(string)
    answer = str()
    for char in result:
        answer += char
    print(f'#{tc} {answer}')
