def solution(n):
    answer = 0
    div = 1000000007
    
    if n % 2 == 1:
        return answer
    
    # f(2k): 가로 배치로 끝나는 경우의 수 / g(2k): 세로 배치로 끝나는 경우의 수
    table = [[0, 0] for _ in range(n // 2)]     # [f(2i), g(2i)]
    table[0] = [1, 2]
    for i in range(1, n // 2):
        # 가로 배치로 끝날 때: 2(i-1) 직사각형에서 가로로 세 개 이어붙이기
        table[i][0] = (table[i-1][0] + table[i-1][1]) % div
        # 세로 배치로 끝날 때: 2(i-1) 직사각형에서 이어붙이는 경우 2가지 + g(2(i-1))에서 |=|로 이어붙이기 
        table[i][1] = (2 * table[i-1][0] + 3 * table[i-1][1]) % div
        
    answer = sum(table[-1]) % div
    return answer