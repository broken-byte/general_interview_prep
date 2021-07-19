

def deletion_distance(str1: str, str2: str) -> int:
    """
    n = len(str1)
    m = len(str2)
    Time Complexity: O(n*m)
    Space Complexity: O(min(n, m))
    """
    if len(str1) < len(str2):
        temp = str1
        str1 = str2
        str2 = temp
    length_1: int = len(str1)
    length_2: int = len(str2)
    previous = [index for index in range(length_2 + 1)]
    current = [0 for _ in range(length_2 + 1)]
    for i in range(1, length_1 + 1):
        current[0] = i
        for j in range(1, length_2 + 1):
            if str1[i - 1] == str2[j - 1]:
                diagonal: int = previous[j - 1]
                current[j] = diagonal
            else:
                left_value: int = current[j - 1]
                up_value: int = previous[j]
                minimum_previous_value: int = min(left_value, up_value)
                current[j] = 1 + minimum_previous_value
        previous = current.copy()
    return current[-1]


if __name__ == '__main__':
    print(f'expected: 3, actual: {deletion_distance(str1="hit", str2="heat")}')
    print(f'expected: 3, actual: {deletion_distance(str1 = "dog", str2 = "frog")}')
    print(f'expected: 0, actual: {deletion_distance(str1 = "some", str2 = "some")}')
    print(f'expected: 9, actual: {deletion_distance(str1 = "some", str2 = "thing")}')
    print(f'expected: 0, actual: {deletion_distance(str1 = "", str2 = "")}')
