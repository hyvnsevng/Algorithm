
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    string = input()
    n = len(string)

    idx1 = n // 2
    if n % 2:
        idx2 = idx1
    else:
        idx2 = idx1-1

    # print(n, string[:idx1], string[n-1:idx2:-1])
    if string[:idx1] == string[n-1:idx2:-1]:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')
    '''
    5: [0:2], [n-1:2]
    6: [0:3], [n-1:3-1]
    '''