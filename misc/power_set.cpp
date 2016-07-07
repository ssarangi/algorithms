// Generate powersets from a given set

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

void generate_set_for_size(
                           const vector<char>& origset,
                           const int size,
                           vector<char>& curr_set,
                           vector<vector<char>>& final_set,
                           int next_el_idx) {
    
    // Check if we have reached our max size
    if (curr_set.size() == size) {
        final_set.push_back(curr_set);
        return;
    }
    
    // Iterate over all the set elements and see which ones have been used.
    int original_set_size = (int)origset.size();
    for (int i = next_el_idx; i < original_set_size; ++i) {
            curr_set.push_back(origset[i]);
            generate_set_for_size(origset, size, curr_set, final_set, i + 1);
            curr_set.pop_back();
    }
}

vector<vector<vector<char>>> generate_power_set(vector<char>& origset) {
    vector<vector<vector<char>>> powerset;
    
    int set_size = (int)origset.size();
    for (int i = 0; i <= set_size; ++i) {
        // Generate set's of all sizes
        vector<char> currset;
        vector<vector<char>> final_set;
        generate_set_for_size(origset, i, currset, final_set, 0);
        powerset.push_back(final_set);
    }
    
    return powerset;
}

int main() {
    vector<char> origset = {'a', 'b', 'c', 'd'};
    auto powerset = generate_power_set(origset);
    
    for (auto set_per_size : powerset) {
        for (auto elem_set : set_per_size) {
            copy(elem_set.begin(), elem_set.end(), ostream_iterator<char>(cout, " "));
            cout << endl;
        }
    }
}