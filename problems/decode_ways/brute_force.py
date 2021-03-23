

def brute_force(s: str) -> int:
    """
    This method COULD work if you
    somehow keep track of the order
    of the sub-arrays as they appear
    in the original string, but I'm
    gonna move on to the optimal
    DP solution to this problem
    since that MIGHT be the only
    way to solve this and I need
    to practice DP anyway LOL.
    """
    alphabet_map: dict = generate_alphabet_map()
    print(alphabet_map)
    contiguous_sub_arrays: list = get_all_contiguous_sub_arrays_of_string(s)  # O(n^3)
    print(contiguous_sub_arrays)
    for i, sub_array in enumerate(contiguous_sub_arrays):
        if int(sub_array) not in alphabet_map:
            contiguous_sub_arrays.pop(i)
    print(contiguous_sub_arrays)
    return 0


def generate_alphabet_map() -> dict:
    alphabet_map: dict = {}
    code: int = 1
    for letter_value in range(65, 91):
        alphabet_map[code] = chr(letter_value)
        code += 1
    return alphabet_map


def get_all_contiguous_sub_arrays_of_string(s: str) -> list:
    n: int = len(s)
    contiguous_sub_arrays: list = []
    for i in range(n):
        for j in range(i, n):
            sub_array: str = s[i: j + 1]
            contiguous_sub_arrays.append(sub_array)
    return contiguous_sub_arrays


if __name__ == '__main__':
    brute_force("226")
