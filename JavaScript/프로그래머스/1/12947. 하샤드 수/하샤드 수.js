function solution(x) {
    var n = 0;
    x.toString().split("").forEach((e) => n += parseInt(e))
    return x % n === 0 ? true : false;
}