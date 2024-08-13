import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for _ in range(1, T+1):
    tc = int(input())
    words = [list(input()) for _ in range(100)]
    words_t = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        for j in range(100):
            words_t[i][j] = words[j][i]

    max_len = 0
    for n in range(100, 0, -1):
        for i in range(100):
            for j in range(100-n):
                string1 = words[i][j:j+n]
                string2 = words_t[i][j:j+n]

                if string1[0:n//2] == string1[n-1:(n-1)//2:-1]:
                    length1 = len(string1)
                    if length1 > max_len:
                        max_len = length1

                if string2[0:n//2] == string2[n-1:(n-1)//2:-1]:
                    length2 = len(string2)
                    if length2 > max_len:
                        max_len = length2

    print(f'#{tc} {max_len}')
