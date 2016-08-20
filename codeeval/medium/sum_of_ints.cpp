// https://www.codeeval.com/open_challenges/17/

#include <iostream>
#include <fstream>
#include <algorithm>
#include <limits>

using namespace std;

int sum_of_integers(vector<int>& elems) {
    vector<int> dp(elems.size());
    int arr_size = elems.size();
    
    int max_sum = numeric_limits<int>::min();
    
    for (int i = 0; i < arr_size; ++i) {
        dp[i] = max(elems[i], dp[i-1] + elems[i]);
        max_sum = max(max_sum, dp[i]);
    }
    
    return max_sum;
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    while (getline(stream, line)) {
        vector<int> elems;
        int i = 0;
        string digits = "";
        while (i < line.size()) {
            if (line[i] == ',') {
                elems.push_back(stoi(digits));
                digits = "";
            } else {
                digits += line[i];
            }
            
            ++i;
        }
        
        elems.push_back(stoi(digits));
        int max_sum = sum_of_integers(elems);
        cout << max_sum << endl;
    }
    
    return 0;
}