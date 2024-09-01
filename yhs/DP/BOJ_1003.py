# 백준 1003번 피보나치 함수

# 피보나치 함수에서 0과 1이 인자로 들어가는 경우가 몇번인지 세는 문제
# 피보나치 함수와 동일하게 n-1과 n-2의 결과값을 더한 것과 같다.


def call_fibonacci(n):
    global dp

    if not dp[n]:
        if n == 0:
            dp[0] = [1, 0]
        elif n == 1:
            dp[1] = [0, 1]
        else:
            fibo1, fibo2 = call_fibonacci(n-1), call_fibonacci(n-2)
            dp[n] = [fibo1[0] + fibo2[0], fibo1[1]+fibo2[1]]

    return dp[n]


T = int(input())
dp = [[] for _ in range(40 + 1)]
for _ in range(T):
    n = int(input())
    print(*call_fibonacci(n))

