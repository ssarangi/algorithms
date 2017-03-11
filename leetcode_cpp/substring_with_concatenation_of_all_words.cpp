#include <vector>
#include <string>
#include <unordered_map>
#include <iterator>
#include <iostream>

using namespace std;

class Solution {
public:
    bool are_all_words_accounted_for(unordered_map<string, int>& hash_table) {
        for (auto item : hash_table) {
            if (item.second != 1)
                return false;
        }
        
        return true;
    }

    vector<int> findSubstring(string s, vector<string>& words) {
        int start_pos = 0;
        int curr_pos = 0;
        int word_len = 0;
        vector<int> results;
        
        while (curr_pos < s.size()) {
            // Reinitialize the map on each iteration
            unordered_map<string, int> hash_table;
            for (auto word: words) {
                word_len = word.size();
                hash_table[word] = 0;
            }
            
            string curr_word = "";
            bool no_intervening_word = true;
            
            while (no_intervening_word && curr_pos < s.size()) {
                curr_word += s[curr_pos];
                if (curr_word.size() == word_len) {
                    if (hash_table.find(curr_word) != hash_table.end() &&
                        hash_table[curr_word] < 1) {
                        if (are_all_words_accounted_for(hash_table)) {
                            results.push_back(start_pos);
                            no_intervening_word = false;
                        }
                            
                        // Reset the counter
                        start_pos = curr_pos;
                    }
                }
                
                curr_pos += 1;
            }
        }
        
        return results;
    }
};

int main() {
    Solution soln;
    
    string s = "barfoothefoobarman";
    vector<string> words = {"foo", "bar"};
    vector<int> results = soln.findSubstring(s, words);
    std::copy(results.begin(), results.end(), ostream_iterator<int>(cout, " "));
    return 0;
}