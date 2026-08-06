import math

def get_dist_square(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

    
def get_min_dist_square(startX, startY, targetX, targetY, m, n):
    dist_squares = []
    
    # 윗쿠
    if not (startX == targetX and startY < targetY):
        dist_squares.append(get_dist_square(startX, startY, targetX, 2 * n - targetY))
    # 아랫쿠
    if not (startX == targetX and startY > targetY):
        dist_squares.append(get_dist_square(startX, startY, targetX, -targetY))
    # 왼쿠
    if not (startY == targetY and startX > targetX):
        dist_squares.append(get_dist_square(startX, startY, -targetX, targetY))
    # 오쿠
    if not (startY == targetY and startX < targetX):
        dist_squares.append(get_dist_square(startX, startY, 2 * m - targetX, targetY))
        
    return min(dist_squares)


def solution(m, n, startX, startY, balls):
    answer = []
    for targetX, targetY in balls:
        answer.append(get_min_dist_square(startX, startY, targetX, targetY, m, n))
    return answer