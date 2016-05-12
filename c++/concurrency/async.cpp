#include <future>
#include <iostream>

int called_from_async() {
    for (int i = 0; i < 1000; ++i) {
        std::cout << "Called from Async: " << i << std::endl;
    }
    
    return 1000;
}

int main() {
    std::future<int> result(std::async(called_from_async));
    
    std::cout << "Called from Main" << std::endl;
    
    result.get();
    
    return 0;
}