import sys

sys.stdin = open('4869_input.txt')

def buchigi(n):
    if n == 1:
        return 1    # 10 짜리 세로로
    elif n == 2:    # 20 짜리 or 10짜리 2개 세로로 or 10짜리 2개 가로로
        return 3
    else:
        # n-1 뒤에 10 세로로 붙이는 경우 + n-2 뒤에 10짜리 2개 가로 or 20짜리 1개 붙이는 경우
        # 10짜리 2개 세로로 붙이는 경우는 n-1과 겹침
        return buchigi(n-1)+2*buchigi(n-2)

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())//10
    print(f'#{tc} {buchigi(n)}')

