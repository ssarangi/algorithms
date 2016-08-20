// https://www.codeeval.com/open_challenges/11/submit/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct Node {
    int val;
    Node *left;
    Node *right;
    
    Node(int v)
    : val(v)
    , left(nullptr)
    , right(nullptr)
    {}
};

int find_lca(Node *root, Node *n1, Node *n2) {
    if (n1->val < root->val && n2->val < root->val)
        return find_lca(root->left, n1, n2);
    else if (n1->val > root->val && n2->val > root->val)
        return find_lca(root->right, n1, n2);
    else
        return root->val;
}

Node *find_node(Node *node, int v) {
    if (node == nullptr)
        return nullptr;
        
    if (node->val == v)
        return node;
        
    if (v < node->val)
        return find_node(node->left, v);
    else if (v > node->val)
        return find_node(node->right, v);
}

Node* create_tree() {
    Node *root = new Node(30);
    Node *left = new Node(8);
    Node *right = new Node(52);
    
    root->left = left;
    root->right = right;
    
    left->left = new Node(3);
    left->right = new Node(20);
    
    left->right->left = new Node(10);
    left->right->right = new Node(29);
    
    return root;
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    
    Node *root = create_tree();
    
    while (getline(stream, line)) {
        int i = 0;
        string digits = "";
        vector<int> elems;
        
        while (i < line.size()) {
            if (line[i] == ' ') {
                elems.push_back(stoi(digits));
                digits = "";
            } else {
                digits += line[i];
            }
            
            ++i;
        }
        
        elems.push_back(stoi(digits));
        
        int lca = find_lca(root, find_node(root, elems[0]), find_node(root, elems[1]));
        cout << lca << endl;
    }
    
    return 0;
}