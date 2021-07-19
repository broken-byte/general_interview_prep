

def brute_force(arr: list, limit: int) -> list:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == limit:
                return get_correctly_ordered_pair(i, j)
    return []


def get_correctly_ordered_pair(i, j):
    pair: list = [i, j]
    return sorted(pair, reverse=True)


if __name__ == '__main__':
    print(brute_force([4, 6, 10, 15, 16], 21))