from numpy import zeros

"""
This solution assumes that source and target are always at
(0,0) and (n - 1, m - 1), respectively
"""


def grid_traveler_forward_facing(n: int, m: int) -> int:
    table = zeros((n + 1, m + 1), dtype=int)
    table[1][1] = 1
    table_rows = n + 1
    table_cols = m + 1
    for row in range(table_rows):
        for col in range(table_cols):
            if row + 1 < table_rows:
                table[row + 1][col] += table[row][col]
            if col + 1 < table_cols:
                table[row][col + 1] += table[row][col]
    return table[n][m]


def grid_traveler_backwards_facing(n: int, m: int) -> int:
    table = zeros((n + 1, m + 1), dtype=int)
    table[1][1] = 1
    table_rows = n + 1
    table_cols = m + 1
    for row in range(1, table_rows):
        for col in range(1, table_cols):
            table[row][col] += table[row - 1][col] + table[row][col - 1]
    return table[n][m]


if __name__ == '__main__':
    print(grid_traveler_forward_facing(1, 1))
    print(grid_traveler_forward_facing(2, 3))
    print(grid_traveler_forward_facing(3, 2))
    print(grid_traveler_forward_facing(3, 3))
    print(grid_traveler_forward_facing(18, 18))

    print(grid_traveler_backwards_facing(1, 1))
    print(grid_traveler_backwards_facing(2, 3))
    print(grid_traveler_backwards_facing(3, 2))
    print(grid_traveler_backwards_facing(3, 3))
    print(grid_traveler_backwards_facing(18, 18))
