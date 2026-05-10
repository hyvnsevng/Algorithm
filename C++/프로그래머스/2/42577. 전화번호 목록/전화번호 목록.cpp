#include <string>
#include <vector>
#include <iostream>

using namespace std;

#define MAX_NODE 20000001
int trie[MAX_NODE][10];
bool has_more[MAX_NODE];
int node_cnt = 1;

void insert(string phone_num) {
    int curr = 0;
    for (int num : phone_num) {
        int idx = num - '0';
        
        if (trie[curr][idx] == 0) {
            trie[curr][idx] = node_cnt++;
            has_more[curr] = true;
        }
        curr = trie[curr][idx];
    }
}

bool find(string phone_num) {
    int curr = 0;
    for (int num : phone_num) {
        curr = trie[curr][num - '0'];
    }
    if (!has_more[curr]) return false;
    return true;
}

bool solution(vector<string> phone_book) {
    for (string phone_num : phone_book) {
        insert(phone_num);
    }
    
    for (auto phone_num: phone_book) {
        if (find(phone_num)) {
            return false;
        };
    }
    
    return true;
}