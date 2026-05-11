#include <string>
#include <vector>

using namespace std;

bool check(int level, long long limit, int n, vector<int> &diffs, vector<int> &times) {
    long long time = 0;
    long long time_prev = 0;
    for (int i = 0; i < n; ++i) {
        int diff = diffs[i];
        int time_cur = times[i];
        if (i > 0) time_prev = times[i-1];
        if (diff <= level) time += time_cur;
        else time += (diff - level) * (time_cur + time_prev) + time_cur;
        if (time > limit) return false;
        time_prev += time_cur;
    }
    return true;
}

int solution(vector<int> diffs, vector<int> times, long long limit) {
    int n = diffs.size();
    int s = 1, e = 100000;
    int answer = 0;
    while (s <= e) {
        int mid = (s + e) / 2;
        if (check(mid, limit, n, diffs, times)) {
            answer = mid;
            e = mid - 1;
        }
        else s = mid + 1;
    }
    return answer;
}
