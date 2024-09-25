# 백준 18870번 좌표 압축

n = int(input())
lst = list(map(int, input().split()))   # 처음 입력받는 좌표 배열
lst_ = [[] for _ in range(n)]           # 정렬할 좌표 배열
for i in range(n):
    lst_[i] = [lst[i], i]               # 원본 배열에서의 index와 함께 저장한다.

lst_.sort()                             # 정렬
ans = [0 for _ in range(n)]             # 압축된 좌표 배열

lst = list(set(lst))                    # 중복되는 좌표 제거하기 위해 list -> set -> list로 변환 후 정렬
lst.sort()

comp = 0                                # 압축된 좌표
# 좌표 압축
for num, idx in lst_:
    if num == lst[comp]:
        ans[idx] = comp
    else:
        comp += 1
        ans[idx] = comp

print(*ans)
