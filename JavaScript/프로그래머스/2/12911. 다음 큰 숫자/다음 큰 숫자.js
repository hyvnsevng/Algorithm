function solution(n) {
    var answer = n+1;
    
    while (true) {
        if (answer.toString(2).split("1").length === n.toString(2).split("1").length) {
            return answer
        }
        answer += 1
    }   
}