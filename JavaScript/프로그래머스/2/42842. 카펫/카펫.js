function solution(brown, yellow) {
    var answer = [];
    for (var i = 1; i <= Math.sqrt(yellow); i++) {
        if (yellow % i === 0) {
            if ((yellow / i + i) * 2 + 4 === brown) {
                answer.push(Math.max(i + 2, yellow/i + 2))
                answer.push(Math.min(i + 2, yellow/i + 2))
                return answer
            }
        }
    }
}