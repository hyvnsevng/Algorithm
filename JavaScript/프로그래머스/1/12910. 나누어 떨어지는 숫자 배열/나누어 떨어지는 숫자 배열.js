function solution(arr, divisor) {
    var answer = [];
    arr.forEach((n) => {
        if (n % divisor === 0) {
            answer.push(n)
        }
    })
    console.log(answer)
    answer.sort((a, b) => a-b)
    // answer = answer.length === 0 ? answer : [-1]
    return answer.length !== 0 ? answer : [-1];
}