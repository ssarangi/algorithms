class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []
        self._other = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self._data.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self._other) == 0:
            # Move all the elements from self._data to self._other
            while len(self._data) > 0:
                self._other.append(self._data.pop())
            
        el = self._other.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self._other[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self._data) == 0
        
q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)

while not q.empty():
    print(q.peek())
    q.pop()