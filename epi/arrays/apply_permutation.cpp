#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void apply_permutation(vector<int>& perm, vector<int>& A) {
    for (int i = 0; i < A.size(); ++i) {
        int next = i;
        
        while (perm[next] >= 0) {
            swap(A[i], A[perm[next]]);
            int temp = perm[next];
            
            // subtracts the perm size from an entry in perm to make it negative.
            // which indicates the corresponding move has been performed.
            perm[next] -= perm.size();
            next = temp;
        }
    }
    
    // Restore perm
    for_each(perm.begin(), perm.end(), [&](int& x) { x += perm.size(); });
}

void CyclicPermutation(int start, const vector<int>& perm, vector<int>& A) {
    int i = start;
    int temp = A[start];
    do {
        int next_i = perm[i];
        int next_temp = A[next_i];
        
        A[next_i] = temp;
        i = next_i, temp = next_temp;
    } while (i != start);
}

void apply_permutation_1(const vector<int>& perm, vector<int>& A) {
    for (int i = 0; i <= A.size(); ++i) {
        bool is_min = true;
        
        int j = perm[i];
        while (j != i) {
            if (j < i) {
                is_min = false;
                break;
            }
            
            j = perm[j];
        }
        
        if (is_min)
            CyclicPermutation(i, perm, A);
    }
}


int main() {
    vector<int> perm_ptr = { 3, 1, 2, 0 };
    vector<int> A = { 5, 6, 7, 8 };
    
    apply_permutation_1(perm_ptr, A);
    for (auto el : A)
        cout << el << endl;
    return 0;
}