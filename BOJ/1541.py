equation = input().split('-')

sum_val = 0
for i in range(len(equation)):
    numbers = map(int, equation[i].split('+'))
    if i==0:
        sum_val += sum(numbers)
    else:
        sum_val -= sum(numbers)
    
print(sum_val)