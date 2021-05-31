

def pancake_sort(arr: list[int]) -> list[int]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n: int = len(arr)
    current_size: int = n
    while current_size > 1:
        max_index: int = find_max(arr, current_size)
        if max_index != current_size - 1:
            move_max_to_end(max_index, current_size, arr)
        current_size -= 1
    return arr


def move_max_to_end(max_index: int, current_size: int, arr: list[int]):
    flip(arr, max_index)
    flip(arr, current_size - 1)


def find_max(arr: list[int], n: int):
    max_index = 0
    for i in range(0, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index


def flip(arr: list[int], k: int):
    start = 0
    while start < k:
        swap(start, k, arr)
        start += 1
        k -= 1


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]
