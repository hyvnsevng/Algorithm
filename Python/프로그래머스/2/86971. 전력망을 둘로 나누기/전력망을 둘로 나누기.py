answer = 100

def dfs(n, edges, ans, curr = 1, prev = 0):
    global answer
    sum_children = 1
    for node in edges[curr]:
        if node == prev:
            continue
        res = dfs(n, edges, ans, node, curr)  # 자식 노드부터의 송전탑 개수 합
        sum_children += res
    
    answer = min(answer, abs(n - sum_children - sum_children))
    return sum_children
    
    
def solution(n, wires):
    edges = [list() for _ in range(n + 1)]
    for a, b in wires:
        edges[a].append(b)
        edges[b].append(a)
    dfs(n, edges, n)
    return answer