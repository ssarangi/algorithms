// https://www.codeeval.com/open_challenges/76/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

bool check_rotation(string& s1, string& s2, int rotation_pt) {
    set<string> present;
    
    string s1_fh = s1.substr(0, rotation_pt);
    string s1_sh = s1.substr(rotation_pt);
    
    present.insert(s1_fh);
    present.insert(s1_sh);
    
    int new_rot_pt = s1.size() - rotation_pt;
    string s2_fh = s2.substr(0, new_rot_pt);
    string s2_sh = s2.substr(new_rot_pt);
    
    if (present.find(s2_fh) != present.end() &&
        present.find(s2_sh) != present.end())
        return true;
        
    return false;
}

bool is_rotation(string& s1, string& s2) {
    // Determine if string s1 is a rotation of string s2.
    if (s1.size() != s2.size())
        return false;
        
    int length = s1.size();
    
    for (int i = 1; i < length; ++i)
        if (check_rotation(s1, s2, i))
            return true;
    
    return false;
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    while (getline(stream, line)) {
        // Split the line at the comma.
        vector<string> words;
        string word = "";
        for (auto c : line) {
            if (c != ',') {
                word += c;
            }
            else {
                words.push_back(word);
                word = "";
            }
        }
        
        words.push_back(word);
        
        bool is_true = is_rotation(words[0], words[1]);
        if (is_true)
            cout << "True" << endl;
        else
            cout << "False" << endl;
    }
    return 0;
}