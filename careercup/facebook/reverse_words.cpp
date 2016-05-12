#include <iostream>

void reverse_words(char* buffer, int size) {
    char *p1 = buffer + 0;
    char *p2 = buffer + size - 1;

    while (p1 < p2) {
        char tmp = *p1;
        *p1 = *p2;
        *p2 = tmp;
        p1 += 1;
        p2 -= 1;
    }
}

int main() {
    int size = 12;
    char *buffer = (char *)(malloc(size));
    memcpy(buffer, "Hello World\0", size);

    reverse_words(buffer, size - 1);
    char *p1 = buffer;
    int word_size = 0;
    char *end = buffer + size;

    while (p1 + word_size < end) {
        if (*(p1 + word_size) == ' ' || *(p1 + word_size) == '\0') {
            reverse_words(p1, word_size);
            p1 += word_size + 1;
            word_size = 0;
        }
        else {
            word_size += 1;
        }
    }

    std::cout << buffer << std::endl;
    free(buffer);
    return 0;
}