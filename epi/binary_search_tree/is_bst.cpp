// Check if a tree is a valid Binary Search Tree

#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int data;
    Node *left;
    Node *right;
    
    Node(int v)
    : data(v)
    , left(nullptr)
    , right(nullptr)
    {}
};

struct BST {
    Node *root;
    
    BST()
    : root(nullptr)
    {}
    
    void add_node(Node* node, int v) {
        if (v < node->data) {
            if (node->left) 
                add_node(node->left, v);
            else
                node->left = new Node(v);
        } else if (v > node->data) {
            if (node->right)
                add_node(node->right, v);
            else
                node->right = new Node(v);
        }
    }
    
    void add_node(int v) {
        if (root == nullptr)
            root = new Node(v);
        else {
            add_node(root, v);
        }
    }
    
    Node* find_key(int v) {
        if (root == nullptr)
            return nullptr;

        Node *cn = root;
        Node *prev = nullptr;
        
        while (cn != nullptr) {
            if (cn->data == v)
                return cn;
            if (cn->left && v < cn->left->data)
                cn = cn->left;
            else if (cn->right && v > cn->right->data)
                cn = cn->right;
        }
        
        return nullptr;
    }
    
    bool is_valid(Node* parent, Node *node) {
        if (node->left && node->left->data > node->data)
            return false;
            
        if (node->right && node->right->data < node->data)
            return false;
            
        // Now check if the parent needs to be checked
        if (parent) {
            // Check if the node is the left child or right child of parent
            if (parent->left == node)
                if (node->right && node->right->data > parent->data)
                    return false;
                    
            if (parent->right == node)
                if (node->left && node->left->data < parent->data)
                    return false;
        }
        
        bool c1 = true;
        if (node->left)
            c1 = is_valid(node, node->left);
            
        bool c2 = true;
        if (node->right)
            c2 = is_valid(node, node->right);
            
        return c1 && c2;
    }
    
    bool is_valid() {
        is_valid(nullptr, root);
    }
};

int main() {
    vector<int> elems = { 19, 7, 43, 3, 11, 2, 5, 17, 13, 23, 47, 37, 53, 29, 41, 31 };
    
    BST *bst = new BST();
    for (auto elem : elems) {
        bst->add_node(elem);
    }
    
    cout << bst->is_valid() << endl;
}