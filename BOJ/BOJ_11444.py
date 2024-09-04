# 백준 11444번 피보나치 수 6

# 2배수번째의 피보나치 수의 관계를 찾아야 했음 (가장 중요)!
# 이후 홀/짝에 따라 DP테이블 갱신하여 답 도출하기

def dp(num, depth):
    if not table[depth]:

        if num == 2:
            table[depth] = [1, 1]
        elif num == 3:
            table[depth] = [2, 1]
        else:
            lst = dp(num // 2, depth - 1)
            if num % 2: # 홀수인 경우
                a = (lst[0]**2 + (lst[0]+lst[1])**2) % 1000000007
                b = (lst[0]*(lst[0] + 2*lst[1])) % 1000000007
                table[depth] = [a, b]
            else:
                a = (lst[0]*(lst[0] + 2*lst[1])) % 1000000007
                b = (lst[0]**2 + lst[1]**2) % 1000000007
                table[depth] = [a, b]

    return table[depth]


n = int(input())
mox = n
length = 0
while mox > 1:
    mox //= 2
    length += 1

# print(length)

table = [[] for _ in range(length)]

if n == 1:
    print(1)
else:
    print(dp(n, length-2)[0])

# dp[k] = x면 dp[nk] = ak
# dp[k] = dp[a+1]*dp[k-a] + dp[a]*dp[k-a-1]
# dp[2k] = dp[k]*(dp[k] + 2*dp[k-1])
# dp[2k+1] = dp[k+1]**2 + dp[k]**2 = (dp[k] + dp[k-1])**2 + dp[k]**2