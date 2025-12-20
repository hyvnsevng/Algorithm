a, b, c = map(int, input().split())
rem = a % c
ans = 1
bit = 1
while bit <= b:
    if b & bit:
        ans = (ans * rem) % c
    rem = (rem * rem) % c
    bit = bit << 1
print(ans % c)
