

def move_zeros_to_end(arr: list[int]) -> list[int]:
    """
    TC: O(n)
    SC: O(1)
    """
    length = len(arr) - 1
    index = 0
    swap_cursor = 0
    while index < length and swap_cursor < length:
        if arr[index] == 0:
            index, swap_cursor = swap_non_zeros_left(arr, index, swap_cursor)
        else:
            index += 1
            swap_cursor += 1
    return arr


def swap_non_zeros_left(arr: list[int], index: int, swap_cursor: int) -> tuple[int, int]:
    length: int = len(arr)
    swap_cursor: int = move_swap_cursor_in_front_of_zeros(swap_cursor, arr)
    while swap_cursor < length and arr[swap_cursor] != 0:
        swap(arr, index, swap_cursor)
        index += 1
        swap_cursor += 1
    return index, swap_cursor


def move_swap_cursor_in_front_of_zeros(swap_cursor: int, arr: list[int]) -> int:
    length: int = len(arr)
    while swap_cursor < length and arr[swap_cursor] == 0:
        swap_cursor += 1
    return swap_cursor


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    print(move_zeros_to_end([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))
    print(move_zeros_to_end([1, 0, 5, 0, 0, 0, 0]))
