"""
생성한 정점 찾기: 전부 나가는 간선이면서 2개 이상
도넛: i=1 o=1
8자: 갑자기 i=2 o=2
직선: 그 외
"""

MAX = 1000000
visited = [False] * (MAX + 1)

def get_graph_type(arr, start):
    stack = [start]
    visited[start] = True
    while stack:
        v = stack.pop()
        
        candidates = arr[v]
        if len(candidates) >= 2:
            return 3    # 8자
        
        for nv in candidates:
            if visited[nv]:
                return 1
            stack.append(nv)
    
    return 2    # 막대
            

def solution(edges):
    answer = [0, 0, 0, 0]
    added = -1                          # 새로 추가된 정점
    indegree = [False] * (MAX + 1)      # 들어오는 간선이 있는지?
    arr = [[] for _ in range(MAX + 1)]  # 간선 인접리스트
    for s, e in edges:
        arr[s].append(e)
        indegree[e] = True
        if len(arr[s]) >= 2 and not indegree[s]:
            added = s
    
    answer[0] = added
    
    for v in arr[added]:
        graph_type = get_graph_type(arr, v)
        answer[graph_type] += 1
    
    return answer
