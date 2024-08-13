import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())    # 팰린드롬 길이
    graph_row = [list(input()) for _ in range(8)]   # 가로방향 회문 확인
    # print(graph_row)
    graph_col = [[0 for _ in range(8)] for _ in range(8)]   # 세로방향 회문 확인
    for i in range(8):
        for j in range(8):
            graph_col[i][j] = graph_row[j][i]

    # 가로, 세로 회문 여부
    row_palindrome = True
    col_palindrome = True
    # 총 회문 개수
    answer = 0

    for i in range(8):
        for j in range(8-n+1):
            row_string = graph_row[i][j:j+n]    # 가로방향 문자열
            col_string = graph_col[i][j:j+n]    # 세로방향 문자열
            # 회문여부 확인
            for k in range(n//2):
                # print(k)
                if row_string[k] != row_string[n-1-k]:
                    row_palindrome = False
                if col_string[k] != col_string[n-1-k]:
                    col_palindrome = False

            # 회문 개수 더하기
            if row_palindrome:
                answer += 1
            if col_palindrome:
                answer += 1
            # 회문 여부 초기화
            row_palindrome, col_palindrome = True, True

    print(f'#{tc} {answer}')