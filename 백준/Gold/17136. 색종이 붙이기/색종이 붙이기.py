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
    
    for i in range(4, -1, -1):
        k = flip(r, c, i+1, use)
        if not k:
            continue
        use[i] -= 1
        res = backtrack(r, c+1, cnt+1, use, ans)
        if res > 0:
            ans = res
        use[i] += 1
        reflip(r, c, r+i+1, c+i+1, i+1)
    
    return ans if ans < 25 else -1


def flip(r, c, size, use):
    if use[size-1] == 0 or r+size > 10 or c+size > 10:
        return False
    for dr in range(size):
        for dc in range(size):
            if graph[r+dr][c+dc] == 0:
                reflip(r, c, r+dr, c+dc, size)
                return False
            graph[r+dr][c+dc] = 0
    return True


def reflip(r, c, lim_r, lim_c, size):
    for dr in range(size):
        for dc in range(size):
            if r+dr == lim_r and c+dc == lim_c:
                return
            graph[r+dr][c+dc] = 1


print(backtrack(0, 0, 0, [5]*5, 25))