answer = [[] for _ in range(7)]

def print_eqs(x):
    equations = answer[x-3]
    if not equations:
        find(x, "1", 1, 2, "1")
        answer[x-3].sort()
    for eq in equations:
        print(eq)
    print()


def find(x, eq, res, num, spaced):
    if num > x:
        if res == 0:
            answer[x-3].append(eq)
        return
    for i in range(3):
        n_res = res
        n_eq = eq
        n_spaced = str(num)
        if i == 0:
            n_res += num
            n_eq += ("+" + str(num))
        elif i == 1:
            n_res -= num
            n_eq += ("-" + str(num))
            n_spaced = "-" + n_spaced
        elif i == 2:
            n_spaced = spaced + str(num)
            n_res += (int(n_spaced) - int(spaced))
            n_eq += (" " + str(num))
        
        find(x, n_eq, n_res, num + 1, n_spaced)
    

T = int(input())
for _ in range(T):
    n = int(input())
    print_eqs(n)
