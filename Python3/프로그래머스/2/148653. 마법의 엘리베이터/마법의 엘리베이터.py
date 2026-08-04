def solution(storey):
    if storey < 10:
        return min(storey, 10 - storey + 1)
    div, remainder = storey // 10, storey % 10
    return min(solution(div) + remainder, solution(div + 1) + 10 - remainder)