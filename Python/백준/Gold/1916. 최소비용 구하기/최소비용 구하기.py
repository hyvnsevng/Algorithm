import sys
from heapq import heappop, heappush


def dijkstra(s, e, edges):
    distances = [10e9 for _ in range(len(edges))]
    hq = [(0, s)]
    while hq:
        cost, curr = heappop(hq)

        for w, _next in edges[curr]:
            if distances[_next] > cost + w:
                heappush(hq, (cost + w, _next))
                distances[_next] = cost + w
    
    return distances[e]


def main():
    input = sys.stdin.readline

    n = int(input())
    m = int(input())

    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges[a].append((c, b))
    
    for node in range(n+1):
        edges[node].sort()
        
    A, B = map(int, input().split())
    print(dijkstra(A, B, edges))
    return


main()
