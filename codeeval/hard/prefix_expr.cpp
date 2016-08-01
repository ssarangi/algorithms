#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

enum class OPS
{
    PLUS,
    MUL,
    DIV
};

struct Token
{
    int number;
    OPS op;
    
    bool is_number;
};

int expr(int num1, int num2, OPS op) {
    if (op == OPS::PLUS)
        return num1 + num2;
    else if (op == OPS::MUL)
        return num1 * num2;
    else
        return num1 / num2;
    
    return -1;
}

int evaluate(vector<Token>& tokens) {
    stack<Token> s;
    
    for (auto token : tokens) {
        if (!token.is_number) {
            s.push(token);
        } else {
            if (!s.top().is_number)
                s.push(token);
            else {
                int num1 = token.number;
                int num2 = s.top().number;
                s.pop();
                OPS op = s.top().op;
                s.pop();
                
                int val = expr(num1, num2, op);
                Token newtok;
                newtok.is_number = true;
                newtok.number = val;
                s.push(newtok);
            }
        }
    }
    
    // Only the final result needs to be calculated
    int num1 = s.top().number;
    return num1;
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    
    while (getline(stream, line)) {
        string s = "";
        vector<Token> tokens;
        for (auto c : line) {
            if (c == ' ') {
                Token t;
                if (s == "+") {
                    t.is_number = false;
                    t.op = OPS::PLUS;
                } else if (s == "*") {
                    t.is_number = false;
                    t.op = OPS::MUL;
                } else if (s == "/") {
                    t.is_number = false;
                    t.op = OPS::DIV;
                } else {
                    t.is_number = true;
                    t.number = stoi(s);
                }
                
                s = "";
                tokens.push_back(t);
            } else {
                s += c;
            }
        }
        
        Token newTok;
        newTok.is_number = true;
        newTok.number = stoi(s);
        tokens.push_back(newTok);
        
        int res = evaluate(tokens);
        cout << res << endl;
    }
    return 0;
}