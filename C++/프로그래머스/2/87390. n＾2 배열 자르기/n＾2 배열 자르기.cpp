#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, long long left, long long right) {
    vector<int> answer(right - left + 1);
    for (int i = 0; i <= right - left; i++) {
        long loc = i + left;
        answer[i] = (max(loc / n, loc % n) + 1);
    }
    return answer;
}