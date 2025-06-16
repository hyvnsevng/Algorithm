n = int(input())
fruits = list(map(int, input().split()))

start, end = 0, 1
numFruit = 1
fruitNindex = [[fruits[0], fruits[0]], [0, -1]]  # 과일 종류, 해당 과일 마지막 인덱스

while end < n:
    # 과일 갱신하기
    if fruits[end] not in fruitNindex[0]:
        if fruitNindex[1][0] < fruitNindex[1][1]:
            fruitNindex[0][0] = fruits[end]
            start = fruitNindex[1][0] + 1
            fruitNindex[1][0] = end
        else:
            fruitNindex[0][1] = fruits[end]
            start = fruitNindex[1][1] + 1
            fruitNindex[1][1] = end
    # 과일 마지막 인덱스 갱신하기
    else:
        if fruits[end] == fruitNindex[0][0]:
            fruitNindex[1][0] = end
        else:
            fruitNindex[1][1] = end

    if end - start + 1 > numFruit:
        numFruit = end - start + 1
    end += 1

# print(fruitNindex)
print(numFruit)
