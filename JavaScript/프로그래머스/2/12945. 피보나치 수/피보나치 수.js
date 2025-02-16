const fibonacci = [0, 1]
function solution(n) {
    for (var i = 2; i <= n; i++) {
        fibonacci.push((fibonacci[i-1] + fibonacci[i-2])%1234567)
    }
    
    return fibonacci[n]
}