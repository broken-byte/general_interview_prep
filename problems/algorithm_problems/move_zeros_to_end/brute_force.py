

def move_zeros_to_end(arr: list[int]) -> list[int]:
    """
    TC: O(n)
    SC: O(n)
    """
    output: list[int] = []
    zero_counter: int = 0
    for num in arr:
        if num != 0:
            output.append(num)
        else:
            zero_counter += 1
    for _ in range(zero_counter):
        output.append(0)
    return output


if __name__ == '__main__':
    print(
        move_zeros_to_end([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]) == [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]
    )
