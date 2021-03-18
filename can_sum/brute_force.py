

def can_sum(arr: list, target: int) -> bool:
    """
    Time Complexity: O(n^(target))
    Space Complexity: O(target)
    """
    if target == 0:
        return True
    elif target < 0:
        return False
    for element in arr:
        remainder: int = target - element
        if can_sum(arr, remainder):
            return True
    return False


if __name__ == '__main__':
    print(can_sum([5, 3, 4, 7], 7))
    print(can_sum([2, 4], 7))
