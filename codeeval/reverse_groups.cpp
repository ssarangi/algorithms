#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>

using namespace std;

void reverse(vector<int>& arr, int start, int k) {
    if (arr.size() == 0)
        return;
        
    int p1 = start, p2 = start + k - 1;
    
    if (p1 >= arr.size())
        return;
        
    if (p2 >= arr.size())
        return;
    
    while (p1 < p2) {
        int tmp = arr[p1];
        arr[p1] = arr[p2];
        arr[p2] = tmp;
        ++p1;
        --p2;
    }
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    while (getline(stream, line)) {
        string s;
        vector<int> arr;
        for (auto c : line) {
            if (c == ',' || c == ';') {
                int num = stoi(s);
                arr.push_back(num);
                s = "";
            } else {
                s += c;
            }
        }
        
        int k = stoi(s);
        
        // So we have the array and k
        int arr_size = arr.size();
        for (int i = 0; i < arr_size; i += k) {
            reverse(arr, i, k);
        }
        
        for (int i = 0; i < arr_size; ++i)
            if (i != arr_size - 1)
                cout << arr[i] << ",";
            else
                cout << arr[i];
        cout << endl;
    }
    
    return 0;
}