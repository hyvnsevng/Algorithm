import sys

sys.stdin = open('4839_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    p, pa, pb = map(int, input().split())

    al, ar, bl, br = 1, p, 1, p

    a_find = False
    b_find = False

    while not a_find and not b_find:
        ac = int((ar + al) / 2)
        bc = int((br + bl) / 2)

        if ac < pa:
            al = ac
        elif ac > pa:
            ar = ac
        else:
            a_find = True

        if bc < pb:
            bl = bc
        elif bc > pb:
            br = bc
        else:
            b_find = True


    if a_find:
        if b_find:
            print(f'#{tc} 0')
        else:
            print(f'#{tc} A')
    else:
        print(f'#{tc} B')
