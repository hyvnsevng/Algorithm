import sys

sys.stdin = open('input.txt')

def recursive(mit, jisu):
    if jisu == 1:
        return mit

    return mit*recursive(mit, jisu-1)

# Testcase 수
T = 10
# Testcase 만큼 반복
for _ in range(1, T+1):
    tc = int(input())
    mit, jisu = map(int, input().split())

    answer = recursive(mit, jisu)
    print(f'#{tc} {answer}')