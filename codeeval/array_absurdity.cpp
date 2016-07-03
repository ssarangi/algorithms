// https://www.codeeval.com/open_challenges/41/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int missing_element(vector<int>& elems) {
    int ideal_sum = 0;
    int actual_sum = 0;
    
    int arr_size = elems.size();
    for (int i = 0; i < arr_size; ++i) {
        ideal_sum += i;
        actual_sum += elems[i];
    }
    
    int diff = ideal_sum - actual_sum;
    int N = arr_size - 1;
    
    // So repeated number is 
    int repeated = N - diff;
    return repeated;
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    while (getline(stream, line)) {
        string s_arr_size = "";
        int i = 0;
        while (line[i] != ';')
            s_arr_size += line[i++];
            
        int arr_size = stoi(s_arr_size);
        
        i += 1;
        string digits = "";
        vector<int> elems;
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
        int missing = missing_element(elems);
        cout << missing << endl;
    }
    return 0;
}