

def better(arr: list, k: int):  # O(n*k)
    insertion_sort(arr)
    return arr


def insertion_sort(arr: list) -> None:
    n: int = len(arr)
    for i in range(n):
        for j in range(i, 0, -1):
            if is_less(arr[j], arr[j - 1]):
                exchange(arr, j, j - 1)
            else:
                break


def is_less(v: any, w: any) -> bool:
    return v < w


def exchange(arr: list, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]