#include <iostream>
#include <algorithm>
#include <stack>
#include <iterator>
#include <limits>

class Node
{
public:
    Node(int val)
    : m_val(val)
    , m_pLeft(nullptr)
    , m_pRight(nullptr)
    {}
    
    ~Node() {}
    
    void insert(int v)
    {
        if (v < m_val)
        {
            if (m_pLeft == nullptr)
                m_pLeft = new Node(v);
            else
                m_pLeft->insert(v);
        }
        else if (v > m_val)
        {
            if (m_pRight == nullptr)
                m_pRight = new Node(v);
            else
                m_pRight->insert(v);
        }
    }
    
    Node* left()
    {
        return m_pLeft;
    }
    
    Node* right()
    {
        return m_pRight;
    }
    
private:
    int m_val;
    Node* m_pLeft;
    Node* m_pRight;
};

Node* create_tree(std::vector<int>& arr)
{
    Node* pRoot = nullptr;
    
    for (auto v : arr)
    {
        Node* pNode = new Node(v);
        if (pRoot == nullptr)
            pRoot = pNode;
        else
        {
            pRoot->insert(v);
        }
    }
    
    return pRoot;
}

int min_diff(Node* pRoot)
{
    if (pRoot == nullptr)
        return 0;
    
    std::stack<Node*> s;
    s.push(pRoot);
    
    std::vector<int> inorder;
    while (!s.empty())
    {
        
    }
}

int main()
{
    std::vector<int> arr = {10, 5, 16, 12, 20};
    Node *pRoot = create_tree(arr);
    std::copy(arr.begin(), arr.end(), std::ostream_iterator<int>(std::cout, " "));
    return 1;
}