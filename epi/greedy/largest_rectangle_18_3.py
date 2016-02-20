import sys

class Stack(list):
    def push(self, item):
        self.append(item)

    def isEmpty(self):
        return not self

    def top(self):
        if not self.isEmpty():
            return self[-1]

        raise Exception("Calling top on empty list")

# O(n^2) solution
def largest_rectangle_unoptimized(heights):
    max_area = -sys.maxsize
    for i, h in enumerate(heights):
        for j in range(i, len(heights)):
            if heights[j] >= heights[i]:
                max_area = max(max_area, heights[i] * (j - i + 1))

    return max_area

# O(n) solution
def largest_rectangle(heights):
    # Keep the max height here as a stack
    max_height_stack = Stack()
    max_height_stack.push((heights[0], 0))

    max_area = -sys.maxsize
    for i, h in enumerate(heights):
        if h > max_height_stack.top()[0]:
            max_height_stack.push((h, i))
        elif h == max_height_stack.top()[0]:
            continue
        else:
            current_max_h, start = max_height_stack.pop()
            end = i - 1
            area = current_max_h * (end - start + 1)
            max_area = max(max_area, area)

    return max_area

def main():
    H = [1, 4, 4, 5, 5, 5, 4, 4, 7, 4, 3, 3, 1]
    print(largest_rectangle_unoptimized(H))
    print(largest_rectangle(H))

if __name__ == "__main__":
    main()