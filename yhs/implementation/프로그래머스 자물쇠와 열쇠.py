from copy import deepcopy

def solution(key, lock):
    M = len(key)
    N = len(lock)

    # 행렬 돌리기
    def rotation(matrix, N):
        result = [[0 for i in range(N)] for i in range(N)]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                result[i][j] = matrix[N-1-j][i]

        return result
    
    # 행렬 세트화
    def make_set(matrix):
        res = set()
        for row in matrix:
            res.update(set(row))
        return res
    
    rotated_key = deepcopy(key)    
    # copied_lock = deepcopy(lock)
    # 열쇠+키 확인
    for _ in range(4):
        # key 이동 (최대 N+M-1만큼)
        for i in range(1, N+M):
            for j in range(1, N+M):
                # print(f"x: +{j}     y: +{i}:")
                # 행렬 복사
                copied_lock = deepcopy(lock)

                # key와 lock 겹치는 모든 부분 더하기
                for k in range(i):
                    for l in range(j):
                        try:
                            if M-i+k >= 0 and M-j+l >= 0:
                                copied_lock[k][l] += rotated_key[M-i+k][M-j+l]
                                # print(k, l)
                        except IndexError:
                            pass

        

                
                # for _ in copied_lock:
                #     print(_)
                #     print('--------')

                # lock에 key 맞췄을 때 lock의 요소가 모두 1이면 True 반환
                if make_set(copied_lock) == {1}:
                    return True
        
        # 90도 돌려서 다시 반복
        rotated_key = rotation(rotated_key, M)
        
                
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	



print(solution(key, lock))

# mtrx = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]


# [[13, 9, 5, 1], 
#  [14, 10, 6, 2], 
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]
#  ]
