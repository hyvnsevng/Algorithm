function solution(n) {
    var answer = n.toString().split("").reverse()
    for (var i=0; i < answer.length; i++) {
        answer[i] = Number(answer[i])
    }
    return answer;
}