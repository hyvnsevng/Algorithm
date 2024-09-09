import sys

sys.stdin = open('sample_input.txt')

def zone(r, c, k):
    area = set()
    result = 0
    for i in range(k):
        for j in range(k - i - 1, -1, -1):
            if 0 <= r+i < n and 0 <= c+j < n and city[r + i][c + j]:
                area.add((r+i, c+j))
            if 0 <= r-i < n and 0 <= c+j < n and city[r - i][c + j]:
                area.add((r-i, c+j))
            if 0 <= r+i < n and 0 <= c-j < n and city[r + i][c - j]:
                area.add((r+i, c-j))
            if 0 <= r-i < n and 0 <= c-j < n and city[r - i][c - j]:
                area.add((r-i, c-j))
    result = len(area)
    return result



# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T + 1):
    n, m = map(int, input().split())    # n x n 도시에서 하나의 집이 지불할 비용 m
    city = [list(map(int, input().split())) for _ in range(n)]

    k = 1
    ans = 0
    while True:
        a = ((k-1)//2)*2+1
        if a > n+1:
            break
        cost = k * k + (k - 1) * (k - 1)
        benefit = 0
        # print('k:', k)
        for i in range(n):
            for j in range(n):
                benefit = zone(i, j, k)
                # print(tmp)
                if benefit * m >= cost and benefit >= ans:
                    ans = benefit

        k += 1

    print(f'#{tc} {ans}')

