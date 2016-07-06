// Implements all the functions of a binary search tree
// This code implements the inorder traversal of a BST with O(1) space. No extra
// space is used for this which makes it elegant code. However, it does need parent
// pointers so have to figure out how to use the stack for use without parent pointers.

#include <iostream>
#include <vector>
#include <stack>
#include <iterator>

using namespace std;

template <typename T>
struct Node {
    Node *left;
    Node *right;
    Node *parent;
    T     data;
    
    T get() { return data; }
    
    Node(T val, Node<T>* parent)
    : left(nullptr)
    , right(nullptr)
    , parent(parent)
    , data(val)
    {}
};

template <typename T>
class BinaryTree {
public:
    BinaryTree()
    : m_pRoot(nullptr) 
    {}
    
    ~BinaryTree() {}
    
    Node<T>* getRoot() { return m_pRoot; }
    
    void setRoot(T data) { m_pRoot = new Node<T>(data, nullptr); }
    
    void insert(T data, Node<T> *nodeToInsert) {
        if (data < nodeToInsert->get()) {
            if (nodeToInsert->left)
                insert(data, nodeToInsert->left);
            else
                nodeToInsert->left = new Node<T>(data, nodeToInsert);
        } else if (data > nodeToInsert->get()) {
            if (nodeToInsert->right)
                insert(data, nodeToInsert->right);
            else
                nodeToInsert->right = new Node<T>(data, nodeToInsert);
        }
    }
    
    void inorder_traversal(vector<T>& arr) {
        Node<T>* curr = m_pRoot;
        Node<T>* prev = nullptr;
        
        bool complete = false;
        while (!complete) {
            if (curr->left == prev) {
                arr.push_back(curr->data);
                // We have completed the left subtree so check the right subtree
                if (curr->right) {
                    prev = curr;
                    curr = curr->right;
                }
            } else if (curr->right == prev) {
                // We have completed the entire right subtree too. So just
                // return.
                if (curr->parent) {
                    prev = curr;
                    curr = curr->parent;
                } else 
                    complete = true;
                
            } else {
                // Go to the left most subtree of this node
                while (curr->left) {
                    prev = curr;
                    curr = curr->left;
                }
                
                // Now we reached the left most node. process it
                arr.push_back(curr->data);
                
                // Check if the curr node has any right child
                if (curr->right) {
                    prev = curr;
                    curr = curr->right;
                } else {
                    // We are done processing all subtrees of this node
                    prev = curr;
                    curr = curr->parent;
                }
            }
        }
    }
    

private:
    Node<T> *m_pRoot;
};

int main() {
    vector<int> elems = { 5, 8, 9, 2, 1, 3, 4, 7 };
    BinaryTree<int>* pBST = new BinaryTree<int>();
    
    for (auto elem : elems) {
        if (pBST->getRoot() == nullptr)
            pBST->setRoot(elem);
        else
            pBST->insert(elem, pBST->getRoot());
    }
    
    vector<int> inorder;
    pBST->inorder_traversal(inorder);
    std::copy(inorder.begin(), inorder.end(), ostream_iterator<int>(cout, " ")); 
    cout << endl;
    return 0;
}