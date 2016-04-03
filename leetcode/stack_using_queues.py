class Stack(object):
    class Queue:
        def __init__(self):
            self._data = []
            
        def put(self, x):
            self._data.append(x)
            
        def get(self):
            return self._data.pop()
            
        def empty(self):
            return len(self._data) == 0
            
        def __str__(self):
            return str(self._data)

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = Stack.Queue()
        self.other = Stack.Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.other.put(x)

        while not self.q.empty():
            el = self.q.get()
            self.other.put(el)
        
        self.other, self.q = self.q, self.other
        print(self.q)

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.q.empty():
            self.q.get()

    def top(self):
        """
        :rtype: int
        """
        top_el = self.q.get()
        
        self.other.put(top_el)
        while not self.q.empty():
            self.other.put(self.q.get())
        
        self.other, self.q = self.q, self.other
        return top_el

    def empty(self):
        """
        :rtype: bool
        """
        return self.q.empty()
        
s = Stack()

s.push(4)
s.push(2)
s.push(8)
s.push(1)

while not s.empty():
    print(s.top())
    s.pop()