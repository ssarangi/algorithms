// Given a string S, print the longest substring P such that P > S lexicographically. 
// You may assume that such substring exists.
#include <string>
#include <iostream>

using namespace std;

std::string longest_substring(std::string S) {
    for (auto c : S) {
        std::cout << c << std::endl;
    }
}

int main() {
    std::string s1 = "abc";
    std::cout << longest_substring(s1) << std::endl;
}