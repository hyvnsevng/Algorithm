import sys

sys.stdin = open('4865_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    max_count = 0

    for letter1 in str1:
        count = 0
        for letter2 in str2:
            if letter2 == letter1:
                count += 1

        if count > max_count:
            max_count = count

    print(f'#{tc} {max_count}')