import sys

input = sys.stdin.readline
colors = 'wyrogb'
idxmap = {'U': 0, 'D': 1, 'F': 2, 'B': 3, 'L': 4, 'R': 5}

def solve(actions):
    cube = [[[colors[_] for r in range(3)] for c in range(3)] for _ in range(6)]
    for action in actions:
        rotate(action[0], action[1], cube)
    for line in cube[0]:
        print("".join(line))

def rotate(P, direction, cube):
    U, D, F, B, L, R = idxmap["U"], idxmap["D"], idxmap["F"], idxmap["B"], idxmap["L"], idxmap["R"]
    if direction == '+':
        flip(cube[idxmap[P]])
    transpose(cube[idxmap[P]])
    if direction == '-':
        flip(cube[idxmap[P]])

    if P == 'U':
        tmp = cube[F][0][:]
        if direction == '+':
            for i in range(3): cube[F][0][i] = cube[R][0][i]
            for i in range(3): cube[R][0][i] = cube[B][0][i]
            for i in range(3): cube[B][0][i] = cube[L][0][i]
            for i in range(3): cube[L][0][i] = tmp[i]
        elif direction == '-':
            for i in range(3): cube[F][0][i] = cube[L][0][i]
            for i in range(3): cube[L][0][i] = cube[B][0][i]
            for i in range(3): cube[B][0][i] = cube[R][0][i]
            for i in range(3): cube[R][0][i] = tmp[i]

    elif P == 'D':
        tmp = cube[F][2][:]
        if direction == '+':
            for i in range(3): cube[F][2][i] = cube[L][2][i]
            for i in range(3): cube[L][2][i] = cube[B][2][i]
            for i in range(3): cube[B][2][i] = cube[R][2][i]
            for i in range(3): cube[R][2][i] = tmp[i]
        elif direction == '-':
            for i in range(3): cube[F][2][i] = cube[R][2][i]
            for i in range(3): cube[R][2][i] = cube[B][2][i]
            for i in range(3): cube[B][2][i] = cube[L][2][i]
            for i in range(3): cube[L][2][i] = tmp[i]

    elif P == 'L':
        tmp = [cube[B][r][2] for r in range(2, -1, -1)]
        if direction == '+':
            for i in range(3): cube[B][2-i][2] = cube[D][i][0]
            for i in range(3): cube[D][i][0] = cube[F][i][0]
            for i in range(3): cube[F][i][0] = cube[U][i][0]
            for i in range(3): cube[U][i][0] = tmp[i]
        elif direction == '-':
            for i in range(3): cube[B][2-i][2] = cube[U][i][0]
            for i in range(3): cube[U][i][0] = cube[F][i][0]
            for i in range(3): cube[F][i][0] = cube[D][i][0]
            for i in range(3): cube[D][i][0] = tmp[i]

    elif P == 'R':
        tmp = [cube[B][r][0] for r in range(2, -1, -1)]
        if direction == '+':
            for i in range(3): cube[B][2-i][0] = cube[U][i][2]
            for i in range(3): cube[U][i][2] = cube[F][i][2]
            for i in range(3): cube[F][i][2] = cube[D][i][2]
            for i in range(3): cube[D][i][2] = tmp[i]
        elif direction == '-':
            for i in range(3): cube[B][2-i][0] = cube[D][i][2]
            for i in range(3): cube[D][i][2] = cube[F][i][2]
            for i in range(3): cube[F][i][2] = cube[U][i][2]
            for i in range(3): cube[U][i][2] = tmp[i]

    elif P == 'F':
        if direction == '+':
            tmp = [cube[L][r][2] for r in range(2, -1, -1)]
            for i in range(3): cube[L][i][2] = cube[D][0][i]
            for i in range(3): cube[D][0][i] = cube[R][2-i][0]
            for i in range(3): cube[R][i][0] = cube[U][2][i]
            for i in range(3): cube[U][2][i] = tmp[i]
        elif direction == '-':
            tmp = cube[D][0][::-1]
            for i in range(3): cube[D][0][i] = cube[L][i][2]
            for i in range(3): cube[L][i][2] = cube[U][2][2-i]
            for i in range(3): cube[U][2][i] = cube[R][i][0]
            for i in range(3): cube[R][i][0] = tmp[i]

    elif P == 'B':
        if direction == '+':
            tmp = cube[D][2][::-1]
            for i in range(3): cube[D][2][i] = cube[L][i][0]
            for i in range(3): cube[L][i][0] = cube[U][0][2-i]
            for i in range(3): cube[U][0][i] = cube[R][i][2]
            for i in range(3): cube[R][i][2] = tmp[i]
        elif direction == '-':
            tmp = [cube[L][r][0] for r in range(2, -1, -1)]
            for i in range(3): cube[L][i][0] = cube[D][2][i]
            for i in range(3): cube[D][2][i] = cube[R][2-i][2]
            for i in range(3): cube[R][i][2] = cube[U][0][i]
            for i in range(3): cube[U][0][i] = tmp[i]


def transpose(plane):
    for r in range(2):
        for c in range(r+1, 3):
            plane[r][c], plane[c][r] = plane[c][r], plane[r][c]


def flip(plane):
    plane[0], plane[2] = plane[2], plane[0]


T = int(input())
for tc in range(T):
    n = int(input())
    actions = input().split(" ")
    solve(actions)
