

def can_sum(arr: list, target: int, memo: dict) -> bool:
    """
    Time Complexity: O(target*n)
    Space Complexity: O(target)
    """
    if target in memo:
        return memo[target]
    elif target == 0:
        return True
    elif target < 0:
        return False
    for element in arr:
        remainder: int = target - element
        if can_sum(arr, remainder, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False


if __name__ == '__main__':
    print(can_sum([5, 3, 4, 7], 7, {}))
    print(can_sum([2, 4], 7, {}))
    print(can_sum([7, 14], 300, {}))
