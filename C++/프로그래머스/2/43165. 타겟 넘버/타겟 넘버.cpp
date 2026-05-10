#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    
    int n = numbers.size();
    
    for (int mask = 0; mask < 1 << n; mask++) {
        int tmp = 0;
        for (int i=0; i < n; i++) {
            if (mask & (1 << i)) tmp += numbers[i];
            else tmp -= numbers[i];
        }
        if (target == tmp) answer++;
    }
    
    return answer;
}