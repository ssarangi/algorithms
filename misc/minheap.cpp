#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

class MinHeap {
public:
    MinHeap() { m_elements = {0}; }
    ~MinHeap() {}
    
    void insert(int v) {
        // Insert the element at the last position in the array
        m_elements.push_back(v);
        heapify_up();
    }
    
    void print() {
        copy(m_elements.begin(), m_elements.end(), ostream_iterator<int>(cout, " "));
        cout << endl;
    }
    
    int min() const { return m_elements[0]; }
    
    int pop() {
        if (m_elements.size() == 1)
            return -1;
            
        int v = m_elements[1];
        m_elements[1] = m_elements[m_elements.size() - 1];
        m_elements.pop_back();
        
        print();
        heapify_down();
        print();
        return v;
    }
    
    bool empty() const { return m_elements.size() == 1; }

private:
    void heapify_up() {
        int idx = m_elements.size() - 1;
        int parent = idx / 2;
        
        bool heapified = false;
        while (parent != idx && !heapified) {
            parent = idx / 2;
            if (m_elements[parent] > m_elements[idx]) {
                swap(m_elements[parent], m_elements[idx]);
                idx = parent;
            } else {
                heapified = true;
            }
        }
    }
    
    int smaller_child(int idx) {
        int child1 = 2 * idx;
        int child2 = 2 * idx + 1;
        
        if (child1 < m_elements.size() && child2 < m_elements.size()) {
            if (m_elements[child1] < m_elements[child2])
                return child1;
            else
                return child2;
        } else if (child1 < m_elements.size() && child2 >= m_elements.size()) {
            return child1;
        }
        
        return -1;
    }
    
    void heapify_down() {
        int parent = 1;
        int small_child = smaller_child(parent);
        
        while (small_child != -1) {
            swap(m_elements[parent], m_elements[small_child]);
            parent = small_child;
            small_child = smaller_child(parent);
        }
    }
    
private:
    vector<int> m_elements;
};

int main() {
    vector<int> elms = { 5, 1, 2, 9, 10, 4, 6, 8, 11, 20 };
    // vector<int> elms = { 5, 1 };
    
    MinHeap minheap;
    
    for (auto el : elms)
        minheap.insert(el);
    
    minheap.print();
    while (!minheap.empty()) {
        cout << minheap.pop() << endl;
    }
    
    return 0;
}