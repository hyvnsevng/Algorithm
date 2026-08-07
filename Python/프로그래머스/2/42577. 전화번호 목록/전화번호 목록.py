def solution(phone_book):
    root = dict()
    for phone_num in phone_book:
        node = root
        for num in phone_num:
            _next = node.get(num, None)
            if _next:
                node = _next
            else:
                node[num] = dict()
                node = node[num]
        else:
            node["-1"] = True
    
    for phone_num in phone_book:
        node = root
        for num in phone_num:
            if node.get("-1", False):
                return False
            node = node[num]
            
    return True