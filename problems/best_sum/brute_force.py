

def best_sum(target_sum: int, numbers: list) -> any:
    if target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    else:
        combinations: list = []
        for num in numbers:
            difference: int = target_sum - num
            result = best_sum(difference, numbers)
            if result is not None:
                result = result + [num]
                combinations.append(result)
        if len(combinations) != 0:
            return min(combinations, key=len)
        else:
            return None


if __name__ == '__main__':
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(7, [2, 4]))
    print(best_sum(300, [7, 14]))
    print(best_sum(7, [2, 4, 3]))
    print(best_sum(8, [2, 3, 5]))


