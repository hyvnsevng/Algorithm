# 백준 5430번 AC

# 1. 입력받은 배열 형식의 문자열을 어떻게 처리할 것인가? -> strip과 split 메서드를 이용해 배열로 형변환
# 2. R과 D 연산을 어떻게 처리할 것인가?
# 2-1. R 연산: bool 변수(reverse)를 통해 배열이 뒤집힌 상태인지 나타냄. 배열 자체를 뒤집지는 않는다.
# 2-2. D 연산: reverse에 따라 앞의 수를 버릴 것인지 뒤의 수를 버릴 것인지 판단. 실제 배열의 요소를 제거하지 않고 인덱싱을 통해 연산 처리한다.
# 3. 답 출력하기 : 인덱스 슬라이싱 통해 정답 배열 구하기. 이후 배열 -> 문자열로 형변환.

T = int(input())
for tc in range(T):
    p = input()  # 수행할 함수
    n = int(input())    # 배열에 들어있는 수의 개수 (0 <= n <= 100,000)
    arr = list(input().strip('[]').split(','))  # 배열 ('[x1,...,xn]'과 같은 문자열로 주어지므로 strip과 split 메서드를 이용해 배열로 형변환)

    ans = ''    # 출력할 정답 초기화
    reverse = False     # R 연산의 결과로 배열이 뒤집힌 상태인지 bool로 저장하기
    start, end = 0, n   # D 연산의 결과로 수를 얼마나 버렸는지 확인. 정답 출력 시 인덱스 슬라이싱을 위해 설정함.

    for char in p:  # 함수 p의 각 연산에 대해
        # R: reverse 토글
        if char == 'R':
            reverse = False if reverse else True
        # D: start == end일 때(모든 수를 버려 빈 배열인 상태에서 D 연산을 해야한다?) => error
        elif char == 'D':
            if start >= end:
                ans = 'error'
                break
            # reverse 여부에 따라 앞 또는 뒤의 수를 버릴지 결정
            if reverse:
                end -= 1
            else:
                start += 1
    # error 발생하지 않고 모든 반복을 끝냈다면 인덱스 슬라이싱을 통해 연산 결과 배열을 구하고, 다시 문자열로 변환
    else:
        newArr = arr[start:end]
        if reverse:
            ans = '['+','.join(newArr[::-1])+']'
        else:
            ans = '['+','.join(newArr)+']'

    print(ans)
