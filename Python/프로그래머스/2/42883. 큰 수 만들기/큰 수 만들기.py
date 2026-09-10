def solution(number, k):
    stack = []
    for i in range(len(number)):
        num = number[i]
        # num보다 작은 수 지울 수 있을 때 까지 스택에서 제거
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 더 지워야 하면 남았으면 뒤에서 제거
    while k > 0:
        k -= 1
        stack.pop()
        
    return ''.join(stack)