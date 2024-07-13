for test_case in range(1, 11):
    dump_count = int(input())
    wall = list(map(int, input().split()))

    for count in range(dump_count):
        wall.sort()
        wall[-1] = wall[-1] - 1
        wall[0] = wall[0] + 1
    wall.sort()
    answer = wall[-1]-wall[0]


    print(f"#{test_case} {answer}")
