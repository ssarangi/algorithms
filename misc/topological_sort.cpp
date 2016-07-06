// https://www.youtube.com/watch?v=ddTC4Zovtbc

#include <iostream>
#include <vector>
#include <set>
#include <stack>
#include <algorithm>

using namespace std;

struct Node {
    char id;
    vector<Node*> incoming;
    vector<Node*> outgoing;
    
    void add_incoming(Node* node) {
        incoming.push_back(node);
    }
    
    void add_outgoing(Node* node) {
        node->add_incoming(this);
        outgoing.push_back(node);
    }
    
    Node(char id): id(id) {}
};

vector<Node*> create_graph() {
    Node *A = new Node('A');
    Node *B = new Node('B');
    Node *C = new Node('C');
    Node *D = new Node('D');
    Node *E = new Node('E');
    Node *F = new Node('F');
    Node *G = new Node('G');
    Node *H = new Node('H');
    
    A->add_outgoing(C);
    B->add_outgoing(C);
    C->add_outgoing(E);
    B->add_outgoing(D);
    D->add_outgoing(F);
    E->add_outgoing(F);
    F->add_outgoing(G);
    E->add_outgoing(H);
    
    vector<Node*> nodes = { A, B, C, D, E, F, G, H };
    return nodes;
}

void topological_sort_util(Node* curr, set<Node*>& visited, vector<Node*>& sorted) {
    for (auto outgoing : curr->outgoing)
        if (visited.find(outgoing) == visited.end())
            topological_sort_util(outgoing, visited, sorted);
    
    visited.insert(curr);
    sorted.push_back(curr);
}

vector<Node*> topological_sort(vector<Node*> nodes) {
    vector<Node*> sorted;
    set<Node*> visited;
    
    for (auto node: nodes) {
        if (visited.find(node) == visited.end()) {
            visited.insert(node);
            topological_sort_util(node, visited, sorted);
        }
    }
    
    return sorted;
}

int main() {
    vector<Node*> nodes = create_graph();
    vector<Node*> sorted = topological_sort(nodes);
    
    reverse(sorted.begin(), sorted.end());
    
    for (auto node: sorted)
        cout << node->id << " ";
        
    cout << endl;
    return 0;
}