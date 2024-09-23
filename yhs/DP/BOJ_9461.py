# 백준 9461번 파도반 수열

# 전형적인 DP 문제로 삼각형 변의 길이들 사이의 점화식을 찾는다면 간단하게 해결할 수 있는 문제
# 이 문제에서 N번째 삼각형 변의 길이는 N-1번째와 N-5번째 삼각형의 변의 길이의 합으로 나타낼 수 있다.

def dp(n):
    if not table[n]:
        if n < 4:       # n = 1, 2, 3일 때 f(n) = 1
            table[n] = 1
        elif n == 4 or n == 5:      # n = 4, 5 일 때 f(n) = 2
            table[n]=2
        else:
            table[n] = dp(n-1) + dp(n-5)    # 그 외: f(n) = f(n-1) + f(n-5) (n > 5인 정수)

    return table[n]


T = int(input())    # Testcase 개수
lst = []            # Testcase 배열
for _ in range(T):
    num = int(input())
    lst.append(num)

max_num = max(lst)      # Testcase 중 가장 큰 수
table = [0 for _ in range(max_num + 1)]     # DP 테이블의 크기를 Testcase 중 가장 큰 수만큼 초기화
for n in lst:
    print(dp(n))
