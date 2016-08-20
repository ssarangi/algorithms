// https://www.codeeval.com/open_challenges/5/

#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

struct Node {
    int val;
    Node *next;
    
    Node(int v)
    : val(v)
    , next(nullptr)
    {}
};

Node* create_linked_list(vector<int>& elems) {
    unordered_map<int, Node*> dict;
    
    Node* prev = nullptr;
    Node* head = nullptr;
    
    for (auto elem : elems) {
        if (dict.find(elem) == dict.end()) {
            dict[elem] = new Node(elem);
            
            if (head == nullptr)
                head = dict[elem];
        }
        if (prev)
            prev->next = dict[elem];

        prev = dict[elem];
    }
    
    return head;
}

bool cycles_present(Node *head) {
    if (head == nullptr)
        return false;
    
    if (head->next == nullptr)
        return false;
    
    Node *slowptr = head;
    Node *fastptr = head->next->next;
    
    while (fastptr != nullptr && slowptr != nullptr) {
        if (fastptr == slowptr)
            return true;
        
        slowptr = slowptr->next;
        
        if (fastptr->next)
            fastptr = fastptr->next->next;
        else
            fastptr = fastptr->next;
    }
    
    return false;
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    while (getline(stream, line)) {
        // Now split the string into the individual digits
        int line_size = line.size();
        string digits = "";
        vector<int> elems;
        
        for (int i = 0; i < line_size; ++i) {
            if (line[i] == ' ') {
                elems.push_back(stoi(digits));
                digits = "";
            } else {
                digits += line[i];
            }
        }
        
        elems.push_back(stoi(digits));
        
        Node *head = create_linked_list(elems);
        
        bool is_cycle = cycles_present(head);
        
        cout << is_cycle << endl;
    }
    return 0;
}