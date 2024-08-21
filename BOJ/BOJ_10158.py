# 10158번 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# if w - p <= t:
#     p += t
# else:
#     dis = t % w
#     if

t_hor = t - (w-p)
if t_hor < 0:
    p += t
else:
    right = int(t_hor / w % 2)
    if right:  # 홀수면 오른쪽
        p = t_hor % w
    else:
        p = w - t_hor % w

t_ver = t - (h-q)
if t_ver < 0:
    q += t
else:
    up = int(t_ver / h % 2)
    if up:
        q = t_ver % h
    else:
        q = h - t_ver % h
print(p, q)