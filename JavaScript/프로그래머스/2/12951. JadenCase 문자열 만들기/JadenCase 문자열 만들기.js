function solution(s) {
    var answer = '';
    s.split(" ").forEach((word) => {
        answer += word.slice(0, 1).toUpperCase() + word.slice(1).toLowerCase() + " "
    })
    return answer.slice(0, answer.length - 1);
}