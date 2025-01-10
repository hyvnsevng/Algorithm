function solution(s){
    var countP = s.toLowerCase().split('p').length
    var countY = s.toLowerCase().split('y').length
    if (countP === countY) {
        return true
    } else {
        return false
    }
}