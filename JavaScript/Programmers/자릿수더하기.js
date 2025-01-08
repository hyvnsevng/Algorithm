function solution(n)
{
    var answer = 0;
    var num = n

    for (var i = 9; i >= 0; i--) {
        var quotient = Math.trunc(num/((10)**i))
        answer += quotient
        num -= quotient*(10**i)
    }

    return answer;
}

console.log(solution(123))
console.log(solution(987))
console.log(solution(0))
console.log(solution(123456789))
