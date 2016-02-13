class Stack:
    def __init__(self):
        self.ds = []

    def push(self, v):
        self.ds.append(v)

    def pop(self):
        self.ds.pop()

    def top(self):
        return self.ds[-1]

    def empty(self):
        return len(self.ds) == 0

    def max(self):
        pass

def main():
    s = Stack()
    s.push(4)
    s.push(1)
    s.push(2)
    s.pop()
    s.push(3)
    

if __name__ == "__main__":
    main()