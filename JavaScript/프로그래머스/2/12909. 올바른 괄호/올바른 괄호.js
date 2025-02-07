function solution(s){
    var answer = true
    var stack = []
    s.split("").forEach((e) => {
        if (e === ")") {
            if (stack.length === 0) {
                answer = false
            }
            stack.pop()
        } else {
            stack.push("(")
        }
    })
    return stack.length === 0 && answer ? answer : false;
}