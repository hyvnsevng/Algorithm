import sys

sys.stdin = open('input.txt')

def find_path(data):
    stack = [1] # 스택에 시작지점 추가
    visited = [False for _ in range(len(data))]
    visited[1] = True
    result = ''

    # 모든 연결 노드 탐색
    while stack:
        v = stack.pop()     # v : 스택의 top 요소
        visited[v] = True   # 방문처리
        result += str(v)    # 결과 문자열에 v 추가
        # result(방문한 노드)의 길이가 n_v가 되면 반복  탈출
        if len(result) == n_v:
            break
        # v의 다음 노드 확인
        for i in data[v][::-1]:
            if not visited[i]:
                stack.append(i) # 다음 노드 큐에 넣기

    return result


def sort_arr(arr):
    len_arr = len(arr)
    for i in range(len_arr-1):
        for j in range(len_arr-1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# Testcase 수
T = 1
# Testcase 만큼 반복
for tc in range(1, T+1):
    n_v, n_e = map(int, input().split())

    edge = list(map(int, input().split()))  # 순서쌍

    data = [[] for _ in range(n_v+1)]         # (인덱스)번째 노드에서 갈 수 있는 노드
    for i in range(n_e):
        data[edge[2*i]].append(edge[2*i + 1])
        data[edge[2*i + 1]].append(edge[2*i])

    for i in data:
        i = sort_arr(i)

    print(f"#{tc}", end = ' ')
    print('-'.join(find_path(data)))