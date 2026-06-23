def rotate(matrix, x1, y1, x2, y2):
    x, y = x1 - 1, y1 - 1
    res = matrix[x][y]
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(4):
        reps = y2 - y1 if i % 2 else x2 - x1
        if i == 3:
            reps -= 1
        dx, dy = d[i]
        for _ in range(reps):            
            matrix[x][y], matrix[x + dx][y + dy] = matrix[x + dx][y + dy], matrix[x][y]
            res = min(res, matrix[x][y])
            x += dx
            y += dy
        
    return res
    

def solution(rows, columns, queries):
    matrix = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    answer = []
    print(matrix)
    for query in queries:
        answer.append(rotate(matrix, *query))
    return answer