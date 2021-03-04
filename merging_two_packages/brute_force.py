

def brute_force(arr: list, limit: int) -> list:
    for i in range(arr):
        for j in range(arr):
            if i != j and arr[i] + arr[j] == limit:
                return get_correctly_ordered_pair(i, j)
    return []


def get_correctly_ordered_pair(i, j):
    if i < j:
        return [i, j]
    else:
        return [j, i]
