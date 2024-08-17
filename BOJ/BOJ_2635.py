n = int(input())

max_len = 0
answer = []

# # 재귀함수 이용한 풀이
# def func(num1, num2, num_list):
#     if num2 < 0:
#         return num_list
#
#     num_list.append(num2)
#
#     lst = func(num2, num1-num2, num_list)
#
#     return lst
#
#
# for i in range(1, n):
#     result = func(n, i, [n])
#     if len(result) > max_len:
#         max_len = len(result)
#         answer = result
#
# print(max_len)
# print(*answer)

for i in range(1, n+1):
    lst = [n, i]
    while True:
        num = lst[-2] - lst[-1]
        if num < 0:
            break
        lst.append(num)
    length = len(lst)
    if length > max_len:
        max_len = length
        answer = lst

print(max_len)
print(*answer)
