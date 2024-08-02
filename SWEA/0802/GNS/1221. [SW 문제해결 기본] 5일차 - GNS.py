import sys

sys.stdin = open('GNS_test_input.txt')

def fucn(lst):
    for i in range(len(lst)):
        for j in range(10):
            if lst[i] == num_in_alpha[j]:
                lst[i] = j

    for i in range(len(lst)-1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


# Testcase 수
T = int(input())
# Testcase 만큼 반복

for _ in range(1, T+1):
    tc, n = input().split()

    num_in_alpha = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    print(tc)

    nums = input().split()
    num_list = fucn(nums)

    for num in num_list:
        print(num_in_alpha[num], end=' ')
    print()



