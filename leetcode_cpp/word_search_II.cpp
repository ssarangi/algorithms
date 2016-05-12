// https://leetcode.com/problems/word-search-ii/

#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

struct TrieNode {
    vector<TrieNode*> children;
    TrieNode() {
        children.resize(26, nullptr);
    }
};

struct Trie {
    TrieNode *root;
    
    void insert(char c) {
        TrieNode *pCN = root;
        if (root == nullptr) {
            root = new TrieNode();
        } else {
            root->insert(c);
        }
    }
    
    void search(char c) {
        
    }
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        unordered_set<string> word_set(words.begin(), words.end());
        
    }
};

int main() {
    vector<vector<char>> board = {
        {'o', 'a', 'a', 'n'},
        {'e', 't', 'a', 'e'},
        {'i', 'h', 'k', 'r'},
        {'i', 'f', 'l', 'v'},
    };
    
    vector<string> words = {"oath","pea","eat","rain"};
    
    
}