#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

class Solution {
public:

    vector<vector<string>> recursiveFindLadders(string beginWord, string endWord, unordered_set<string> &wordList, unordered_set<char>& unique_chars, vector<vector<string>>& ladders) {
        if (beginWord == endWord)
    }

    vector<vector<string>> findLadders(string beginWord, string endWord, unordered_set<string> &wordList) {
        vector<vector<string>> ladders;
        unordered_set<char> unique_chars;
        
        // Add all the unique characters.
        for (auto word : wordList) {
            for (auto c : word) {
                unique_chars.insert(c);
            }
        }

        recursiveFindLadders(beginWord, endWord, wordList, unique_chars, ladders);
        return ladders;
    }
};

int main() {
    Solution soln;
    string beginWord = "hit";
    string endWord = "cog";
    unordered_set<string> wordList { "hot","dot","dog","lot","log" };
    vector<vector<string>> ladders = soln.findLadders(beginWord, endWord, wordList);
}