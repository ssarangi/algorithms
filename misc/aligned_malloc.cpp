#include <cstdlib>
#include <cstdio>
#include <iostream>

void *aligned_malloc(size_t req_bytes, size_t alignment) {
    void *p1 = nullptr;
    void *p2 = nullptr;
    
    int offset = alignment + sizeof(void*);
    if ((p1 = (void *)malloc(req_bytes + offset)) == nullptr)
        return nullptr;

    std::cout << p1 << " -- " << size_t(p1) % alignment << std::endl;
    p2 = (void *)(size_t(p1) + (alignment - size_t(p1) % alignment) + sizeof(void*));
    return p2;
}

void aligned_free(void *p) {
    free(((void**)p)[-1]);
}

int main(int argc, char **argv) {
    char **endptr;
    int alignment = atoi(argv[1]);
    int *p = (int *)aligned_malloc(100, alignment);
    int *q = (int *)aligned_malloc(128, alignment);
    int *r = (int *)aligned_malloc(128, alignment);
    
    printf("%s: %p\n", argv[1], p);
    aligned_free(p);
    aligned_free(q);
    aligned_free(r);
    return 0;
}