function solution(n) {
    for (var i = 2; i < n; i++) {
        if ((n-1) % i === 0) {
            return i
        }
    }
    
}