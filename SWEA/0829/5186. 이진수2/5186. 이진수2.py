import sys

sys.stdin = open('5186_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    num = float(input())
    # print(num)

    binary = ''
    for i in range(13):
        div = 2**(-i-1)
        # print(div)
        binary += str(int(num//div))
        # print(binary)
        num %= div
        if num == 0:
            break

    if num == 0:
        print(f'#{tc} {binary}')
    else:
        print(f'#{tc} overflow')