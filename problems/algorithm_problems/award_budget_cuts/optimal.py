

def find_grants_cap(grants_array: list[int], new_budget: float):
    """
    Time Complexity: O(log(max(grants_array))
    Space Complexity: O(1)
    """
    hi = max(grants_array)
    lo = 0
    while lo <= hi:
        middle_cap: float = (lo + hi) / 2
        budget_calculation: float = get_budget_calculation(grants_array, middle_cap)
        if budget_calculation == new_budget:
            return middle_cap
        elif budget_calculation < new_budget:
            lo = middle_cap
        else:
            hi = middle_cap


def get_budget_calculation(grants_array, cap) -> float:
    """
    Time Complexity: O(n), but grants_array is capped at length 20,
    therefore the TC reduces to O(1)
    """
    possible_grant_reduction = grants_array.copy()
    for index in range(len(grants_array)):
        if possible_grant_reduction[index] > cap:
            possible_grant_reduction[index] = cap
    return sum(possible_grant_reduction)


if __name__ == '__main__':
    print(find_grants_cap([2, 100, 50, 120, 1000], 190))
