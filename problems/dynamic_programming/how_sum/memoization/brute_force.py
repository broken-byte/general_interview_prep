

def brute_force(target: int, nums: list) -> list:
    """
    n = target
    m = len(nums)
    Time Complexity: O(m * n^m)
    Space Complexity: O(m)
    """
    return how_sum(target, nums)


def how_sum(target: int, nums: list) -> any:
    if target == 0:
        return []
    elif target < 0:
        return None
    else:
        for num in nums:
            difference: int = target - num
            result = how_sum(difference, nums)
            if result is not None:
                return result + [num]


if __name__ == '__main__':
    print(brute_force(7, [2, 4, 3]))
    print(brute_force(300, [7, 14]))
