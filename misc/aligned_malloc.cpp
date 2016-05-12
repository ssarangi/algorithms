#include <cstdlib>
#include <cstdio>

void *aligned_malloc(size_t req_bytes, size_t alignment) {
    void *p1 = nullptr;
    void **p2 = nullptr;
    
    int offset = alignment - 1 + sizeof(void*);
    if ((p1 = (void *)malloc(req_bytes + offset)) == nullptr)
        return nullptr;
        
    // p2 = (void **)(((size_t)p1 + offset) & ~(alignment - 1));
    p2 = (void **)(size_t(p1) + (alignment - size_t(p1) % alignment));
    p2[-1] = p1;
    return p2;
}

void aligned_free(void *p) {
    free(((void **)p)[-1]);
}

int main(int argc, char **argv) {
    char **endptr;
    int *p = (int *)aligned_malloc(100, strtol(argv[1], endptr, 10));
    
    printf("%s: %p\n", argv[1], p);
    aligned_free(p);
    return 0;
}