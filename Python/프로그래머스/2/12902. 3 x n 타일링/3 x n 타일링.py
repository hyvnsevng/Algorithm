def solution(n):
    answer = 0
    div = 1000000007
    
    ends_with_vertical = [0] * (n // 2)
    ends_with_horizontal = [0] * (n // 2)
    ends_with_vertical[0] = 2
    ends_with_horizontal[0] = 1
    for i in range(1, n // 2):
        ends_with_vertical[i] = (3 * ends_with_vertical[i - 1] + 2 * ends_with_horizontal[i - 1]) % div
        ends_with_horizontal[i] = ends_with_vertical[i - 1] + ends_with_horizontal[i - 1] % div
        
    answer = (ends_with_vertical[-1] + ends_with_horizontal[-1]) % div
    return answer