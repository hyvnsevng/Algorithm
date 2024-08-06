# import sys
#
# sys.stdin = open('input.txt')

def pascal(n):
    if n==1:
        print(1)
        return [1]
    else:
        lst = pascal(n-1)
        result = [1 for _ in range(n)]
        for i in range(n-2):
            result[i+1] = lst[i] + lst[i+1]

        print(*result)
        return result


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    print(f'#{tc}')
    pascal(int(input()))



# n = int(input())
#
# pascal = [[1] * x for x in range(1, n + 1)]
#
# for i in range(n):
#     print(*pascal[i])