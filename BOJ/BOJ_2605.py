# 백준 2605 줄 세우기
'''
출력 형식을 착각해서 여러번 수정했다. 반드시 문제에서 요구하는 형식대로 출력할 수 있도록 코드 작성에 유의할 것.
'''

n = int(input())
students = list(map(int, input().split()))

line = []
for i in range(len(students)):
    line.insert(students[i], i+1)

print(*line[::-1])