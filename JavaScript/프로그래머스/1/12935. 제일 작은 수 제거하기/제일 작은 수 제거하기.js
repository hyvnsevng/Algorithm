function solution(arr) {
    
    if (arr.length === 1) {
        return [-1]
    } else {    
        const minNum = Math.min(...arr)
        var answer = arr.filter((e) => e!==minNum)
        return answer
    }
}
// | [1, 2, 3, 4] | [2, 3, 4] | [4, 3, 2] |