import asyncio
import random

async def sort_operation(i, arr, start, end):
    print(i, arr[start], arr[end])
    # Assume that we have been broken up into 2 elements each
    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]

    print(i, arr[start], arr[end])

async def map(arr):
    break_size = 2 # Sort 10 elements at a time
    assert len(arr) % break_size == 0

    await asyncio.wait([
        sort_operation(i, arr, i * break_size, i * break_size + break_size - 1) for i in range(0, len(arr) // break_size)
    ])

def reduce(arr):
    pass

def main():
    max_limit = 20
    arr = [random.randint(0, max_limit) for i in range(0, max_limit)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(map(arr))

if __name__ == "__main__":
    main()