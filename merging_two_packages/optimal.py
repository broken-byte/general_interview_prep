
def optimal(arr: list, limit: int) -> list:
    hashed_values = create_hashed_arr(arr)
    for current_index, key in enumerate(arr):
        difference: int = limit - key
        diff_index: int = hashed_values[limit - key]
        if difference in hashed_values and indices_not_equal(diff_index, current_index):
            ans = correctly_ordered_pair(current_index, diff_index)
            return ans
    return []


def create_hashed_arr(arr: list):
    hashed_arr = {}
    for index, num in enumerate(arr):
        hashed_arr[num] = index
    return hashed_arr


def correctly_ordered_pair(i: int, j: int):
    if i > j:
        return [i, j]
    else:
        return [j, i]


def indices_not_equal(i: int, j: int):
    return i != j
