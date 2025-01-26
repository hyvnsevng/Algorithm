function solution(n) {
    var arr = [...n.toString()];
    for (var i = 0; i < arr.length; i++) {
        for (var j = 0; j < arr.length - i - 1; j++) {
            if (arr[j] < arr[j+1]) {
                var tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
            }
        }
    }
    var answer = parseInt(arr.join(""))
    return answer;
}