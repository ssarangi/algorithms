#include <iostream>

using namespace std;

void test_pointer(int **ptr) {
    *ptr = new int;
    **ptr = 19;
}

int main() {
    int **ptr = new int*[1];
    test_pointer(ptr);
    cout << *ptr << " -- " << **ptr << endl;
    return 0;
}