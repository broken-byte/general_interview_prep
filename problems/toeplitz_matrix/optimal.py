

def isToeplitz(arr):
    n = len(arr)
    m = len(arr[0])
    for row in range(n):
        for col in range(m):
            if diagonal_in_bounds(row, col, n, m) and diagonal_does_not_match(arr, row, col):
                return False
        return True


def diagonal_in_bounds(row, col, n, m):
    return row + 1 < n and col + 1 < m


def diagonal_does_not_match(arr, row, col):
    return arr[row][col] != arr[row + 1][col + 1]


if __name__ == '__main__':
    print(isToeplitz(
        [[1,2,3,4],
        [5,1,2,3],
        [6,5,1,2]]
        )
    )

    print(isToeplitz(
        [[1,2,3,4],
        [5,1,9,3],
        [6,5,1,2]]
        )
    )