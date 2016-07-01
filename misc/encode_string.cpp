#include <iostream>
#include <cstring>
#include <memory>

using namespace std;

unique_ptr<char> encode_string(unique_ptr<char> ubbuffer, int old_length, int new_length) {
    // Now start the copy of the string into the new one
    char *buffer = ubbuffer.get();
    int new_idx = new_length - 1;
    for (int i = old_length - 1; i >= 0; --i) {
        if (buffer[i] != ' ')
            buffer[new_idx--] = buffer[i];
        else
        {
            buffer[new_idx - 2] = '%';
            buffer[new_idx - 1] = '2';
            buffer[new_idx] = '0';
            new_idx -= 3;
        }
    }
    
    return std::move(ubbuffer);
}

int calculate_new_size(const char *inp_str, int len) {
    int num_spaces = 0;
    for (int i = 0; i < len; ++i) {
        if (inp_str[i] == ' ')
            num_spaces += 1;
    }
    
    return (len - num_spaces + (num_spaces * 3));
}

int main() {
    const char *orig_str = "This is a test";
    int length = strlen(orig_str);
    int new_length = calculate_new_size(orig_str, length);
    std::cout << "New Length: " << new_length << std::endl;
    
    // Create a new string to copy this into
    unique_ptr<char> pNewStr(new char[new_length]);
    memcpy(pNewStr.get(), orig_str, length);
    
    unique_ptr<char> new_str = encode_string(std::move(pNewStr), length, new_length);
    
    std::cout << new_str.get() << std::endl;
    
    return 0;
}