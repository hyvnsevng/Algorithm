# import sys
#
# sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())

    new_arr = [[False for _ in range(N)] for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    di = 0
    row = 0
    col = -1

    sorted_arr = [x for x in range(1, N**2+1)]

    for i in range(N**2):

        ni, nj = dr[di], dc[di]
        row += ni
        col += nj
        new_arr[row][col] = sorted_arr[i]

        if not 0 <= row+ni < N or not 0 <= col+nj < N or new_arr[row+ni][col+nj]:
            di = (di+1)%4

    print(f'#{tc}')
    for row in new_arr:
        for col in row:
            print(col, end = ' ')
        print()




    # 0, 5, 1
    # 4, -1, -1

    # 0, 6, 1
    # 5, -1, -1

    # (N//2)*((-1)**(i%2)+1)