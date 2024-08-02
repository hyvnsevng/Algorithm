T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    n = len(str1)
    m = len(str2)

    ans = 0
    for i in range(m - n + 1):
        if str1 == str2[i:i + n]:
            ans = 1

    print(f'#{tc} {ans}')
