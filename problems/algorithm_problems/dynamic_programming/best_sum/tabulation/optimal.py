

def best_sum(target_sum: int, numbers: list[int]) -> list:
    """
    M = target
    N = len(numbers)
    Time Complexity: O(M^2*N)
    Space Complexity: O(M^2)
    """
    table: list = [None for _ in range(target_sum + 1)]
    table[0] = []
    for index in range(target_sum + 1):  # O(M)
        if table[index] is not None:
            tabulate(index, table, numbers)
    return table[target_sum]


def tabulate(index: int, table: list, numbers: list[int]):  # O(N*M)
    for num in numbers:  # O(N)
        if index + num < len(table):
            current_value = table[index + num]
            potential_value = table[index] + [num]  # O(M)
            if current_value is None or \
                    len(potential_value) < len(current_value):
                table[index + num] = potential_value


if __name__ == '__main__':
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(7, [2, 4]))
    print(best_sum(300, [7, 14]))
    print(best_sum(7, [2, 4, 3]))
    print(best_sum(8, [2, 3, 5]))
    print(best_sum(8, [1, 4, 5]))
    print(best_sum(100, [1, 2, 5, 25]))
