# 프로그래머스 가사 검색

def solution(words, queries):
    answer = []

    head, head_rev = {}, {}
    len_words = []

    for word in words:
        add(head, word)
        add(head_rev, word[::-1])
        len_words.append(len(word))

    answer = []

    for query in queries:
        if query[0] == '?':
            if query[-1] == '?':
                count = len_words.count(len(query))
            else:
                count = find(query[::-1], head_rev)
        else:
            count = find(query, head)

        answer.append(count)

    return answer


def add(head, word):
    node = head

    for letter in word:
        if letter not in node:
            node[letter] = {}
        node = node[letter]

        if 'len' not in node:
            node['len'] = [len(word)]
        else:
            node['len'].append(len(word))

    node['end'] = True


def find(query, head):
    node = head
    length = len(query)
    for i in range(length):
        if query[i] == '?':
            return node['len'].count(length)

        if query[i] in node:
            node = node[query[i]]
        else:
            return 0


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))