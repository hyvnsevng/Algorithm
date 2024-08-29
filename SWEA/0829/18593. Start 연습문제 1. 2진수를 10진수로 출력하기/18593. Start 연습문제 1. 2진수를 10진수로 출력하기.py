import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n = int(input())

    bit = ''
    for _ in range(n):
        bit += input().strip()          # 문자열 전부 이어붙이기

    print(f'#{tc}', end='')
    for i in range(10):
        binary_num = bit[i*7:(i+1)*7]   # 7개 단위로 자르기

        num, j = 0, 2**6
        # 2 -> 10진수 변환
        for char in binary_num:
            num += int(char)*j
            j //= 2

        print(f' {num}', end='')
    print()
