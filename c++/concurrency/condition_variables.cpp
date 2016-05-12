struct BoundedBuffer {
    int *buffer;
    int capacity;
    
    int front;
    int rear;
    int count;
    
    std::mutex lock;
    
    std::condition_variable not_full;
    std::condition_variable not_empty;
    
    BoundedBuffer(int capacity)
    : capacity(capacity)
    , front(0)
    , rear(0)
    , count(0) {
        buffer = new int[capacity];
    }
    
    ~BoundedBuffer() {
        delete[] buffer;
    }
    
    void put(int data) {
        std::unique_lock<std::mutex> l(lock);
        
    }
}