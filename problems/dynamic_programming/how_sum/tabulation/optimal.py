

def how_sum(target: int, nums: list[int]) -> list[int]:
    """
    M = target
    N = len(nums)
    Time Complexity: O(M*N*M0 -> O(M^2*N)
    Space Complexity: O(M^2)
    """
    table: list = [None for _ in range(target + 1)]
    table[0]: list[int] = []
    for index in range(target + 1):  # O(m)
        tabulate(index, table, nums)
    return table[target]


def tabulate(index: int, table: list, nums: list[int]):  # O(n*m)
    if table[index] is None:
        return
    for num in nums:  # O(n)
        if index + num < len(table):
            table[index + num] = table[index] + [num]  # O(m)


if __name__ == '__main__':
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(7, [2, 4]))
    print(how_sum(300, [7, 14]))
    print(how_sum(21, [3, 4, 5, 7]))
