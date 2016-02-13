from geeksforgeeks.bst.bst

class Queue:
    def __init__(self):
        self.ds = []

    def enqueue(self, v):
        self.ds.append(v)

    def dequeue(self):
        val = self.ds[0]
        self.remove(val)
        return val

def main():
    pass

if __name__ == "__main__":
    main()