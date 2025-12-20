a, b, c = map(int, input().split())
st = [-1] * 32
st[0] = a % c
for i in range(1, 32):
    st[i] = (st[i-1] * st[i-1]) % c

ans = 1

for j in range(32):
    if b & 1 << j:
        ans *= st[j]
    
print(ans % c)
