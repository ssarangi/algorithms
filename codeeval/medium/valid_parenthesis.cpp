#include <iostream>
#include <fstream>
#include <string>
#include <stack>

using namespace std;

bool is_valid(const string& line) {
    if (line.size() == 0)
        return false;
        
    stack<char> S;
    
    for (auto c : line) {
        if (c == '[' || c == '{' || c == '(')
            S.push(c);
        else if (c == ']' || c == '}' || c == ')') {
            // Pop the stack to see we have a corresponding opening parens
            if (S.empty())
                return false;
                
            char op = S.top();
            S.pop();
            if ((op == '[' && c != ']') ||
                (op == '{' && c != '}') ||
                (op == '(' && c != ')'))
                return false;
        }
    }
    
    if (S.size() > 0)
        return false;
        
    return true;
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    while (getline(stream, line)) {
        // Now we have the line with parens. Figure out whether its valid or not.
        if (is_valid(line))
            cout << "True" << endl;
        else
            cout << "False" << endl;
    }
    return 0;
}