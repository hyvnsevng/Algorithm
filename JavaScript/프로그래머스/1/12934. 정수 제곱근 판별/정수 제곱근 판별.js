function solution(n) {
    var answer = 0;
    for (var i = 1; i <= Math.sqrt(50000000000000) + 1; i++) {
        if (i**2 === n) {
            return (i+1)**2
        } 
        if (i**2 > n) {
            return -1
        }
    }
    // return answer;
}