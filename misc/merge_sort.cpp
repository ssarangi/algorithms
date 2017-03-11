#include <vector>
#include <iostream>
#include <iterator>

using namespace std;

vector<int> merge(vector<int>& arr1, vector<int>& arr2) {
    int p1 = 0, p2 = 0;
    vector<int> result;
    
    while (p1 != arr1.size() && p2 != arr2.size()) {
        if (arr1[p1] < arr2[p2]) {
            result.push_back(arr1[p1]);
            ++p1;
        }
        else {
            result.push_back(arr2[p2]);
            ++p2;
        }
    }
    
    // Add the remaining items
    for (int i = p1; i < arr1.size(); ++i)
        result.push_back(arr1[i]);
        
    for (int i = p2; i < arr2.size(); ++i)
        result.push_back(arr2[i]);
        
    return result;
}

vector<int> merge_sort(vector<int>& arr, int start, int end) {
    if (start >= end) {
        vector<int> a = { arr[start] };
        return a;
    }

    int center = (start + end) / 2;
    vector<int> a1 = merge_sort(arr, start, center);
    vector<int> a2 = merge_sort(arr, center + 1, end);
    
    vector<int> result = merge(a1, a2);
    return result;
}

int main() {
    vector<int> arr = { 5, 8, 2, 1, 0, 7, 3, 11, 9 };
    vector<int> sorted_arr = merge_sort(arr, 0, arr.size() - 1);
    
    copy(sorted_arr.begin(), sorted_arr.end(), ostream_iterator<int>(cout, " "));
    cout << endl;
}