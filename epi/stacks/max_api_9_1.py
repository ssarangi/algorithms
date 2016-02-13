class Stack:
    def __init__(self):
        self.ds = []
        self.maxv = None

    def push(self, v):
        if len(self.ds) == 0:
            self.maxv = v

        self.ds.append((v, max(self.maxv, v)))

    def pop(self):
        self.ds.pop()

    def peek(self):
        return self.ds[-1]

    def empty(self):
        return len(self.ds) == 0

    def max(self):
        if self.empty():
            raise Exception("No elements in the stack")

        return self.ds[-1][1]

def main():
    s = Stack()
    s.push(2)
    s.push(1)
    s.push(4)
    print(s.max())
    s.pop()
    s.push(3)
    

if __name__ == "__main__":
    main()