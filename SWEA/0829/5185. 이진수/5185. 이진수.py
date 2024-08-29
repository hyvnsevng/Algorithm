import sys

sys.stdin = open('5185_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n, hex = input().split()
    n = int(n)

    hex_dict = {
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    print(f'#{tc}', end=' ')
    for key in hex:
        if key.isdigit():
            key = int(key)
            div = 8
            binary = ''
            for i in range(4):
                binary += str(key//div)
                key %= div
                div //= 2
        else:
            binary = hex_dict[key]
        print(binary, end='')
    print()