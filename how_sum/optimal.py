

def optimal(target: int, nums: list) -> list:
    memo: dict = {}
    return how_sum(target, nums, memo)


def how_sum(target: int, nums: list, memo: dict) -> any:
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for num in nums:
        difference: int = target - num
        result = how_sum(difference, nums, memo)
        if result is not None:
            memo[target] = result + [num]
            return memo[target]
    memo[target] = None
    return None


if __name__ == '__main__':
    print(optimal(7, [4, 3]))
    print(optimal(300, [7, 14]))
