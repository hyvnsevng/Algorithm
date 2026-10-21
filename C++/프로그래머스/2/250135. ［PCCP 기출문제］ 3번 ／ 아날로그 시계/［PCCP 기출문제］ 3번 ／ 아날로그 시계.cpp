int convertToSec(int h, int m, int s) {
    return h * 3600 + m * 60 + s;
}

int countAlarm(int t) {
    return (t * 59 / 3600) + (t * 719 / 43200) - (t >= 12 * 3600 ? 2 : 1);
}

int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
    
    int st = convertToSec(h1, m1, s1);
    int et = convertToSec(h2, m2, s2);
    
    int cs = countAlarm(st);
    int ce = countAlarm(et);
    
    int answer = ce - cs;
    if (st * 59 % 3600 == 0 || st * 719 % 43200 == 0) {
        answer++;
    }
    
    return answer;
}