n = int(input())
prices = list(map(int, input().split()))
m = int(input())
ans = ""

flag = False
dummy = min(prices)

while m > 0:
    min_p = 51
    max_nl = 0      # 만들 수 있는 숫자 길이
    num = n
    for i in range(n-1, 0-flag, -1):
        p = prices[i]
        nl = int((m-p)/dummy)+1
        if p <= m and nl > max_nl:
            min_p = p
            max_nl = nl
            num = i
    if not flag:
        flag = True
    if num == n:
        break
    m -= min_p
    ans += str(num)

print(0 if ans == '' else ans)
