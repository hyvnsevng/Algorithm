function solution(n)
{
    var answer = 0;
    var num = n

    for (var i = 9; i > 0; i--) {
        var quotient = parseInt(num/((10)**i))
        answer += quotient
        
        console.log("몫: " + `${quotient} 그리고 ${num}`)
        num -= quotient
    }

    return answer;
}

console.log(solution(123))