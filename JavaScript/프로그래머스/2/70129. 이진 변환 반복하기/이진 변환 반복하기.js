function solution(s) {
    var binC = 0;
    var delZ = 0;
    while (s !== "1") {
        var tmp = s.split("0").join("") // tmp: 0 제거
        delZ += s.length - tmp.length   // 제거된 0의 개수
        s = Number(tmp.length).toString(2)  // 2진수 변환
        binC += 1
        console.log(s)
    }
    return [binC, delZ];
}
