

def best_sum(target_sum: int, numbers: list) -> list:
    memo: dict = {}
    result = best_sum_recursive(target_sum, numbers, memo)
    return result if result is not None else []


def best_sum_recursive(target_sum: int, numbers: list, memo) -> any:
    if target_sum in memo:
        return memo[target_sum]
    elif target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    else:
        shortest_combination: any = None
        for num in numbers:
            difference: int = target_sum - num
            combination = best_sum_recursive(difference, numbers, memo)
            if combination is not None:
                combination = combination + [num]
                if shortest_combination is None or len(combination) < len(shortest_combination):
                    shortest_combination = combination
        memo[target_sum] = shortest_combination
        return shortest_combination


if __name__ == '__main__':
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(7, [2, 4]))
    print(best_sum(300, [7, 14]))
    print(best_sum(7, [2, 4, 3]))
    print(best_sum(8, [2, 3, 5]))
    print(best_sum(100, [1, 2, 5, 25]))
