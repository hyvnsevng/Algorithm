#include <string>
#include <vector>

using namespace std;

bool check_limit(vector<int> &diffs, vector<int> &times, int &n, long long &limit, int level) {
    long long total_time = 0;
    int time_prev = 0;
    for (int i = 0; i < n; i++) {
        int diff = diffs[i];
        int time_cur = times[i];
        if (i > 0) time_prev = times[i-1];
        
        if (diff > level) total_time += (diff - level) * (time_cur + time_prev) + time_cur;
        else total_time += time_cur;
        
   }
    if (total_time > limit) return false;
    return true;
}

int solution(vector<int> diffs, vector<int> times, long long limit) {
    int answer = 0;
    int n = diffs.size();
    int s = 1, e = 100000;
    while (s <= e) {
        int mid = (s + e) / 2;
        if (check_limit(diffs, times, n, limit, mid)) {
            answer = mid;
            e = mid - 1;
        }
        else {
            s = mid + 1;
        }
    }
    return answer;
}
