#include <iostream>
#include <vector>

using namespace std;

bool possible_to_reach_end(vector<int>& arr) {
    int lastidx = arr.size() - 1;
    int furthest_reached_so_far = 0;
    
    for (int i = 0; i <= furthest_reached_so_far && furthest_reached_so_far <= lastidx; ++i) {
        furthest_reached_so_far = max(furthest_reached_so_far, arr[i] + i);
    }
    
    return furthest_reached_so_far >= lastidx;
}

int main() {
    // vector<int> vals = { 3, 3, 1, 0, 2, 0, 1 };
    vector<int> vals = { 2, 3, 0, 0, 0, 1 }; 
    std::cout << possible_to_reach_end(vals) << std::endl;
    return 0;
}