N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
B2 = B

idx_B = [x for x in range(len(B))]
# idx_B = B


for i in range(N):
    for j in range(N-i-1):
        if B2[j] > B2[j+1]:
            B2[j], B2[j+1] = B2[j+1], B2[j]
            idx_B[j], idx_B[j+1] = idx_B[j+1], idx_B[j]
            
A.sort()

ans = 0
for i in range(N):
    ans += A[i]*B[idx_B[i]]


print(ans)