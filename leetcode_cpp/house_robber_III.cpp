#include <iostream>
#include <algorithm>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int rob(TreeNode* root) {
        return std::max(
            dfs(root, root->val, true),
            dfs(root, 0, false)
        );
    }
    
    int dfs(TreeNode *pNode, int profit, bool parent_robbed) {
        if (pNode == nullptr)
            return profit;
        
        int c1, c2;
        if (parent_robbed) {
            c1 = dfs(pNode->left, profit, false);
            c2 = dfs(pNode->right, profit, false);
        }
        else {
            c1 = std::max(
            dfs(pNode->left, profit + pNode->val, true), dfs(pNode->left, profit, false));
            
            c2 = std::max(
            dfs(pNode->right, profit + pNode->val, true), dfs(pNode->right, profit, false));
        }
        
        return c1 + c2;
    }
};

TreeNode* create_tree() {
    TreeNode *pRoot = new TreeNode(3);
    TreeNode *pLeft = new TreeNode(2);
    TreeNode *pRight = new TreeNode(3);
    
    TreeNode *pLeftRight = new TreeNode(3);
    TreeNode *pRightRight = new TreeNode(1);
    
    pRoot->left = pLeft;
    pRoot->right = pRight;
    pLeft->right = pLeftRight;
    pRight->right = pRightRight;
    
    return pRoot;
}

int main() {
    TreeNode *pRoot = create_tree();
    Solution soln;
    int max_profit = soln.rob(pRoot);
    std::cout << max_profit << std::endl;
    return 0;
}