p, m = map(int, input().split())

rooms = []
for _ in range(p):
    lv, name = input().split()
    for room in rooms:
        if len(room) < m and abs(room[0][0] - int(lv)) <= 10:
            room.append((int(lv), name))
            break
    else:
        room = [(int(lv), name)]
        rooms.append(room)

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    
    tmp = sorted(room, key=lambda x: x[1])
    for lv, name in tmp:
        print(lv, name)