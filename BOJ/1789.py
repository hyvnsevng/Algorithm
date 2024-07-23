N = int(input())

integer = 0
sum_val = 0

while True:
    integer += 1
    sum_val += integer
    if N < sum_val:
        break
    

print(integer-1)