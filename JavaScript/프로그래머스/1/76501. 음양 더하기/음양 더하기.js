function solution(absolutes, signs) {
    var answer = 0
    for (var i = 0; i < signs.length; i++) {
        answer += signs[i] === true ? absolutes[i] : - absolutes[i]
    }
    return answer;
}