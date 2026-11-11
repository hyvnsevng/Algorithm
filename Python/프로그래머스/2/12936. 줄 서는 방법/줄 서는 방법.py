def solution(n, k):
    dims = [1] * n
    for i in range(1, n):
        dims[i] = dims[i - 1] * (i + 1)
    dims.reverse()
    
    answer = []
    visited = set()
    for i in range(n):
        remainder = (k - 1) % dims[i]
        # 1~n 중 answer에 없는 애들 정렬한 리스트
        arr = [x for x in range(1, n + 1) if x not in visited]
        
        # 리스트에서 나머지 구해서 추가
        # dims[i]를 n-i로 분할. -> 몇번째에 속하는가?
        # 예를 들어 dims[i] = 24이면 나올 수 있는 수는 4개. k 6개 파티션으로 나눈다. 이 때 몫으로 정함. 
        idx = remainder // (dims[i] // (n - i))
        answer.append(arr[idx])
        visited.add(arr[idx])    
        
    return answer