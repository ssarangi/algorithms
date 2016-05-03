#include <iostream>
#include <thread>

class thread_guard {
public:
    explicit thread_guard(std::thread& t_)
    : m_t(t_) {}
    
    ~thread_guard() {
        if (m_t.joinable()) {
            m_t.join();
        }
    }
    
    thread_guard(thread_guard const&)=delete;
    thread_guard& operator=(thread_guard const&)=delete;

private:
    std::thread& m_t;
};

int main() {
    std::thread t([]() { std::cout << "Hello I am in thread" << std::endl; });
    thread_guard g(t);
    
    std::cout << "I am in global scope" << std::endl;
    return 0;
}