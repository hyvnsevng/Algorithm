def find_row(turn, board, n, r):
    for c in range(n):
        if board[r][c] != turn:
            return False
        
    return True


def find_col(turn, board, n, c):
    for r in range(n):
        if board[r][c] != turn:
            return False
        
    return True


def find_desc_diag(turn, board, n):
    for i in range(n):
        if board[i][i] != turn:
            return False
        
    return True


def find_asc_diag(turn, board, n):
    for i in range(n):
        if board[i][n - i - 1] != turn:
            return False
        
    return True


def find_tictactoe(turn, board, n):
    # 가로or세로 찾기
    for i in range(n):
        if find_row(turn, board, n, i) or find_col(turn, board, n, i):
            return 1
        
    # 대각선 찾기
    if find_desc_diag(turn, board, n) or find_asc_diag(turn, board, n):
        return 1
    
    return 0


def solution(board):
    n = 3
    
    O_cnt, X_cnt = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'O':
                O_cnt += 1
            elif board[i][j] == 'X':
                X_cnt += 1
    
    """
    가능한 경우
    1. O가 X보다 1개 많고 X 빙고가 없어야 함
    2. O가 X랑 개수가 같고 O 빙고가 없어야 함
    """
    if O_cnt == X_cnt + 1:
        if find_tictactoe('X', board, n):
            return 0
        return 1
    elif O_cnt == X_cnt:
        if find_tictactoe('O', board, n):
            return 0
        return 1
    
    return 0
