function solution(num) {
    var answer = 0;
    while (answer <= 500) {
        if (num === 1) return answer
        if (num % 2 === 0) {
            num /= 2
        } else {
            num = num * 3 + 1
        }
        answer += 1
    }
    answer = -1
    return answer;
}