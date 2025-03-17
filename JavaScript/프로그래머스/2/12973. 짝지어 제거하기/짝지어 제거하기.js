function solution(s)
{
    if (s.length % 2 === 1) {
        return 0
    }
    
    var arr = s.split("")
    var stack = []
    for (var i = 0; i < s.length; i++) {
        if (arr.length === 0) {
            arr.push(arr[i])
        } else {
            if (stack[stack.length - 1] === arr[i]) {
                stack.pop()
            } else {
                stack.push(arr[i])
            }
        }
    }
    
    return stack.length === 0 ? 1 : 0
        
}