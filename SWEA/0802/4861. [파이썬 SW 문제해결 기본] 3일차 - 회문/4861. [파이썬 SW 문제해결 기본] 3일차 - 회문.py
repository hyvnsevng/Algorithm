import sys

sys.stdin = open('4861_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(int, input().split())            # n x n 행렬에서 길이가 m인 회문 찾기

    puzzle = [input() for _ in range(n)]


    # print('puzzle')
    # print(puzzle)
    puzzle_t = list(zip(*puzzle))
    # print(puzzle_t)

    for i in range(n):
        for j in range(n-m+1):
            string = puzzle[i][j:j+m]
            # print(puzzle[j:j+m][i])
            if string == string[::-1]:
                print(f'#{tc} {string}')
            string = puzzle_t[i][j:j+m]
            # print(string)
            if string == string[::-1]:
                print(f'#{tc}', end=' ')
                for letter in string:
                    print(letter, end='')
                print()




'''
짝수
se : se + n//2
se + n -1 : se + n//2 -1

홀수
se : se + n//2
se + n -1 : se + n//2
len = 5
0 : 2, 4: 2
'''