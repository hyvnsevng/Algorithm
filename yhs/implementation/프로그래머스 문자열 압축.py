def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):      # 자르는 길이는 s 길이의 반 까지만 유효
        last_str = ''               # 자른 문자열
        repeated = 0                # 중복 횟수
        compressed = ''             # 압축된 문자열
        # print(f'cutting by {i} chars')
        for j in range(0, len(s)+i, i):     
            try:
                # 문자열 중복 시 중복 횟수 추가
                if last_str == s[j:j+i]:
                    repeated += 1
                    # print('repeated')

                # 지난 반복에서 자른 문자열 추가
                else:
                    if repeated:            
                        compressed += (str(repeated+1)+last_str)
                    else:
                        compressed += last_str
                    last_str = s[j:j+i]
                    repeated = 0
                
                # print(f'{j}th: {compressed}')
            except IndexError:
                if repeated:
                    compressed += (str(repeated)+last_str+s[j:])
                else:
                    compressed += s[j:]
        # print(f'compressed: {compressed}')
        
        # 최소길이 갱신
        if answer > len(compressed):
            answer = len(compressed)



    return answer

s = input()
print(solution(s))


