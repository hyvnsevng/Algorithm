import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    solve = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'
    }

    string = ''
    for _ in range(n):
        tmp = input()
        if not string and '1' in tmp:
            string = tmp

    last = string[::-1].index('1')
    password = string[m-last-56:m-last]

    code = ''

    for i in range(8):
        key = password[7*i:7*(i+1)]
        code += solve[key]

    odd, even, answer = 0, 0, 0
    for i in range(4):
        odd += int(code[i*2])
        even += int(code[i*2+1])
        answer += int(code[i*2]) + int(code[i*2+1])

    print(f'#{tc}', end=' ')
    if not (odd*3+even)%10:
        print(answer)
    else:
        print(0)

