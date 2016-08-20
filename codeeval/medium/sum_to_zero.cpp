#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>

using namespace std;

int num_ways_4_elements_sum_to_zero(vector<int>& arr) {
    int total_ways = 0;
    set<int> arr_elms;
    
    for (auto num : arr)
        arr_elms.insert(num);

    int arr_size = arr.size();
    for (int i = 0; i < arr_size; ++i) {
        for (int j = i+1; j < arr_size; ++j) {
            for (int k = j+1; k < arr_size; ++k) {
                for (int l = k+1; l < arr_size; ++l) {
                    if (arr[i] + arr[j] + arr[k] + arr[l] == 0) {
                        ++total_ways;
                    }
                }
            }
        }
    }
    
    return total_ways;
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    while (getline(stream, line)) {
        string s = "";
        vector<int> arr;
        for (auto c : line) {
            if (c == ',') {
                int num = stoi(s);
                arr.push_back(num);
                s = "";
            } else {
                s += c;
            }
        }
        
        arr.push_back(stoi(s));
        int num_ways = num_ways_4_elements_sum_to_zero(arr);
        cout << num_ways << endl;
    }
    return 0;
}