import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    puzzle = [input() for _ in range(8)]

    print(puzzle)

    answer1 = 0
    answer = 0
    print(n, (n-1)//2, 8-n//2)

    print((n-1)//2-n, (n-1)//2+1)
    for i in range(9-n):
        for j in range(8):
            if not n%2:     # 짝수일 때
                if puzzle[j][i:i+n//2] == puzzle[j][i+n-1:i-1+n//2:-1]:
                    answer1 += 1
                if puzzle[i][j:j+n//2] == puzzle[i][j+n-1:j-1+n//2:-1]:
                    answer1 += 1
            else:           # 홀수일 때
                if puzzle[j][i:i+n//2] == puzzle[j][i+n:i+n//2:-1]:
                    answer += 1
                if puzzle[i][j:j-n//2:-1] == puzzle[i][j+1:j+1+n//2]:
                    answer += 1
            # print(puzzle[j])


    print(answer1)
'''
[
i~i+n//2
i+n//2+1~i+n
i+n-1~i+n//2
3: 1, 7
4: 1, 6
'CBBCBAAB', 
'CCCBABCB', 
'CAAAACAB', 
'BACCCCAC', 
'AABCBBAC', 
'ACAACABC', 
'BCCBAABC', 
'ABBBCCAA'
]

['BCBBCACA', 'BCAAACAC', 'ABACBCCB', 'AACBCBCA', 'ACACBAAA', 'ACCACCCB', 'AACAAABA', 'CACCABCB']
['BABBBACB', 'ABCAACCB', 'CCACBCBA', 'CACACBCA', 'CCABACCB', 'CCBAAAAA', 'BBACBACA', 'CBCCBABC']
['ACBBCCCA', 'CCBCBACB', 'ACBCABAA', 'BABCCAAA', 'ACCCCCBB', 'AABBCCBC', 'CCABBACA', 'CAACBCCC']
['AAACACAB', 'CCABCCCC', 'CABCAAAA', 'BBBCBBBA', 'ABCCACCC', 'ABACBCBB', 'CBABACAB', 'BBBBBABB']
['ABCBCBCA', 'ABCBCCCB', 'ABACCCCA', 'BBABBBAC', 'BBACBCCC', 'AAACACCA', 'BABCCCBC', 'ACCBCBCA']
['CACBCCBA', 'CBCCBCCA', 'CCBCBCAB', 'BBCCABAA', 'CACCBCCC', 'BCCACCBB', 'CBCCCBBC', 'CBACBCBC']
['BCBABCBA', 'CBBABABC', 'BCACBAAA', 'BBABACAB', 'BCBCCBAC', 'CBBCBBBB', 'CBBAACAB', 'ACCBCBCC']
['BBBBCCAA', 'BCBBCACC', 'BBCAAAAB', 'ABABBABB', 'BACAAABA', 'ABACCBCA', 'ACCAABCB', 'BACCACBA']
['BCCCACCB', 'CABCACAB', 'BAACCCAC', 'BBABBABC', 'CCABABCA', 'CABABACC', 'CBACACAB', 'CBCCCBAB']

'''