function solution(phone_number) {
    const len = phone_number.length
    var answer = "*".repeat(len-4) + phone_number.substr(len-4, len);
    return answer;
}