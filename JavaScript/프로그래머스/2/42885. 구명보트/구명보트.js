function solution(people, limit) {
    var answer = people.length;
    
    people.sort((a, b) => a-b)
    var start = 0
    var end = people.length - 1
    
    while (start < end) {
        if (people[end] + people[start] <= limit) {
            answer -= 1
            start += 1
        }
        end -= 1
    }
    return answer;
}