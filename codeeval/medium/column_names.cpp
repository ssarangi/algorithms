#include <iostream>
#include <fstream>
#include <string>
#include <stack>

using namespace std;

string getColumnName(int num) {
    if (num < 0)
        return "";
    
    string s = "";
    while (num > 0) {
        int remainder = (num - 1) % 26;
        s = (char)(65 + remainder) + s;
        num = (num - remainder) / 26;
    }
    
    return s;
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    while (getline(stream, line)) {
        int num = stoi(line);
        cout << getColumnName(num) << endl;
    }
    return 0;
}