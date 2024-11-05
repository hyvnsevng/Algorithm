# 백준 6064번 카잉 달력

T = int(input())

for tc in range(1, T + 1):
    n, m, x, y = map(int, input().split())

    # 최소공배수 구하기
    gcd = 0
    for i in range(max(n, m), n*m+1, max(n, m)):
        if not i % n and not i % m:
            gcd = i
            break

    # 정답 구하기
    i = 0
    ans = -1
    while n * i + x <= gcd:
        if m == y:
            if (n * i + x) % m == 0:
                ans = n * i + x
                break
        else:
            if (n * i + x) % m == y:
                ans = n * i + x
                break

        i += 1

    print(ans)

'''
    기존 코드와의 차이점
    1. 너무 하드 코딩이었다. n이나 m이 1일 때 각각 예외 케이스를 두고 출력으로 끝낸다? 별로 바람직한 방법은 아닌듯.
    if n == 1:
        print(y)
        continue
    if m == 1:
        print(x)
        continue

    2. 최소공배수 구하는 방법이 비효율적.
        굳이 배열을 만들어서 메모리를 낭비하는 방법
    # 최소공배수 구하기
    lcm_lst = []
    for i in range(n, n*m, n):
        if i not in lcm_lst:
            lcm_lst.append(i)

    lcm = n * m
    for num in lcm_lst:
        if num % m == 0:
            lcm = num
            break

    ans = -1

    3. n == x, 혹은 m == y인 경우
    나머지가 0으로 처리되지만 실제 표현식의 결과값은 x, 혹은 y가 나와야 함
    이에 대한 처리를 해주지 않았다.
    
    if n > m:
        mox = n
        rem = y
    else:
        mox = m
        rem = x

    while True:
        if rem % m == x and rem % n == y:
            break

    print(ans)
'''
