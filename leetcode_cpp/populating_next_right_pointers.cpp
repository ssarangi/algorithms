// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

#include <iostream>
#include <memory>
#include <queue>
#include <tuple>

using namespace std;

struct TreeLinkNode {
    int val;
    TreeLinkNode *left, *right, *next;
    TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
    
    ~TreeLinkNode() { cout << "Deleting object: " << val << std::endl; }
};


TreeLinkNode* create_tree() {
    TreeLinkNode *one = new TreeLinkNode(1);
    TreeLinkNode *two = new TreeLinkNode(2);
    TreeLinkNode *three = new TreeLinkNode(3);
    
    TreeLinkNode *four = new TreeLinkNode(4);
    TreeLinkNode *five = new TreeLinkNode(5);
    TreeLinkNode *six = new TreeLinkNode(6);
    TreeLinkNode *seven = new TreeLinkNode(7);

    one->left = two;
    one->right = three;
    
    two->left = four;
    two->right = five;
    
    three->left = six;
    three->right = seven;
    
    return one;
}

class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (root == nullptr)
            return;
            
        queue< tuple<TreeLinkNode*, int> > q;
        
        int current_level = -1;
        q.push(make_tuple(root, 0));
        
        
        TreeLinkNode *pPrev = nullptr;
        while (!q.empty()) {
            TreeLinkNode *pCN = nullptr;
            int level = -1;
            tie(pCN, level) = q.front();
            q.pop();
            
            // If the level is different from the current level then set the prev
            // pointer to nullptr. Since we are doing traversal on a new level
            // altogether.
            if (level != current_level) {
                pPrev = nullptr;
            } else {
                pPrev->next = pCN;
            }
            
            pPrev = pCN;
            current_level = level;
            if (pCN->left)
                q.push(make_tuple(pCN->left, level + 1));
                
            if (pCN->right)
                q.push(make_tuple(pCN->right, level + 1));
        }
    }
};

int main() {
    TreeLinkNode* root = create_tree();
    Solution soln;
    soln.connect(root);
    return 0;
}