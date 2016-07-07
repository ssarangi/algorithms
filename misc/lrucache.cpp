// LRU Cache implementation
#include <unordered_map>
#include <iostream>

using namespace std;

struct Node {
    Node(int id)
    : ID(id)
    , pNext(nullptr)
    , pPrev(nullptr)
    {}
    
    int ID;
    Node *pNext;
    Node *pPrev;
};

class LRUCache {
public:
    LRUCache(int size)
    : m_size(size)
    , m_currsize(0)
    , m_pHead(nullptr)
    {}
    
    void use(int val) {
        Node *cn = m_nodes[val];
        
        cout << "Using Node: " << val << endl;
        if (cn == m_pHead)
            return;
        
        // Disconnect the node first
        cn->pPrev->pNext = cn->pNext;
        
        // Move this node to the head of the cache
        cn->pNext = m_pHead;
        cn->pPrev = nullptr;
        m_pHead->pPrev = cn;
        m_pHead = cn;
    }
    
    void insert(int val) {
        if (m_currsize == m_size) {
            // We need to evict the last value in the cache.
            Node *pCurr = m_pHead;
            while (pCurr->pNext)
                pCurr = pCurr->pNext;
            
            cout << "Evicting LRU: " << pCurr->ID << endl;
            pCurr->pPrev->pNext = nullptr;
            if (pCurr == m_pHead)
                m_pHead = nullptr;
            delete pCurr;
            --m_currsize;
        }
        
        cout << "Inserting Item: " << val << endl;
        Node *pNew = new Node(val);
        pNew->pNext = m_pHead;
        
        if (m_pHead)
            m_pHead->pPrev = pNew;
            
        m_pHead = pNew;
        m_nodes[val] = pNew;
        ++m_currsize;
    }
    
private:
    int m_size;
    int m_currsize;
    unordered_map<int, Node*> m_nodes;
    Node *m_pHead;
};

int main() {
    LRUCache lrucache(3);
    
    lrucache.insert(10);
    lrucache.insert(11);
    lrucache.use(10);
    lrucache.insert(12);
    lrucache.use(10);
    lrucache.insert(15);
    lrucache.insert(16);
    return 0;
}