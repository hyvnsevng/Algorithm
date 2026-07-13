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


def find_tictactoe(r, c, turn, board, n):
    # 가로or세로 찾기
    if find_row(turn, board, n, r) or find_col(turn, board, n, c):
        return True
        
    # 대각선 찾기
    if find_desc_diag(turn, board, n) or find_asc_diag(turn, board, n):
        return True
    
    return False
    

def dfs(n, board, curr, turn='O', r=-1, c=-1):
    if r >= 0 and find_tictactoe(r, c, 'O' if turn == 'X' else 'X', curr, n):
        for i in range(n):
            for j in range(n):
                if board[i][j] != curr[i][j]:
                    return 0
        return 1
    
    same = True
    for i in range(n):
        for j in range(n):
            # 아직 board가 완성되지 않은 경우
            if board[i][j] != curr[i][j]:
                same = False
                
            # 현재 턴 중 가능한 경우 탐색하기
            if board[i][j] == turn and curr[i][j] == '.':
                same = False
                curr[i][j] = turn
                res = dfs(n, board, curr, 'X' if turn == 'O' else 'O', i, j)
                
                # board가 가능한 경우 1 반환
                if res == 1:
                    return 1
                curr[i][j] = '.'
                
    # board가 가능한 경우 1 반환
    if same:
        return 1
    
    return 0
    

def solution(board):
    n = 3
    curr = [['.'] * n for _ in range(n)]
    answer = dfs(n, board, curr)
    return answer
