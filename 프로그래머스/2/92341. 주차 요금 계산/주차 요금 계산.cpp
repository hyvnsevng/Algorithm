#include <string>
#include <vector>
#include <map>

using namespace std;

int toMinute(int hour, int minute) {
    return hour * 60  + minute;
}

int calcFee(vector<int> fees, int minute) {
    int b_time = fees[0];
    int b_fee = fees[1];
    int u_time = fees[2];
    int u_fee = fees[3];
    if (minute <= b_time) return b_fee;
    return b_fee + ((minute - b_time + u_time - 1) / u_time) * u_fee;
}

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    map<string, int> inTime;
    map<string, int> totalTime;
    for (auto record : records) {
        int hour = stoi(record.substr(0, 2));
        int minute = stoi(record.substr(3, 2));
        string number = record.substr(6, 4);
        string status = record.substr(11);
        
        int currentTime = toMinute(hour, minute);        
        int lastInTime = inTime[number];
        
        if (status == "IN") {
            inTime[number] = currentTime;
        }
        if (status == "OUT") {
            totalTime[number] += currentTime - lastInTime;
            inTime.erase(number);
        }             
    }
    
    int endTime = toMinute(23, 59);
    for (auto enter: inTime) {
        totalTime[enter.first] += endTime - enter.second;
    }
    
    for (auto io: totalTime) {
        int time = io.second;
        answer.push_back(calcFee(fees, time));
    }
    
    return answer;
    
}