from queue import Queue

def get_new_string(s, idx):
    i1 = idx[0] - 1
    i2 = idx[1] - 1

    new_s = s[0:i1]
    new_s += s[i2]
    new_s += s[i1+1:i2]
    new_s += s[i1]

    return new_s

def lexicographically_largest_string(s, *args):
    q = Queue()
    q.put(s)

    visited = {}
    max_str = s
    while not q.empty():
        node = q.get()
        if node in visited:
            continue

        visited[node] = True
        max_str = max(max_str, node)

        for swap_idx in args:
            new_s = get_new_string(node, swap_idx)
            q.put(new_s)

    return max_str

def main():
    s = "abdc"
    print(lexicographically_largest_string(s, (1, 4), (3, 4)))

if __name__ == "__main__":
    main()