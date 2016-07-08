#include <iostream>
#include <cstring>

using namespace std;

void custom_memcpy(void* dst, void *src, int size) {
    // Start the copy
    int rem = size % 4;
    int num_iter = size / 4;
    
    int *intdst = (int*)dst;
    int *intsrc = (int*)src;
    for (int i = 0; i < num_iter; ++i) {
        *intdst = *intsrc;
        ++intdst;
        ++intsrc;
    }
    
    char *remdst = (char*)(intdst);
    char *remsrc = (char*)(intsrc);
    
    for (int i = 0; i < rem; ++i) {
        // Now copy the remaining bytes
        *remdst = *remsrc;
        ++remdst;
        ++remsrc;
    }
}

int main() {
    int size = 103;
    char* src = new char[size];
    
    for (int i = 0; i < size; ++i)
        src[i] = (char)(i);
        
    char *dst = new char[size];
    
    custom_memcpy(dst, src, size);
    
    if (memcmp(dst, src, size) != 0)
        cout << "Invalid memory copy" << endl;
    else
        cout << "Successful memory copy" << endl;
        
    return 0;
}