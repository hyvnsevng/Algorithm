text = input()
bomb = input()
bomb_len = len(bomb)

while (1):
    i = text.find(bomb)
    if i < 0:
        break
    start, end = i, i + bomb_len
    while 1:
        tmp = text[start-bomb_len:start] + text[end:end+bomb_len]
        idx = tmp.find(bomb)
        if idx > 0:
            start = start - bomb_len + idx
            end = end + idx
        else:break
    text = text[:start] + text[end:]
    
print(text if text else "FRULA")
