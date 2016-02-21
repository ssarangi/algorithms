class Stack(list):
    def push(self, el):
        self.append(el)

    def empty(self):
        return len(self) == 0

    def top(self):
        if len(self) > 0:
            return self[-1]

        raise Exception("Top called on an empty stack")

def normalize_path(path):
    s = Stack()
    # Split the paths by '/'
    paths = path.split("/")
    for p in paths:
        if p == '..':
            s.pop()
        elif p == '.' or p == '':
            continue
        else:
            s.push(p)

    final_path = ""
    while not s.empty():
        final_path = s.pop() + "/" + final_path

    return "/" + final_path

def main():
    print(normalize_path("/usr/lib/../bin/gcc"))

if __name__ == "__main__":
    main()