import sys

sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    print(tc)
    n, m = map(int, input().split())

    # solve = {
    #     [3, 2, 1, 1: '0',
    #     [2, 2, 2, 1]: '1',
    #     [2, 1, 2, 2]: '2',
    #     [1, 4, 1, 1]: '3',
    #     [1, 1, 3, 2]: '4',
    #     [1, 2, 3, 1]: '5',
    #     [1, 1, 1, 4]: '6',
    #     [1, 3, 1, 2]: '7',
    #     [1, 2, 1, 3]: '8',
    #     [3, 1, 1, 2]: '9'
    # }

    strings = []
    for _ in range(n):
        tmp = int(input(), 16)

        tmp = bin(tmp)[2:].rstrip('0')

        if '1' not in tmp:          #
            continue

        codes = []

        r1, r2, r3 = 0
        while True:
            # if len(tmp) < 56*i:
            #     string = '0'*(56*i-len(tmp))+tmp
            #     if string not in strings:
            #         strings.append(string)
            #     break

            r1, r2, r3 = 0
            for char in tmp[::-1]:
                if char == '1':
                    if not r2:
                        r1 += 1
                    else:
                        r3 += 1
                else:
                    if r3:
                        break
                    else:
                        r2 += 1

            r = min(r1, r2, r3)
            ratio = [r1//r, r2//r, r3//r]

            string = tmp[len(tmp)-56*r:]
            code = ''
            for i in range(8):
                char = ''
                for j in range(7):
                    char += string[r*(i*7+j)]

                code += asldkfj;aseiov


