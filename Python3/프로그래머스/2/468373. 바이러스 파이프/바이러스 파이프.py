def dfs(edges, k, infected, cnt = 0, curr = 0):
    
    # k번 수행 시 return
    if cnt == k:
        return len(infected)
    
    res = len(infected)
    for i in range(1, 4):
        # 마지막으로 열었다 닫은 파이프와 같은 종류일 경우 건너뛰기
        if i == curr:
            continue
            
        # 파이프 연 후 감염된 집합 계산
        candidates = get_set(edges, infected, i) | infected
        res = max(res, dfs(edges, k, candidates, cnt + 1, i))
                
    return res
    

def get_set(edges, infected, t):
    
    stack = list(infected)
    visited = set() # 방문 노드 == 새로 감염된 배양체
    
    while stack:
        u = stack.pop()
        
        # 이미 방문했을 경우 건너뛰기
        if u in visited:
            continue
        visited.add(u)
        for v in edges[u][t]:
            stack.append(v)
            
    return visited
    
    
def solution(n, infection, edges, k):
    answer = 0
    arr = [[[] for _ in range(4)] for __ in range(n+1)]
    for u, v, t in edges:
        arr[u][t].append(v)
        arr[v][t].append(u)
        
    return dfs(arr, k, {infection, })