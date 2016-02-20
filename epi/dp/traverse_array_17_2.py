def traverse_array(width, height):
    arr = [[0 for i in range(0, width)] for j in range(0, height)]
    arr[0] = [1] * width

    # Since we can only go down and right so initialize the array with weight 1
    for y in range(0, height):
        arr[y][0] = 1

    for y in range(1, height):
        for x in range(1, width):
            arr[y][x] = arr[y-1][x] + arr[y][x-1]

    return arr[height - 1][width - 1]


def main():
    print(traverse_array(5, 5))
    
if __name__ == "__main__":
    main()