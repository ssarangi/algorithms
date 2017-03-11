#include <iostream>
#include <vector>
#include <unordered_set>
#include <string>
#include <queue>
#include <utility>

using namespace std;

typedef pair<string, int> StringWithDistance;

int transform_strings(unordered_set<string>& dict, const string &s, const string &t) {
    queue<StringWithDistance> q;
    dict.erase(s);
    vector<string> path;
    path.push_back(s);
    
    q.emplace(make_pair(s, 0));
    
    while (!q.empty()) {
        string curr;
        int curr_dist = 0;
        tie(curr, curr_dist) = q.front();
        
        if (curr == t) {
            // Print all the paths
            for (auto s : path) {
                cout << s << endl;
            }
            return curr_dist;
        }
        
        // Try all possible transformations of the candidate string
        int curr_str_size = curr.size();
        for (int i = 0; i < curr_str_size; ++i) {
            string str = curr;
            for (int j = 0; j < 26; ++j) {
                str[i] = 'a' + j;
                if (dict.find(str) != dict.end()) {
                    dict.erase(str);
                    q.emplace(make_pair(str, curr_dist + 1));
                    path.push_back(str);
                }
            }
        }
        
        q.pop();
    }
    
    return -1;
}

int main() {
    unordered_set<string> dict = { "bat", "cot", "dog", "dag", "dot", "cat" };
    int distance = transform_strings(dict, "bat", "dot");
    if (distance < 0)
        cout << "No valid transformation found" << endl;
    else
        cout << "Distance: " << distance << endl;
}