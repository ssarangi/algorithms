/*
Given a singly linked list, group all odd nodes together followed by the even 
nodes. Please note here we are talking about the node number and not the value 
in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
*/

#include <vector>
#include <iostream>

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        ListNode *pOdd = nullptr;
        ListNode *pEven = nullptr;
        
        if (head == nullptr)
            return head;
            
        pOdd = head;
        if (head->next != nullptr)
            pEven = head->next;
        
        ListNode *pEvenStart = pEven;
        ListNode *pOddStart = pOdd;
        
        ListNode *pOddIter = pOdd->next->next;
        ListNode *pEvenIter = pEven->next->next;
        
        // Now start looping through the list
        while (pEvenIter != nullptr) {
            pOdd->next = pOddIter;
            
            if (pOdd->next != nullptr)
                pOdd = pOdd->next;
                
            pEven->next = pEvenIter;
            if (pEven->next != nullptr)
                pEven = pEven->next;
                
            pOddIter = (pOddIter->next) ? pOddIter->next->next : nullptr;
            pEvenIter = (pEvenIter->next) ? pEvenIter->next->next : nullptr;
        }
        
        pOdd = pOdd->next;
        pOdd->next = pEvenStart;
        return pOddStart;
    }
    
    ListNode* create_list(std::vector<int>& arr) {
        ListNode *pRoot = nullptr;
        ListNode *pPrev = nullptr;
        
        for (auto v : arr) {
            ListNode *pCN = new ListNode(v);
            if (pRoot == nullptr)
                pRoot = pCN;
            else if (pPrev != nullptr)
                pPrev->next = pCN;
                
            pPrev = pCN;
        }
        
        return pRoot;
    }
    
    void print_list(ListNode *pHead) {
        while (pHead != nullptr) {
            std::cout << pHead->val << " ";
            pHead = pHead->next;
        }
        
        std::cout << std::endl;
    }
};

int main() {
    Solution soln;
    std::vector<int> arr = {1, 2, 3, 4, 5};
    ListNode *pHead = soln.create_list(arr);
    soln.print_list(pHead);
    pHead = soln.oddEvenList(pHead);
    soln.print_list(pHead);
    return 0;
}