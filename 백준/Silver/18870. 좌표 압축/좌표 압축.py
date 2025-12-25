n = int(input())
lst = list(map(int, input().split()))
lst_ = [[] for _ in range(n)]
for i in range(n):
    lst_[i] = [lst[i], i]

lst_.sort()
ans = [0 for _ in range(n)]
lst = list(set(lst))
lst.sort()
comp = 0
for num, idx in lst_:
    if num == lst[comp]:
        ans[idx] = comp
    else:
        comp += 1
        ans[idx] = comp

print(*ans)