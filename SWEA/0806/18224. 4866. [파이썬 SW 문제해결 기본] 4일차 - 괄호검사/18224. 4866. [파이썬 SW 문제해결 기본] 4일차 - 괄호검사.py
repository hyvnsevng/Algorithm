import sys

sys.stdin = open('4866_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    string = input()

    brackets_left = ['{', '(']
    brackets_right = {'}':'{', ')':'('}
    stack = []
    for char in string:
        if char in brackets_left:
            stack.append(char)
        elif char in brackets_right:
            bracket = stack.pop()
            if brackets_right[char] != bracket:
                print(f'#{tc} 0')
                break
    else:
        print(f'#{tc} 1')



    # # print(string)
    # mid = ['{', '}']
    # small = ['(', ')']
    #
    # mid_cnt1 = 0
    # mid_cnt2 = 0
    #
    # small_cnt1 = 0
    # small_cnt2 = 0
    #
    # for char in string:
    #     if char == mid[0]:
    #         mid_cnt1 += 1
    #     elif char == mid[1]:
    #         mid_cnt2 += 1
    #     elif char == small[0]:
    #         small_cnt1 += 1
    #     elif char == small[1]:
    #         small_cnt2 += 1
    #
    #     if mid_cnt2 > mid_cnt1 or small_cnt2 > small_cnt1:
    #         print(f'#{tc} 0')
    #         break
    # else:
    #     if mid_cnt1 == mid_cnt2 and small_cnt1 == small_cnt2:
    #         print(f'#{tc} 1')
    #     else:
    #         print(f'#{tc} 0')