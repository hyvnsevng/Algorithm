n, m = map(int, input().split())        # n, m: 가로, 세로

cut_times = int(input())
cuts_ver = []
cuts_hor = []

for _ in range(cut_times):
    direction, where = map(int, input().split())
    if direction:       # 세로로 자르기 (가로)
        cuts_ver.append(where)
    else:               # 가로로 자르기 (세로)
        cuts_hor.append(where)

cuts_ver.sort()
cuts_hor.sort()

widest = [m, n]

if cuts_hor:
    widest[0] = cuts_hor[0]
if cuts_ver:
    widest[1] = cuts_ver[0]

for i in range(len(cuts_hor)):
    if i == len(cuts_hor) - 1:
        space = m - cuts_hor[i]
    else:
        space = cuts_hor[i+1] - cuts_hor[i]

    if space > widest[0]:
        widest[0] = space

for i in range(len(cuts_ver)):
    if i == len(cuts_ver) - 1:
        space = n - cuts_ver[i]
    else:
        space = cuts_ver[i + 1] - cuts_ver[i]

    if space > widest[1]:
        widest[1] = space

print(widest[0]*widest[1])


