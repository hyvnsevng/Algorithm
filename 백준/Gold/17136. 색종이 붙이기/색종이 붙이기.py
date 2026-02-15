graph = [list(map(int, input().split())) for _ in range(10)]


def backtrack(r, c, cnt, use, ans):
    if cnt > ans:
        return ans
    if r == 10:
        return cnt
    if c == 10:
        return backtrack(r+1, 0, cnt, use, ans)

    if graph[r][c] == 0:
        return backtrack(r, c+1, cnt, use, ans)
    
    max_size = get_max_size(r, c)
    for size in range(max_size, -1, -1):
        if use[size] == 0:
            continue
        flip(r, c, size+1, 0)
        use[size] -= 1
        res = backtrack(r, c+1, cnt+1, use, ans)
        if res > 0:
            ans = res
        use[size] += 1
        flip(r, c, size+1, 1)
    
    return ans if ans < 25 else -1


def get_max_size(r, c):
    for size in range(1, 5):    # 1, 2, 3, 4
        if r+size >= 10 or c+size >= 10:
            return size-1
        for diff in range(size+1):
            if graph[r+diff][c+size] == 0:
                return size-1
            if graph[r+size][c+diff] == 0:
                return size-1
    return 4
                

def flip(r, c, size, t):
    for dr in range(size):
        for dc in range(size):
            graph[r+dr][c+dc] = t


print(backtrack(0, 0, 0, [5]*5, 25))