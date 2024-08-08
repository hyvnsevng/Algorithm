import sys

sys.stdin = open('4874_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    eq = input().split()    # 후위계산식 리스트로 받기
    stack = []

    for string in eq:
        # . 만나면 계산결과 출력
        if string == '.':
            # 스택에 숫자가 있으면
            if len(stack) == 1:
                num = stack.pop()
                if type(num) == int:
                    print(f'#{tc} {num}')
            # 아니면 오류
            else:
                print(f'#{tc} error')
            break
        # 숫자면 스택에 넣기
        elif string.isdigit():
            stack.append(string)
        # 사칙연산 및 그 외
        else:
            # 스택에 숫자가 2개 이상 있어야 함
            if len(stack)>1:
                num2 = stack.pop()
                num1 = stack.pop()
                if string == '+':
                    stack.append(int(num1) + int(num2))
                elif string == '-':
                    stack.append(int(num1) - int(num2))
                elif string == '*':
                    stack.append(int(num1) * int(num2))
                elif string == '/':
                    stack.append(int(num1) // int(num2))
                # 사칙연산 기호가 아닌 문자열일 경우 오류
                else:
                    print(f'#{tc} error')
                    break
            # 스택에 피연산자가 부족한 경우 오류 출력
            else:
                print(f'#{tc} error')
                break
