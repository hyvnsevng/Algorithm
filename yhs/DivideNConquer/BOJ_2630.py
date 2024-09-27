# 백준 2630번 색종이 만들기

# 분할 정복을 이용하여 풀이하였다.
# 1. 색종이 전체에서 시작해 4개의 사분면으로 나누어 함수를 재귀호출한다.
# 2. 각 함수는 영역 내 (흰 색종이의 개수, 파란 색종이의 개수)를 튜플로 반환한다.
# 3. 만약 한 종류의 색종이만 존재한다면 (1, 0) 혹은 (0, 1)을 반환한다.
# 4. 두 종류의 색종이 모두 존재한다면 각 색종이의 개수를 있는 그대로 반환한다.


def divide(row_start, row_end, col_start, col_end):
    if row_end - row_start == 1:
        if graph[row_start][col_start]:
            return 0, 1
        else:
            return 1, 0

    white, blue = 0, 0
    for i in range(2):
        for j in range(2):
            rs = row_start + i*(row_end-row_start)//2
            re = (row_start+row_end)//2 + i*(row_end-row_start)//2
            cs = col_start + j*(col_end-col_start)//2
            ce = (col_start + col_end) // 2 + j * (col_end - col_start) // 2
            white_tmp, blue_tmp = divide(rs, re, cs, ce)
            white += white_tmp
            blue += blue_tmp
    if white == 0:
        return 0, 1
    elif blue == 0:
        return 1, 0
    else:
        return white, blue


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

white, blue = divide(0, n, 0, n)
print(white)
print(blue)