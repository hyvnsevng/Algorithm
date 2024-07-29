import sys
sys.stdin = open("input (1).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def expo(a, b):

    if a%b:
        return 0

    ans = expo(a/b, b) + 1

    return ans


for test_case in range(1, T + 1):
    N = int(input())

    div = [2, 3, 5, 7, 11]  # 나눌 수
    ans = []

    for i in range(5):
        ans.append(expo(N, div[i]))

        # exp = 0             # 지수
        #
        # # 더이상 나눌 수 없으면 탈출
        # while True:
        #     if N % div[i]:
        #         break
        #
        #     N //= div[i]
        #
        #     exp += 1
        #
        # ans.append(exp)

    print(f'#{test_case}', end=' ')
    for _ in range(5):
        print(ans[_], end=' ')
    print()