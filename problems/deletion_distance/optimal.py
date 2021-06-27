

def deletion_distance(str1: str, str2: str) -> int:
    """
    n = len(str1)
    m = len(str2)
    Time Complexity: O(n*m)
    Space Complexity: O(n*m)
    """
    length_1: int = len(str1)
    length_2: int = len(str2)
    min_deletion_table: list[list[int]] = create_seeded_min_deletions_table(len(str1), len(str2))
    for i in range(1, length_1 + 1):
        for j in range(1, length_2 + 1):
            if str1[i - 1] == str2[j - 1]:
                diagonal: int = min_deletion_table[i - 1][j - 1]
                min_deletion_table[i][j] = diagonal
            else:
                left_value: int = min_deletion_table[i][j - 1]
                up_value: int = min_deletion_table[i - 1][j]
                minimum_previous_value = min(left_value, up_value)
                min_deletion_table[i][j] = 1 + minimum_previous_value
    return min_deletion_table[-1][-1]


def create_seeded_min_deletions_table(length_1: int, length_2: int) -> list[list[int]]:  # O(n*m)
    min_deletion_table: list[list[int]] = [[0 for _ in range(length_2 + 1)] for _ in range(length_1 + 1)]
    seed_table(min_deletion_table)
    return min_deletion_table


def seed_table(min_deletions_table: list[list[int]]) -> None:  # O(n + m)
    for index in range(len(min_deletions_table)):
        min_deletions_table[index][0] = index
    for index in range(len(min_deletions_table[0])):
        min_deletions_table[0][index] = index


if __name__ == '__main__':
    print(f'expected: 3, actual: {deletion_distance(str1 = "dog", str2 = "frog")}')
    print(f'expected: 0, actual: {deletion_distance(str1 = "some", str2 = "some")}')
    print(f'expected: 9, actual: {deletion_distance(str1 = "some", str2 = "thing")}')
    print(f'expected: 0, actual: {deletion_distance(str1 = "", str2 = "")}')
