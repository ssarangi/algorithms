#include <vector>
#include <queue>
#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode *create_sorted_list(std::vector<int>& l) {
    ListNode *pHead = nullptr;
    ListNode *pCurr = nullptr;
    
    for (auto v : l) {
        if (pHead == nullptr) {
            pHead = new ListNode(v);
            pCurr = pHead;
        } else {
            pCurr->next = new ListNode(v);
            pCurr = pCurr->next;
        }
    }
    
    return pHead;
}

void print_list(ListNode *pHead) {
    if (pHead == nullptr)
        return;
        
    ListNode *pCurr = pHead;
    while (pCurr != nullptr) {
        std::cout << pCurr->val << std::endl;
        pCurr = pCurr->next;
    }
}

class Solution {
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        auto cmp = [](ListNode *left, ListNode *right) { return left->val > right->val; };
        
        std::priority_queue<ListNode*, std::vector<ListNode*>, decltype(cmp) > pq(cmp);
        
        for (auto listnode : lists) {
            if (listnode)
                pq.push(listnode);
        }
        
        ListNode *pHead = nullptr;
        ListNode *pPrev = nullptr;
        
        while (!pq.empty()) {
            ListNode *pCN = pq.top();
            pq.pop();
            
            if (pHead == nullptr) {
                pHead = pCN;
                if (pCN->next)
                    pq.push(pCN->next);
            } else {
                if (pCN->next)
                    pq.push(pCN->next);
                
                pPrev->next = pCN;
            }
            

            pPrev = pCN;
        }
        
        return pHead;
    }
};

int main() {
    std::vector<int> l1 = {1,3,5,7,9};
    std::vector<int> l2 = {2,4,6,8,10};
    std::vector<int> l3 = {12,13,14,15,16};
    
    ListNode *pL1 = create_sorted_list(l1);
    ListNode *pL2 = create_sorted_list(l2);
    ListNode *pL3 = create_sorted_list(l3);
    
    // std::vector<ListNode*> sorted_lists = {pL1, pL2, pL3};
    std::vector<ListNode*> sorted_lists = {pL1, nullptr};
    
    Solution soln;
    ListNode *pNewHead = soln.mergeKLists(sorted_lists);
    print_list(pNewHead);
}