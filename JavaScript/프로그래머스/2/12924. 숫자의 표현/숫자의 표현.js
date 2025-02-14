function solution(n) {
    var answer = 0;
    var sum = 1
    var arr = [1]
    while (arr[arr.length-1] <= n) {
        if (sum > n) {
            arr.shift()
        } else if (sum === n) {
            answer += 1
            arr.push(arr[arr.length-1] + 1)
        } else {
            arr.push(arr[arr.length-1] + 1)
        }
        sum = arr.reduce((a, b) => a+b)
    }
    return answer
}