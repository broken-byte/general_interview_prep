from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """

        memo: dict = {}

        def rob_recursively(loot_inside_houses: List[int], current_house=-1) -> int:
            if current_house in memo:
                return memo[current_house]
            elif no_safe_houses_to_rob(loot_inside_houses, current_house):
                return loot_inside_houses[current_house]
            else:
                safe_houses_to_rob: List[int] = get_safe_houses_to_rob(loot_inside_houses, current_house)
                results: List[int] = []
                for safe_house in safe_houses_to_rob:
                    result: int = rob_recursively(loot_inside_houses, safe_house)
                    results.append(result)
                maximum_loot: int = 0
                if current_house != -1:
                    maximum_loot = max(results) + loot_inside_houses[current_house]
                else:
                    maximum_loot = max(results)
                memo[current_house] = maximum_loot
                return maximum_loot

        return rob_recursively(nums)


def no_safe_houses_to_rob(loot_inside_houses: List[int], current_house: int) -> bool:
    return current_house + 2 > len(loot_inside_houses) - 1


def get_safe_houses_to_rob(loot_inside_houses: List[int], current_house: int) -> List[int]:
    safe_houses_to_rob = []
    current: int = current_house + 2 if current_house != -1 else current_house + 1
    while current < len(loot_inside_houses):
        safe_houses_to_rob.append(current)
        current += 1
    return safe_houses_to_rob


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([2, 7, 9, 3, 1]))
    print(solution.rob([1, 2, 3, 1]))
